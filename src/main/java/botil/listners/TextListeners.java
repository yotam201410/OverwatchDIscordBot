package botil.listners;

import botil.exceptions.OuterApiException;
import botil.exceptions.RepositorySearchEmpty;
import botil.exceptions.TokenOutdatedException;
import botil.Globals;
import botil.repositores.GuildRepository;
import botil.repositores.UserRepository;
import net.dv8tion.jda.api.entities.Message;
import net.dv8tion.jda.api.entities.Role;
import net.dv8tion.jda.api.events.message.MessageReceivedEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;
import org.jetbrains.annotations.NotNull;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import javax.net.ssl.HttpsURLConnection;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.Objects;
import java.util.concurrent.ExecutionException;

public class TextListeners extends ListenerAdapter {

    private boolean isCommand (MessageReceivedEvent event) {
        return event.getMessage().getContentStripped().startsWith(Globals.PREFIX);
    }

    private String[] stripCommand (String command) {
        String[] strippedCommand = command.split(" ");
        strippedCommand[0] = strippedCommand[0].substring(1);
        return strippedCommand;
    }

    private boolean runCommand (MessageReceivedEvent event) throws InvocationTargetException, IllegalAccessException {
        String command = event.getMessage().getContentStripped().split(" ")[0].substring(1);
        if (!command.equals("onMessageReceived")) {
            try {
                Method method = TextListeners.class.getMethod(command, MessageReceivedEvent.class);
                method.invoke(this, event);
                return true;
            } catch (NoSuchMethodException e) {
                event.getChannel().sendMessage("Sorry, this command does not exist!").submit();
            }
        }
        return false;
    }

    public void login (MessageReceivedEvent event) {
        String baseURL = "http://eu.battle.net/oauth/authorize?response_type=code";
        String clientID  = "&client_id=" + Globals.CLIENT_ID;
        String redirectURI = "&redirect_uri=" + Globals.LOGIN_REDIRECT_URI;
        String state = "&state=" + event.getAuthor().getId();
        event.getChannel().sendMessage("Please login to battle.net using this link:\n" + baseURL + clientID + redirectURI + state).submit();
    }

    public void loginhelp (MessageReceivedEvent event) {
        event.getChannel().sendMessage("when you login, the bot gets permissions only for 24 hours " +
                "this means that if you want to use the bot 24 hours after the login, you will need to login again").submit();
    }

    public void level (MessageReceivedEvent event) throws TokenOutdatedException, ExecutionException, InterruptedException, OuterApiException {
        Message message = event.getChannel().sendMessage("Please wait, this action takes longer than normal commands").submit().get();
        JSONObject stats = getCompleteStats(event);
        Long level = (Long)stats.get("level") + ((Long)stats.get("prestige") * 100);
        message.editMessage(Long.toString(level)).submit();
    }

    public void rank (MessageReceivedEvent event) throws ExecutionException, InterruptedException, TokenOutdatedException, OuterApiException {
        Message message = event.getChannel().sendMessage("Please wait, this action takes longer than normal commands").submit().get();
        Long sr = (Long)getCompleteStats(event).get("rating");
        String rank = findRank(sr);
        message.editMessage(rank + " : " + sr).submit();
        Role rankRole = null;
        try {
            rankRole = GuildRepository.findRoleByName(event.getGuild(), rank);
            event.getGuild().addRoleToMember(Objects.requireNonNull(event.getMember()), rankRole);
            if (event.getMember().getRoles().stream().filter(role -> rank.equals(role.getName())).findAny().orElse(null) == null){
                event.getChannel().sendMessage("It seems that the bot could not manage to apply the role" +
                        "\nplease contact the developer and report this problem.\n" +
                        "in the meantime ask staff members to apply the roles").submit();
            }
        } catch (RepositorySearchEmpty repositorySearchEmpty) {
            event.getChannel().sendMessage("Could not find the corresponding role, please contact the dev").submit();
        }
    }

    private JSONObject getCompleteStats (MessageReceivedEvent event) throws TokenOutdatedException, OuterApiException {
        UserRepository userRepository = new UserRepository();
        String url = "https://ow-api.com/v1/stats/pc/eu/"+ userRepository.getBattleTag(userRepository.findUserByDiscordUserID(event.getAuthor().getId())) +"/complete";
        url = url.replace('#','-');
        try {
            URL urlObj = new URL(url);
            HttpsURLConnection connection = (HttpsURLConnection) urlObj.openConnection();
            connection.setRequestMethod("GET");
            connection.setDoOutput(true);

            if (connection.getResponseCode()==200) {

                JSONParser parser = new JSONParser();
                BufferedReader in = new BufferedReader(
                        new InputStreamReader(connection.getInputStream()));
                String inputLine;
                StringBuilder response = new StringBuilder();

                while ((inputLine = in.readLine()) != null) {
                    response.append(inputLine);
                }
                in.close();
                return (JSONObject) parser.parse(response.toString());
            } else {
                event.getChannel().sendMessage("It seems like the services the bot is using are down, please let the dev know").submit();
            }
        } catch (MalformedURLException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (ParseException e) {
            e.printStackTrace();
        }
        throw new OuterApiException();
    }

    private String findRank(Long sr) {
        if (0<sr && sr<1500) return "Bronze";
        else if (1500<=sr && sr<2000) return "Silver";
        else if (2000<=sr && sr<2500) return "Gold";
        else if (2500<=sr && sr<3000) return "Platinum";
        else if (3000<=sr && sr<3500) return "Diamond";
        else if (3500<=sr && sr<4000) return "Master";
        else if (4000<=sr) return "Grandmaster";
        else return "Unranked";
    }

    @Override
    public void onMessageReceived(@NotNull MessageReceivedEvent event) {
        if (isCommand(event)) {
            try {
                if (!runCommand(event)) {
                    event.getChannel().sendMessage("No such command");
                }
            } catch (InvocationTargetException e) {
                if (e.getTargetException().getClass().equals(TokenOutdatedException.class)){
                    event.getChannel().sendMessage("The battle.net permission have been outdated, please use the ^login " +
                                                        "command and log in once again\nfor more information use ^loginhelp").submit();
                } else if (e.getTargetException().getClass().equals(OuterApiException.class)) {
                    event.getChannel().sendMessage("It seems like the services the bot is using are causing some problems," +
                            "please let the dev know about this").submit();
                } else {
                    e.printStackTrace();
                    event.getChannel().sendMessage(Globals.DEFAULT_ERROR_MESSAGE).submit();
                }
            } catch (IllegalAccessException e) {
                e.printStackTrace();
                event.getChannel().sendMessage(Globals.DEFAULT_ERROR_MESSAGE).submit();
            }
        }
    }
}
