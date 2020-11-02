package com.pic2cheese.repository;

import com.pic2cheese.api.Subscription;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Repository;

import javax.persistence.EntityManager;
import java.util.List;

@Repository
@RequiredArgsConstructor
public class SubscriptionRepository {

    private final EntityManager em;

    public Subscription findOne(Long id) {
        return em.find(Subscription.class, id);
    }

    public List<Subscription> findAll() {
        return em.createQuery("select s from Subscription s", Subscription.class).getResultList();
    }


}
