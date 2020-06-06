package botil.controllers;

import botil.models.User;
import botil.services.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("login")
public class LoginController {

    @Autowired
    UserService userService;

    @GetMapping()
    public void key(@RequestParam String code, @RequestParam String state) {
        System.out.println("Got the code");
        System.out.println(code);
        System.out.println("From");
        System.out.println(state);

        userService.addUser(new User(state, code, userService.getBattleNetToken(code)));
    }
}
