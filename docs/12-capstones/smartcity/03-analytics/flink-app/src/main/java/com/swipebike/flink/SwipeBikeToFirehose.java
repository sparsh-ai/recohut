package com.swipebike.flink;


import com.amazonaws.services.kinesisanalytics.flink.connectors.producer.FlinkKinesisFirehoseProducer;
import com.amazonaws.services.kinesisanalytics.runtime.KinesisAnalyticsRuntime;
import org.apache.flink.api.common.serialization.DeserializationSchema;
import org.apache.flink.api.common.serialization.SimpleStringSchema;
import org.apache.flink.api.common.typeinfo.Types;
import org.apache.flink.api.java.tuple.Tuple2;
import org.apache.flink.shaded.jackson2.com.fasterxml.jackson.databind.JsonNode;
import org.apache.flink.shaded.jackson2.com.fasterxml.jackson.databind.ObjectMapper;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.datastream.SingleOutputStreamOperator;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.streaming.api.windowing.time.Time;
import org.apache.flink.streaming.connectors.kinesis.FlinkKinesisConsumer;
import org.apache.flink.streaming.connectors.kinesis.config.ConsumerConfigConstants;
import org.apache.log4j.Logger;
import software.amazon.kinesis.connectors.flink.serialization.KinesisDeserializationSchemaWrapper;

import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Map;
import java.util.Properties;

import static java.util.Optional.ofNullable;
import static software.amazon.kinesis.connectors.flink.config.AWSConfigConstants.AWS_REGION;
import static software.amazon.kinesis.connectors.flink.config.ConsumerConfigConstants.*;

public class SwipeBikeToFirehose {
    private static final ObjectMapper jsonParser = new ObjectMapper();
    private static final String region = "us-east-1";
    //private static final String inputStreamName = "RideGenerator";
    private static final String outputDeliveryStreamName = "station_data_kdf";

    private static final Logger logger = Logger.getLogger(SwipeBikeToFirehose.class);
    private final StreamExecutionEnvironment env;

    public static final SimpleDateFormat DATE_TIME_FORMAT = new SimpleDateFormat("yyyyMMddHHmm");

    /**
     * Constructor
     * @param env
     */
    public SwipeBikeToFirehose(StreamExecutionEnvironment env) {
        this.env = env;
    }

    /**
     * Initilizes Input Stream for reading
     * @param env
     * @return
     * @throws IOException
     */
    private static DataStream<String> createSourceFromStaticConfig(
            StreamExecutionEnvironment env) throws IOException {

        Map<String, Properties> applicationProperties = KinesisAnalyticsRuntime.getApplicationProperties();

        Properties consumerProperties = ofNullable(applicationProperties.get("ConsumerConfigProperties")).orElseGet(Properties::new);

        consumerProperties.putIfAbsent(RECORD_PUBLISHER_TYPE, "EFO");
        consumerProperties.putIfAbsent(EFO_CONSUMER_NAME, "EFOKDAConsumer");
        consumerProperties.putIfAbsent(STREAM_INITIAL_POSITION, "LATEST");
        consumerProperties.putIfAbsent(AWS_REGION, "us-east-1");


        return env.addSource( new FlinkKinesisConsumer<String>(consumerProperties.getProperty("INPUT_STREAM", "BikeRideGenerator"),
                (DeserializationSchema<String>) new KinesisDeserializationSchemaWrapper<>(new SimpleStringSchema()), consumerProperties));
        //new FlinkKinesisConsumer<>(consumerProperties.getProperty("INPUT_STREAM", "BikeRideGenerator"),
        //                new SimpleStringSchema(), consumerProperties));
    }


    private static FlinkKinesisFirehoseProducer<String> createFirehoseSinkFromStaticConfig() {
        /*
         * com.amazonaws.services.kinesisanalytics.flink.connectors.config.ProducerConfigConstants
         * lists of all of the properties that firehose sink can be configured with.
         */

        Properties outputProperties = new Properties();
        outputProperties.setProperty(ConsumerConfigConstants.AWS_REGION, region);

        FlinkKinesisFirehoseProducer<String> sink = new FlinkKinesisFirehoseProducer<>(outputDeliveryStreamName, new SimpleStringSchema(), outputProperties);
        return sink;
    }

    public static void main(String[] args) throws Exception {

        final StreamExecutionEnvironment env =
                StreamExecutionEnvironment.getExecutionEnvironment();

        SwipeBikeToFirehose toFirehose = new SwipeBikeToFirehose(env);
        toFirehose.start();



    }


    void start() throws Exception {

        //logger.info("Start...");

        DataStream<String> input = createSourceFromStaticConfig(env);

        SingleOutputStreamOperator<Tuple2<String, Integer>> inputMap = input.map(value -> {
            JsonNode jsonNode = jsonParser.readValue(value, JsonNode.class);
            return new Tuple2<>(jsonNode.get("stationId").asText(), ("DOCKED".equalsIgnoreCase(jsonNode.get("action").asText()) ? 1 : -1) );
        }).returns(Types.TUPLE(Types.STRING, Types.INT));

        //logger.info("Got input map...");

        inputMap.returns(Types.TUPLE(Types.STRING, Types.INT))
                .keyBy(0) // Logically partition the stream per stock symbol
                .timeWindow(Time.minutes(3)) // tumbling window definition
                .sum(1) // Calculate the minimum price over the window
                .map( value -> DATE_TIME_FORMAT.format(new Date()) + ","+ value.f0 + "," + value.f1.toString() + "\n")
                .addSink(createFirehoseSinkFromStaticConfig()); // write to Firehose Delivery Stream

        env.execute("Earnings by Bike Fleet");


    }
}

