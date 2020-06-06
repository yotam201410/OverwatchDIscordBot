package botil.models;

public class User {
    private String discordUserID;
    private String battleNetCode;
    private String battleNetToken;

    public User(String discordUserID, String battleNetCode, String battleNetToken) {
        this.discordUserID = discordUserID;
        this.battleNetCode = battleNetCode;
        this.battleNetToken = battleNetToken;
    }

    public String getDiscordUserID() {
        return discordUserID;
    }

    public void setDiscordUserID(String discordUserID) {
        this.discordUserID = discordUserID;
    }

    public String getBattleNetCode() {
        return battleNetCode;
    }

    public void setBattleNetCode(String battleNetCode) {
        this.battleNetCode = battleNetCode;
    }

    public String getBattleNetToken() {
        return battleNetToken;
    }

    public void setBattleNetToken(String battleNetToken) {
        this.battleNetToken = battleNetToken;
    }
}
