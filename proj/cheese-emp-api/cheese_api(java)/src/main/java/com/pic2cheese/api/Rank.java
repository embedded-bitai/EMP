package com.pic2cheese.api;

public enum Rank {

    GOLD(30000),PLATINUM(50000),BLACK(100000);

    private final int PRICE;

    private Rank(int PRICE) {
        this.PRICE = PRICE;
    }

    int fare(){
        return PRICE;
    }
}
