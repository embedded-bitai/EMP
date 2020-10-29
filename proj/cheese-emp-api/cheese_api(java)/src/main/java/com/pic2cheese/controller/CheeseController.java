package com.pic2cheese.controller;

import com.pic2cheese.api.Cheese;
import com.pic2cheese.service.CheeseService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequiredArgsConstructor
public class CheeseController {

    private final CheeseService cheeseService;

    @PostMapping("/cheese/new")
    public ResponseEntity<Cheese> create(@Validated Cheese cheese) throws Exception {

        cheeseService.register(cheese);

        return new ResponseEntity<>(cheese, HttpStatus.OK);
    }

    @GetMapping("/cheese/{cheeseNo}")
    public ResponseEntity<Cheese> read(@PathVariable("cheeseNo") Long cheeseNo) {
        Cheese cheese = cheeseService.findOne(cheeseNo);

        return new ResponseEntity<>(cheese, HttpStatus.OK);
    }

    @GetMapping("/cheese/list")
    public ResponseEntity<List<Cheese>> list() throws Exception {
        return new ResponseEntity<>(cheeseService.list(), HttpStatus.OK);
    }

    @DeleteMapping("/cheese/{cheeseNo}")
    public ResponseEntity<Void> remove(@PathVariable("cheeseNo") Long cheeseNo) throws Exception {
        cheeseService.remove(cheeseNo);

        return new ResponseEntity<>(HttpStatus.NO_CONTENT);
    }

    @PutMapping("/cheese/{cheeseNo}")
    public ResponseEntity<Cheese> modify(@PathVariable("cheeseNO") Long cheeseNo,
                                         @Validated Cheese cheese) throws Exception {
        cheese.setId(cheeseNo);
        cheeseService.modify(cheese);

        return new ResponseEntity<>(cheese, HttpStatus.OK);
    }
}
