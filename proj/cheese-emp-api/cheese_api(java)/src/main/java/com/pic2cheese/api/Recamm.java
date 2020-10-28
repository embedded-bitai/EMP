package com.pic2cheese.api;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;

@Entity
@Getter @Setter
public class Recamm {

    @Id @GeneratedValue
    @Column(name = "recamm_id")
    private Long id;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "analysis_id")
    private Analysis analysis;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "cheese_id")
    private Cheese cheese;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "user_id")
    private User user;
}
