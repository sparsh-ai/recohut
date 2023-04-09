package com.swipebike.dto;

import java.io.IOException;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.time.ZoneOffset;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Date;
import java.util.TimeZone;

import com.fasterxml.jackson.databind.DeserializationFeature;
import com.fasterxml.jackson.databind.ObjectMapper;

public class BikeRide {
    private final static ObjectMapper JSON = new ObjectMapper();
    static {
        JSON.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
    }

    private int stationId;
    private String action;
    private int  tripDuration;
    private double price;
    private Bike bikeDetail = new Bike();
    private TimeZone eventUTCTime  = TimeZone.getTimeZone("UTC");
    DateFormat df = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss.SSS");


    public String getEventUTCTime() {
        df.setTimeZone(eventUTCTime);
        String nowAsISO = df.format(new Date());
        return nowAsISO;
    }




    public BikeRide(int stationId, String action, int tripDuration, double price) {
        this.stationId = stationId;
        this.action = action;
        this.tripDuration = tripDuration;
        this.price = price;
    }

    public byte[] toJsonAsBytes() {
        try {
            return JSON.writeValueAsBytes(this);
        } catch (IOException e) {
            return null;
        }
    }

    public int getStationId() {
        return stationId;
    }

    public void setStationId(int stationId) {
        this.stationId = stationId;
    }

    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }

    public int getTripDuration() {
        return tripDuration;
    }

    public void setTripDuration(int tripDuration) {
        this.tripDuration = tripDuration;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public Bike getBikeDetail() {
        return bikeDetail;
    }

    public void setBikeDetail(Bike bikeDetail) {
        this.bikeDetail = bikeDetail;
    }

    @Override
    public String toString() {
        return String.format("StationID %d: %s lasted %d sec. and cost $%.02f, occured at %s",
                stationId, action, tripDuration,  price, this.getEventUTCTime());
    }


}
