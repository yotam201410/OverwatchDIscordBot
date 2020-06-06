package botil.repositores;

import botil.exceptions.TokenOutdatedException;
import botil.Globals;
import botil.models.User;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;

import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
import org.springframework.stereotype.Repository;

import javax.net.ssl.HttpsURLConnection;
import java.io.*;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.ProtocolException;
import java.net.URL;
import java.util.ArrayList;
import java.util.Iterator;

@Repository
public class UserRepository {
    private ArrayList<User> repository;

    public UserRepository() {
        repository = new ArrayList<>();
        JSONParser parser = new JSONParser();
        try (FileReader reader = new FileReader(Globals.USERS_REPOSITORY_PATH)){
            Object obj = parser.parse(reader);
            JSONArray jsonArray = (JSONArray) obj;
            Iterator<JSONObject> iterator = jsonArray.listIterator();
            while (iterator.hasNext()) {
                repository.add(parseJsonToUser(iterator.next()));
            }
        } catch (ParseException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public boolean checkToken(User user) throws TokenOutdatedException {
        String url = "http://eu.battle.net/oauth/check_token?token=" + user.getBattleNetToken();
        try {
            URL urlObj = new URL(url);
            HttpURLConnection connection = (HttpURLConnection) urlObj.openConnection();
            connection.setRequestMethod("GET");
            connection.setDoOutput(true);
            if (connection.getResponseCode()==200){
                return true;
            } else {
                throw new TokenOutdatedException();
            }
        } catch (ProtocolException e) {
            e.printStackTrace();
        } catch (MalformedURLException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        throw new TokenOutdatedException();
    }

    public String getBattleTag (User user) {

        String url = "https://eu.battle.net/oauth/userinfo";
        try {
            URL urlObj = new URL(url);
            HttpsURLConnection connection = (HttpsURLConnection) urlObj.openConnection();
            connection.setRequestMethod("GET");
            connection.setRequestProperty("Authorization", "Bearer " + user.getBattleNetToken());
            connection.setDoOutput(true);

            if (connection.getResponseCode()==200) {
                return parseBattleTagFromResponse(processResponse(connection.getInputStream()));
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

    public String getBattleNetToken(String battleNetCode) {
        String url = "http://eu.battle.net/oauth/token?grant_type=authorization_code&code=" + battleNetCode + "&redirect_uri=" + Globals.LOGIN_REDIRECT_URI;
        try {
            URL urlObj = new URL(url);
            HttpURLConnection connection = (HttpURLConnection) urlObj.openConnection();
            connection.setRequestMethod("POST");
            connection.setRequestProperty("authorization", "Basic NDI2YzQwY2RiYjcwNDU2NWFlYjE5YTU5ZGE2NzExZmM6aHZTb3JQQVo5MzNJR0gwUW9FTE11Vk1Qb2loOE9UajQ=");
            connection.setDoOutput(true);

            if (connection.getResponseCode()==200) {
                return parseAccessTokenFromResponse(processResponse(connection.getInputStream()));
            }
        } catch (MalformedURLException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

    public User findUserByDiscordUserID (String discordUserID) {
        for (User user : repository) {
            if (user.getDiscordUserID().equals(discordUserID)) {
                return user;
            }
        }
        return null;
    }

    public User findUserByBattleNetCode (String battleNetCode) {
        for (User user : repository) {
            if (user.getBattleNetCode().equals(battleNetCode)) {
                return user;
            }
        }
        return null;
    }

    public void deleteUser (User user) {
        repository.remove(user);
        save();
    }

    public void addUser (User user) {
        User oldUser = findUserByDiscordUserID(user.getDiscordUserID());
        if (oldUser != null) {
            repository.remove(oldUser);
        }
        repository.add(user);
        save();
    }

    private String processResponse(InputStream inputStream) throws IOException {
        BufferedReader in = new BufferedReader(
                new InputStreamReader(inputStream));
        String inputLine;
        StringBuilder response = new StringBuilder();

        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine);
        }
        in.close();
        return response.toString();
    }

    private User parseJsonToUser(JSONObject jsonObject) {
        return new User((String) jsonObject.get("discordUserID"),(String) jsonObject.get("battleNetCode"),(String) jsonObject.get("battleNetToken"));
    }

    private void save() {
        JSONArray jsonArray = new JSONArray();
        for (User user : repository) {
            jsonArray.add(parseUserToJson(user));
        }
        try (FileWriter fileWriter = new FileWriter(Globals.USERS_REPOSITORY_PATH);
             PrintWriter printWriter = new PrintWriter(fileWriter)){
            printWriter.print("");
            fileWriter.write(jsonArray.toJSONString());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private String parseAccessTokenFromResponse (String response) {
        JSONParser parser = new JSONParser();
        try {
            Object obj = parser.parse(response);
            JSONObject jsonObject = (JSONObject) obj;
            return (String) jsonObject.get("access_token");
        } catch (ParseException e) {
            e.printStackTrace();
        }
        return null;
    }

    private String parseBattleTagFromResponse (String response) {

        JSONParser parser = new JSONParser();
        try {
            Object obj = parser.parse(response);
            JSONObject jsonObject = (JSONObject) obj;
            return (String) jsonObject.get("battletag");
        } catch (ParseException e) {
            e.printStackTrace();
        }
        return null;
    }

    private JSONObject parseUserToJson (User user) {
        JSONObject jsonObject = new JSONObject();
        jsonObject.put("discordUserID", user.getDiscordUserID());
        jsonObject.put("battleNetCode", user.getBattleNetCode());
        jsonObject.put("battleNetToken", user.getBattleNetToken());
        jsonObject.put("battleTag", getBattleTag(user));
        return jsonObject;
    }
}
