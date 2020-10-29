package com.pic2cheese.repository;

import com.pic2cheese.api.User;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Repository;

import javax.persistence.EntityManager;
import java.util.List;

@Repository
@RequiredArgsConstructor
public class UserRepository {

    private final EntityManager em;

    public void save(User user) {
        em.persist(user);
    }

    public User findOne(Long id) {
        return em.find(User.class, id);
    }

    public List<User> findAll() {
        return em.createQuery("select u from User u", User.class).getResultList();
    }

    public List<User> finById(Long userNo) {
        return em.createQuery("select u from User u where u.id= :userNo", User.class).getResultList();
    }

    public void deleteById(Long userNo) {
        em.createQuery("delete from User u where u.id = :userNo", User.class);
    }
}
