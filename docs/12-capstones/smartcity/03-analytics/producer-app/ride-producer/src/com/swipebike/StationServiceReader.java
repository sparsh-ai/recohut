package com.swipebike;

import com.swipebike.dto.Behavior;
import com.swipebike.dto.InTransitDTO;
import com.swipebike.dto.Station;
import org.apache.log4j.Logger;

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;

public class StationServiceReader {
    private final static String  FILE_NAME = "stations.csv";
    private static final Logger logger = Logger.getLogger(StationServiceReader.class);
    public static List<Station> loadStations(InTransitDTO transitPool)
    {
        logger.info("Start of loadStations.");
        List<Station> stationList = new ArrayList<Station>();  ;
        BufferedReader br = null;
        try {
            logger.info("getResourceAsStream : " + FILE_NAME);
            InputStream is = getFileFromResourceAsStream(FILE_NAME);
            InputStreamReader streamReader = new InputStreamReader(is, StandardCharsets.UTF_8);
            BufferedReader reader = new BufferedReader(streamReader);
            String line;
            while ((line = reader.readLine()) != null) {
                String[] columns = line.split(",");
                if(columns[0].trim().contains("stationId")) continue;
                int iStationId = Integer.parseInt(columns[0].trim());
                int iCapacity = Integer.parseInt(columns[1].trim());
                int iInitCount = Integer.parseInt(columns[2].trim());

                Station aStation = new Station(iStationId, iCapacity, iInitCount, Behavior.valueOf(columns[3]));
                aStation.setTransitPool(transitPool);
                stationList.add(aStation);
                logger.info(aStation);
            }
        } catch (IOException e) {
                e.printStackTrace();
        }


        return stationList;
    }

    private static InputStream getFileFromResourceAsStream(String fileName) {

        // The class loader that loaded the class
        ClassLoader classLoader = StationServiceReader.class.getClassLoader();
        InputStream inputStream = classLoader.getResourceAsStream(fileName);

        // the stream holding the file content
        if (inputStream == null) {
            throw new IllegalArgumentException("file not found! " + fileName);
        } else {
            return inputStream;
        }

    }

}
