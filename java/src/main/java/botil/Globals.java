package botil;

import net.dv8tion.jda.api.JDA;

public class Globals {

    private Globals() {
        throw new IllegalStateException("Utility class");
    }

    public static final String VERSION = "Dev Release 0.0.1";
    public static final String PREFIX = "^";
    static JDA jda;
    public static final String LOGIN_REDIRECT_URI = "http://localhost:8080/login";
    public static final String CLIENT_ID = "426c40cdbb704565aeb19a59da6711fc";
    public static final String TOKEN = "NjMwNDA4Njc3Mjk1MTI4NTk2.XaOIWg._D25SLMU9CIGFM9jO5mSJumLL74";
    public static final String DEFAULT_ERROR_MESSAGE = "Encountered an error while running the command, please contact the devs and report this issue";
    public static final String USERS_REPOSITORY_PATH = "Repositories/users.json";
}
