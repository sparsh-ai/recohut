package com.swipebike.dto;

import java.util.UUID;
import java.util.Random;

public class Bike {
    private UUID bikeNum = UUID.randomUUID();
    private String bikeType = (new Random().nextBoolean()? "BASIC":"ADVANCED");

    public UUID getBikeNum() {
        return bikeNum;
    }

    public void setBikeNum(UUID bikeNum) {
        this.bikeNum = bikeNum;
    }

    public String getBikeType() {
        return bikeType;
    }

    public void setBikeType(String bikeType) {
        this.bikeType = bikeType;
    }
}
