package com.swipebike.dto;


import software.amazon.awssdk.services.kinesis.model.DescribeStreamRequest;
import software.amazon.awssdk.services.kinesis.model.DescribeStreamResponse;
import software.amazon.awssdk.services.kinesis.model.PutRecordRequest;
import software.amazon.awssdk.services.kinesis.KinesisAsyncClient;
import software.amazon.kinesis.common.KinesisClientUtil;
import software.amazon.awssdk.core.SdkBytes;
import software.amazon.awssdk.regions.Region;
import com.swipebike.StationServiceReader;
import netscape.javascript.JSObject;
import org.apache.log4j.Logger;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.UnsupportedEncodingException;
import java.nio.ByteBuffer;
import java.text.DateFormat;
import java.text.DecimalFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Random;
import java.util.TimeZone;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.atomic.AtomicInteger;

public class InTransitDTO {
    private static AtomicInteger inTransitCounter = new AtomicInteger(100);
    private static final Logger logger = Logger.getLogger(InTransitDTO.class);
    private TimeZone tz = TimeZone.getTimeZone("UTC");
    private DateFormat df = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss.SSS"); // Quoted "Z" to indicate UTC, no timezone offset
    private Random rn = new Random();
    private int low = 120;
    private int high = 3600;
    DecimalFormat decFormat = new DecimalFormat("#.##");
    private static String kinesisStream = System.getenv().getOrDefault("KINESIS_STREAM", "defaultStreamName");
    private static String regionName = System.getenv().getOrDefault("AWS_REGION", "us-east-1");

    Region region = Region.of(regionName);
    KinesisAsyncClient kinesisClient = KinesisClientUtil.createKinesisAsyncClient(KinesisAsyncClient.builder().region(region));

    {
        df.setTimeZone(tz);
    }

    public void dockBike(int stationId) {
        int tripDuration = rn.nextInt(high - low) + low;
        BikeRide bikeRide = new BikeRide(stationId, "DOCKED", tripDuration, Double.parseDouble(decFormat.format(tripDuration / 60.0)) );
        sendToKinesis(bikeRide);
    }

    public void startUsingBike(int stationId) {
        BikeRide bikeRide = new BikeRide(stationId, "RENTED", 0, 0.00 );
        sendToKinesis(bikeRide);

    }

    private void sendToKinesis(BikeRide br) {


        // Validate that the stream exists and is active
        //validateStream(kinesisClient, kinesisStream);

        byte[] bytes = br.toJsonAsBytes();


        logger.info("Putting Ride: " + br.toString());
        PutRecordRequest request = PutRecordRequest.builder()
                .partitionKey(String.valueOf(br.getStationId())) // We use the ticker symbol as the partition key, explained in the Supplemental Information section below.
                .streamName(kinesisStream)
                .data(SdkBytes.fromByteArray(bytes))
                .build();
        try {
            kinesisClient.putRecord(request).get();
        } catch (InterruptedException e) {
            logger.info("Interrupted, assuming shutdown.");
        } catch (ExecutionException e) {
            logger.error("Exception while sending data to Kinesis. Will try again next cycle.", e);
        }


    }

    private static void validateStream(KinesisAsyncClient kinesisClient, String streamName) {
        try {
            DescribeStreamRequest describeStreamRequest =  DescribeStreamRequest.builder().streamName(streamName).build();
            DescribeStreamResponse describeStreamResponse = kinesisClient.describeStream(describeStreamRequest).get();
            if(!describeStreamResponse.streamDescription().streamStatus().toString().equals("ACTIVE")) {
                System.err.println("Stream " + streamName + " is not active. Please wait a few moments and try again.");
                System.exit(1);
            }
        }catch (Exception e) {
            System.err.println("Error found while describing the stream " + streamName);
            System.err.println(e);
            System.exit(1);
        }
    }
}
