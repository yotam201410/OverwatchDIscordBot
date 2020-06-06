package botil.services;

import botil.models.User;
import botil.repositores.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class UserService {

    @Autowired
    UserRepository userRepository;

    public User findUserByDiscordUserLongID (String discordUserID) {
        return userRepository.findUserByDiscordUserID(discordUserID);
    }

    public User findUserByBattleNetCode (String battleNetCode) {
        return userRepository.findUserByBattleNetCode(battleNetCode);
    }

    public void deleteUser (User user) {
        userRepository.deleteUser(user);
    }

    public void addUser (User user) {
        userRepository.addUser(user);
    }

    public String getBattleNetToken(String battleNetCode) {
        return userRepository.getBattleNetToken(battleNetCode);
    }

}
