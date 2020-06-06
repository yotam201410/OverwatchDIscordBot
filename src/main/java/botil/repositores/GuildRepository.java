package botil.repositores;

import botil.exceptions.RepositorySearchEmpty;
import net.dv8tion.jda.api.entities.Guild;
import net.dv8tion.jda.api.entities.Role;

public class GuildRepository {

    private GuildRepository() {
        throw new IllegalStateException("Utility class");
    }

    public static Role findRoleByName(Guild guild, String roleName) throws RepositorySearchEmpty {
        Role result = guild.getRoles().stream().filter(role -> roleName.equals(role.getName())).findAny().orElse(null);
        if (result == null) {
            throw new RepositorySearchEmpty();
        } else {
            return result;
        }
    }
}
