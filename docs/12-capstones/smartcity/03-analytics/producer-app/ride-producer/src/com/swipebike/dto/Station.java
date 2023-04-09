package com.swipebike.dto;

import java.util.Random;

import static com.swipebike.dto.Behavior.*;

public class Station implements Runnable{
    private int stationId;
    private int capacity;
    private int initialCount;
    private Behavior behavior;
    Random rd = new Random();
    private Behavior previousBehavior;

    private int threadSleep;

    private InTransitDTO transitPool;
    private int currentCount;

    public InTransitDTO getTransitPool() {
        return transitPool;
    }

    public void setTransitPool(InTransitDTO transitPool) {
        this.transitPool = transitPool;
    }

    public Behavior getBehavior() {
        return behavior;
    }

    public void setBehavior(Behavior behavior) {
        previousBehavior = this.behavior;
        this.behavior = behavior;
    }

    public Station(int stationId, int capacity, int initialCount, Behavior behavior) {
        Random rn = new Random();
        int answer = rn.nextInt(10) + 1;
        this.threadSleep = answer * 1000;
        this.stationId = stationId;
        this.capacity = capacity;
        this.initialCount = initialCount;
        this.behavior = behavior;
        this.currentCount = initialCount;
    }
    public String toString()
    {
        StringBuilder sb = new StringBuilder();
        sb.append("StationID:").append(stationId).append(" | ");
        sb.append("Capacity:").append(capacity).append(" | ");
        sb.append("Initial Count:").append(initialCount).append(" | ");
        sb.append("Behavior:").append(behavior).append(" | ");
        return sb.toString();

    }

    @Override
    public void run() {
        while(true) {
            switch (behavior) {
                case EVEN:
                    if (rd.nextBoolean()) {
                        // when TRUE dock the bike
                        if (currentCount < this.capacity) {
                            transitPool.dockBike(this.stationId);
                            currentCount++;
                        } else
                            this.setBehavior(SEND);
                    } else {
                        // start using bike
                        if (currentCount > 0) {
                            transitPool.startUsingBike(this.stationId);
                            currentCount--;
                        } else
                            this.setBehavior(RECEIVE);
                    }
                    break;
                case RECEIVE:
                    if (capacity > currentCount) {
                        transitPool.dockBike(this.stationId);
                        currentCount++;
                    } else {
                        if (behavior.equals(previousBehavior)) {
                            setBehavior(SEND);
                        } else {
                            setBehavior(EVEN);
                        }
                    }
                    break;
                case SEND:
                    if (currentCount < 0) {
                        transitPool.startUsingBike(this.stationId);
                        currentCount--;
                    } else {
                        if (behavior.equals(previousBehavior)) {
                            setBehavior(RECEIVE);
                        } else {
                            setBehavior(EVEN);
                        }
                    }
                    break;
                default:
                    transitPool.startUsingBike(this.stationId);
                    currentCount--;
                    break;
            }
            try {
                Thread.sleep(this.threadSleep);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
