package com.pic2cheese.api;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.List;

@Entity
@Getter @Setter
public class Analysis {

    @Id @GeneratedValue()
    @Column(name = "analysis_id")
    private Long id;

    @OneToMany(mappedBy = "analysis")
    private List<FnQ> fnQS = new ArrayList<>();

    @OneToMany(mappedBy = "analysis")
    private List<Recamm> recamms = new ArrayList<>();
}
