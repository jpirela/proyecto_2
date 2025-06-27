package com.todolist.Manudev01.urbe.User.Controller;


import org.springframework.web.bind.annotation.*;

import com.todolist.Manudev01.urbe.User.Services.userServices;
import com.todolist.Manudev01.urbe.User.Model.User;

@RestController
@RequestMapping("/user")
public class UserController {

    @PostMapping("/userRegister")
    public String userRegister(@RequestBody User user) {
        userServices userService = new userServices();
        return userService.userRegister(user.getNombre(), user.getApellido(), user.getUsuario(), user.getContrasena());
    }

    @GetMapping("/getUserByUsername/{userId}")
    public String getUserById(@PathVariable int userId) {
        userServices userService = new userServices();
        return userService.getUserById(userId);
    }
}
