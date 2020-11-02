package com.pic2cheese.service;

import com.pic2cheese.api.Subscription;
import com.pic2cheese.repository.SubscriptionRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
@Transactional
@RequiredArgsConstructor
public class SubscriptionService {

    private final SubscriptionRepository subscriptionRepository;

    public List<Subscription> list() {
        return subscriptionRepository.findAll();
    }

    public Subscription findOne(Long subscriptionNo) {
        return subscriptionRepository.findOne(subscriptionNo);
    }
}
