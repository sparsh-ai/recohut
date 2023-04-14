import sys

if __name__ == "__main__":

    output_path = None
    
    print("System arguments are {}".format(sys.argv))

    if len(sys.argv) > 1:
        output_path = sys.argv[1]
        print("Output path is {}".format(output_path))
    else:
        print("S3 output location not specified printing top 10 results to output stream")