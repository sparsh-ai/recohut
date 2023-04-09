package com.swipebike;

import com.swipebike.dto.InTransitDTO;
import com.swipebike.dto.Station;
import org.apache.log4j.Logger;

import java.util.Iterator;
import java.util.List;
import java.util.concurrent.Executors;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.atomic.AtomicInteger;

public class KDABikeProducer {
    private static final Logger logger = Logger.getLogger(KDABikeProducer.class);
    private static InTransitDTO transitPool = new InTransitDTO();


    public static void main(String[] args) {
	    // write your code here
        logger.info("Start of setUp");
        List<Station> listOfStations = StationServiceReader.loadStations(transitPool);

        ThreadPoolExecutor executor = (ThreadPoolExecutor) Executors.newFixedThreadPool(listOfStations.size());

        Iterator<Station> stationIterator = listOfStations.iterator();
        while (stationIterator.hasNext()) {
            Station aStation = stationIterator.next();
            executor.execute(aStation);
        }
        executor.shutdown();
    }

}
