import numpy as np

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

# defining custom arguments
class MyOptions(PipelineOptions):    
  @classmethod
  def _add_argparse_args(cls, parser):
    parser.add_argument('--input',
                        help='Input for the pipeline',
                        default='./data/')
    parser.add_argument('--output',
                        help='Output for the pipeline',
                        default='./output/')

# class to split a csv line by elements and keep only the columns we are interested in 
class Split(beam.DoFn):
    def process(self, element):
        Date,Open,High,Low,Close,Volume = element.split(",")
        return [{
            'Date': Date,
            'Open': float(Open),
            'Close': float(Close)
        }]
        
class CollectOpen(beam.DoFn):
    def process(self, element):
        # Returns a list of tuples containing the 1 key and Open value
        result = [(1, element['Open'])]
        return result

class CollectClose(beam.DoFn):
    def process(self, element):
        # Returns a list of tuples containing the 1 key and Close value
        result = [(1, element['Close'])]
        return result

# class to calculate the standard deviation over an entire PCollection
class Standard_deviation(beam.DoFn):
    def create_accumulator(self):
        return (0.0, 0.0, 0) # x, x^2, count

    def add_input(self, sum_count, input):
        (sum, sumsq, count) = sum_count
        return sum + input, sumsq + input*input, count + 1

    def merge_accumulators(self, accumulators):
        sums, sumsqs, counts = zip(*accumulators)
        return sum(sums), sum(sumsqs), sum(counts)

    def extract_output(self, sum_count):
        (sum, sumsq, count) = sum_count
        if count:
            mean = sum / count
            variance = (sumsq / count) - mean*mean
            stddev = np.sqrt(variance) if variance > 0 else 0
            return {
                'mean': mean,
                'variance': variance,
                'stddev': stddev,
                'count': count
            }
        else:
            return {
                'mean': float('NaN'),
                'variance': float('NaN'),
                'stddev': float('NaN'),
                'count': 0
            }

# setting input and output files
input_filename = "./data/sp500.csv"
output_filename = "./output/result.txt"

# instantiate the pipeline
options = PipelineOptions()

with beam.Pipeline(options=options) as p:
    # reading the csv and splitting lines by elements we want to retain
    csv_lines = (
            p | beam.io.ReadFromText(input_filename, skip_header_lines=1) |
            beam.ParDo(Split())
        )

    # calculate the mean for Open values
    mean_open = (
        csv_lines | beam.ParDo(CollectOpen()) |
        "Grouping keys Open" >> beam.GroupByKey() |
        "Calculating mean for Open" >> beam.CombineValues(
            beam.combiners.MeanCombineFn()
            )
        )

    # calculate the mean for Close values
    mean_close = (
        csv_lines | beam.ParDo(CollectClose()) |
        "Grouping keys Close" >> beam.GroupByKey() |
        "Calculating mean for Close" >> beam.CombineValues(
            beam.combiners.MeanCombineFn()
            )
        )

    # writing results to file
    output= ( 
        { 
            'Mean Open': mean_open,
            'Mean Close': mean_close 
        } | 
        beam.CoGroupByKey() | 
        beam.io.WriteToText(output_filename)
    )
