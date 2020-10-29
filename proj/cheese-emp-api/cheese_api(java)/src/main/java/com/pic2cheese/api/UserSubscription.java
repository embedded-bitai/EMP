package com.pic2cheese.api;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;
import java.time.LocalDateTime;

@Entity
@Getter
@Setter
public class UserSubscription {

    @Id @GeneratedValue
    @Column(name = "user_subscription_id")
    private Long id;

    @ManyToOne
    @JoinColumn(name = "user_id")
    private User user;

    @OneToOne
    @JoinColumn(name = "subscription_id")
    private Subscription subscription;

    private LocalDateTime localDateTime;
}
