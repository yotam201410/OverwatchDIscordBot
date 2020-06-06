package botil;

import botil.listners.TextListeners;
import net.dv8tion.jda.api.JDABuilder;
import net.dv8tion.jda.api.entities.Activity;
import net.dv8tion.jda.api.hooks.ListenerAdapter;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import javax.security.auth.login.LoginException;

@SpringBootApplication
public class Main extends ListenerAdapter {
    public static void main(String[] args) throws LoginException {
        SpringApplication.run(Main.class, args);
        JDABuilder builder = new JDABuilder(Globals.TOKEN);
        builder.setActivity(Activity.watching("You"));
        Globals.jda = builder.build();
        Globals.jda.addEventListener(new TextListeners());
    }
}
