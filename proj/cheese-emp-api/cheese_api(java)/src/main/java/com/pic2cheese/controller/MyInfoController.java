package com.pic2cheese.controller;

import com.pic2cheese.api.User;
import com.pic2cheese.api.UserSubscription;
import com.pic2cheese.service.MyInfoService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.util.UriComponentsBuilder;

@RestController
@RequiredArgsConstructor
public class MyInfoController {

    private MyInfoService myInfoService;

    @PutMapping("/myinfo")
    public ResponseEntity<Boolean> register(@Validated UserSubscription userSubscription,
                                            UriComponentsBuilder uriBuilder,
                                            @RequestHeader(name = "Authorization") String header) throws Exception {

        //지연이한테 물어보기
        Long userNo = Long.valueOf(header);

        myInfoService.register(userNo);

        return new ResponseEntity<>(HttpStatus.OK);
    }


}
