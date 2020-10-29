package com.pic2cheese.controller;

import com.pic2cheese.api.Subscription;
import com.pic2cheese.service.SubscriptionService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequiredArgsConstructor
public class SubscriptionController {

    private final SubscriptionService subscriptionService;

    @GetMapping("/subscription/list")
    public ResponseEntity<List<Subscription>> list() throws Exception {

        return new ResponseEntity<>(subscriptionService.list(), HttpStatus.OK);

    }


    @GetMapping("/subscription/{subscriptionNo}")
    public ResponseEntity<Subscription> read(@PathVariable("subscriptionNo") Long subscriptionNo) throws Exception {
        Subscription subscription = subscriptionService.findOne(subscriptionNo);

        return new ResponseEntity<>(subscription, HttpStatus.OK);
    }



}
