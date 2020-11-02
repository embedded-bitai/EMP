package com.pic2cheese.api;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;
import java.time.LocalDateTime;

@Entity
@Getter @Setter
@Table(name = "user_cheese")
public class UserCheese {

    @Id
    @GeneratedValue
    @Column(name = "user_cheese_id")
    private Long id;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "cheese_id")
    private Cheese cheese;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "user_id")
    private User user;

    private int orderPrice;
    private int count;

    private LocalDateTime orderTime;
}
