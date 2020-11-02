package com.pic2cheese.controller;

import com.pic2cheese.api.User;
import com.pic2cheese.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequiredArgsConstructor
public class UserController {

    private final UserService userService;

    @PostMapping("/users/new")
    public ResponseEntity<User> create(@Validated User user) throws Exception {

        userService.join(user);

        return new ResponseEntity<>(user, HttpStatus.OK);
    }

    @GetMapping("/users/{userNo}")
    public ResponseEntity<User> read(@PathVariable("userNo") Long userNo) throws Exception{
        User user = userService.findOne(userNo);

        return new ResponseEntity<>(user, HttpStatus.OK);
    }

    @GetMapping("/users/list")
    public ResponseEntity<List<User>> list() throws Exception {
        return new ResponseEntity<>(userService.list(), HttpStatus.OK);
    }

    @DeleteMapping("/users/{userNo}")
    public ResponseEntity<Void> remove(@PathVariable("userNo") Long userNo) throws Exception {
        userService.remove(userNo);

        return new ResponseEntity<>(HttpStatus.NO_CONTENT);
    }

    @PutMapping("/users/{userNo}")
    public ResponseEntity<User> modify(@PathVariable("userNo") Long userNo,
                                       @Validated User user) throws Exception {
        user.setId(userNo);
        userService.modify(user);

        return new ResponseEntity<>(user, HttpStatus.OK);
    }


}
