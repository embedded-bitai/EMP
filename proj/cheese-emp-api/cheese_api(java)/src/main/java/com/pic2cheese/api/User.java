package com.pic2cheese.api;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

@Entity
@Getter
@Setter
@Table(name = "user")
public class User {

    @Id
    @GeneratedValue
    @Column(name = "user_id")
    private Long id;

    @Enumerated(EnumType.STRING)
    private Gender gender;

    private String pw;
    private String nickname;

    private String name;
    private int age;

    private String city;
    private String street;
    private String zipcode;

    private LocalDateTime joinDay;

    @OneToMany(mappedBy = "user")
    private List<UserCheese> userCheeses = new ArrayList<>();

    @OneToMany(mappedBy = "user")
    private List<FnQ> fnQS = new ArrayList<>();

    @OneToMany(mappedBy = "user")
    private List<Recamm> recamms = new ArrayList<>();

    @OneToMany(mappedBy = "user")
    private List<Review> reviews = new ArrayList<>();
}
