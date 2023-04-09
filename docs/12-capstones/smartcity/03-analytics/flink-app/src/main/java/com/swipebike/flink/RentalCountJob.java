package com.swipebike.flink;

import com.amazonaws.services.kinesisanalytics.flink.connectors.producer.FlinkKinesisFirehoseProducer;
import com.amazonaws.services.kinesisanalytics.runtime.KinesisAnalyticsRuntime;
import org.apache.flink.api.common.serialization.SimpleStringSchema;
import org.apache.flink.api.common.typeinfo.TypeHint;
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

import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Map;
import java.util.Properties;
import static java.util.Optional.ofNullable;



public class RentalCountJob {
    private static final ObjectMapper jsonParser = new ObjectMapper();
    private static final String region = "us-east-1";
    private static final String inputStreamName = "ProducerStream";
    private static final String outputDeliveryStreamName = "station_data_kdf";
    public static final SimpleDateFormat DATE_TIME_FORMAT = new SimpleDateFormat("yyyyMMddHHmm");


    private static DataStream<String> createSourceFromStaticConfig(
            StreamExecutionEnvironment env) {

        /*Properties consumerProperties = new Properties();
        consumerProperties.putIfAbsent(ConsumerConfigConstants.STREAM_INITIAL_POSITION, "LATEST");
        consumerProperties.putIfAbsent(ConsumerConfigConstants.AWS_REGION, region);
*/
        Map<String, Properties> applicationProperties = null;
        try {
            applicationProperties = KinesisAnalyticsRuntime.getApplicationProperties();
        } catch (IOException e) {
            e.printStackTrace();
        }

        Properties consumerConfigProperties = ofNullable(applicationProperties.get("ConsumerConfigProperties")).orElseGet(Properties::new);

        consumerConfigProperties.putIfAbsent(ConsumerConfigConstants.STREAM_INITIAL_POSITION, "LATEST");
        consumerConfigProperties.putIfAbsent(ConsumerConfigConstants.AWS_REGION, region);
        consumerConfigProperties.putIfAbsent("INPUT_STREAM", inputStreamName);


        return env.addSource(new FlinkKinesisConsumer<>(
                consumerConfigProperties.getProperty("INPUT_STREAM", inputStreamName),
                    new SimpleStringSchema(), consumerConfigProperties));
    }


    private static FlinkKinesisFirehoseProducer<String> createFirehoseSinkFromStaticConfig() {
        /*
         * com.amazonaws.services.kinesisanalytics.flink.connectors.config.ProducerConfigConstants
         * lists of all of the properties that firehose sink can be configured with.
         */

        /*Properties outputProperties = new Properties();
        outputProperties.putIfAbsent("OUTPUT_KDF", outputDeliveryStreamName);
        outputProperties.putIfAbsent(ConsumerConfigConstants.AWS_REGION, region);
*/
        Map<String, Properties> applicationProperties = null;
        try {
            applicationProperties = KinesisAnalyticsRuntime.getApplicationProperties();
        } catch (IOException e) {
            e.printStackTrace();
        }

        Properties outputConfigProperties = ofNullable(applicationProperties.get("OutputConfigProperties")).orElseGet(Properties::new);

        outputConfigProperties.putIfAbsent(ConsumerConfigConstants.AWS_REGION, region);
        outputConfigProperties.putIfAbsent("OUTPUT_KDF", outputDeliveryStreamName);


        FlinkKinesisFirehoseProducer<String> sink = new FlinkKinesisFirehoseProducer<>(outputDeliveryStreamName, new SimpleStringSchema(), outputConfigProperties);
        return sink;
    }

    public static void main(String[] args) throws Exception {

        final StreamExecutionEnvironment env =
                StreamExecutionEnvironment.getExecutionEnvironment();

        DataStream<String> input = createSourceFromStaticConfig(env);

        SingleOutputStreamOperator<Tuple2<String, Integer>> inputMap = input.map(value -> {
            JsonNode jsonNode = jsonParser.readValue(value, JsonNode.class);
            return new Tuple2<>(jsonNode.get("stationId").asText(), ("DOCKED".equalsIgnoreCase(jsonNode.get("action").asText()) ? 1 : -1) );
        }).returns(Types.TUPLE(Types.STRING, Types.INT));



        //logger.info("Got input map...");
        //inputMap.returns(Types.TUPLE(Types.STRING, Types.INT))
        inputMap.returns(new TypeHint<Tuple2<String, Integer>>(){})
                .keyBy(tuple -> tuple.f0)//.keyBy(0) // Logically partition the stream per stationId
                .timeWindow(Time.minutes(3)) // tumbling window definition
                .sum(1) // Calculate the minimum price over the window
                .map( value -> DATE_TIME_FORMAT.format(new Date()) + ","+ value.f0 + "," + value.f1.toString() + "\n")
                .addSink(createFirehoseSinkFromStaticConfig()); // write to Firehose Delivery Stream

        env.execute("RentalCountJob");

    }

}
