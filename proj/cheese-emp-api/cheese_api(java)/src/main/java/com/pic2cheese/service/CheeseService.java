package com.pic2cheese.service;

import com.pic2cheese.api.Cheese;
import com.pic2cheese.repository.CheeseRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class CheeseService {

    private final CheeseRepository cheeseRepository;

    public Long register(Cheese cheese) {

        Cheese cheeseEntity = new Cheese();

        cheeseEntity.setTaste(cheese.getTaste());
        cheeseEntity.setCountry(cheese.getCountry());
        cheeseEntity.setContent(cheese.getContent());
        cheeseEntity.setStockQuantity(cheese.getStockQuantity());
        cheeseEntity.setPrice(cheese.getPrice());
        cheeseEntity.setName(cheese.getName());
        cheeseEntity.setMatching(cheese.getMatching());
        cheeseEntity.setSubcategory(cheese.getSubcategory());
        cheeseEntity.setTexture(cheese.getTexture());
        cheeseEntity.setTypes(cheese.getTypes());

        cheeseRepository.save(cheeseEntity);

        return cheeseEntity.getId();

    }

    public List<Cheese> list() {
        return cheeseRepository.findAll();
    }

    public Cheese findOne(Long cheeseId) {
        return cheeseRepository.findOne(cheeseId);
    }

    public void remove(Long cheeseNo) throws Exception {
        cheeseRepository.deleteById(cheeseNo);
    }

    public void modify(Cheese cheese) throws Exception {

        Cheese cheeseEntity = new Cheese();

        cheeseEntity.setTaste(cheese.getTaste());
        cheeseEntity.setCountry(cheese.getCountry());
        cheeseEntity.setContent(cheese.getContent());
        cheeseEntity.setStockQuantity(cheese.getStockQuantity());
        cheeseEntity.setPrice(cheese.getPrice());
        cheeseEntity.setName(cheese.getName());
        cheeseEntity.setMatching(cheese.getMatching());
        cheeseEntity.setSubcategory(cheese.getSubcategory());
        cheeseEntity.setTexture(cheese.getTexture());
        cheeseEntity.setTypes(cheese.getTypes());


    }

}
