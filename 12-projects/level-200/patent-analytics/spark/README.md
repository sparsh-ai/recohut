# Patents Analytics Spark

This folder contains the pyspark scripts used for cleaning, performing keyword extraction, and doing the ETL job for patents analytics data.

This project follows the recommendations from [pyspark-example-project](https://github.com/AlexIoannides/pyspark-example-project) on how to structure the project, passing configuration parameters to a pyspark job, handling dependencies, and unit testing pyspark scripts. Please refer to the link for more details.

## Project Structure
- `Configs` hosts the config file for the pyspark jobs. The file inside this folder will be submitted to Spark cluster together with the script
- `dependencies` contains commonly used functions shared by the pyspark scripts. These files will be bundled into packages.zip and should be submitted together with the script to Spark cluster.
- `jobs` contains the pyspark scripts to run data cleaning, keyword extraction, and ETL
- `tests` contains the unit test for the pyspark scripts
- `build_dependencies.sh` packages all the dependencies which include all the files from `dependencies` folder and the python libraries specified in the pipfile into `packages.zip`
- `copy_jobs_to_ariflwo.sh` copies all the required files to be submitted to Spark Cluster to airflow folder.
- `packages.zip` is the result of running `build_dependencies.sh`

## Getting Started
### Installing the project dependencies
We are using pipenv to manage the project dependencies. Please follow these steps to set up the required libraries:
- Install `pipenv`
```commandline
pip install pipenv
```
- Install the libraries specified in the pipfile
```commandline
pipenv install
```
- Activate the pipenv environment
```commandline
pipenv shell .
```

### Create the configuration file
- Create a folder named `configs` in the same level as this README.md file, and create a file inside named `etl_config.json`. Put the following value:
```json
{
  "redshift": {
    "username": "<redshift username>",
    "password": "<redshift password>",
    "jdbc_url": "<redshift jdbc url>",
    "s3_temp_dir": "<s3 path to store temp data for writing to redshift>",
    "iam_role": "<iam role to allow redshift to read s3>"
  },
  "cleaned_data_s3_path": "<s3 path to store cleaned data>",
  "raw_data_s3_path": "<s3 path to store raw data>"
}
```

### Bundle the dependencies
Run the following command to package all the script's dependencies:
```commandline
./build_dependencies.sh
```

### Copy spark scripts to airflow
Run the following command to copied all the scripts, dependencies, and configs to airflow folder:
```commandline
./copy_jobs_to_airflow.sh
```

## Unit Testing
Please follow these steps to be able to run unit testing locally in Windows:

**Setup Java**
- Install JDK version 11, this is the version required because we are using spark version 3.1.2
- Set the `JAVA_HOME` environment variable to the JDK path

**Setup Python Path**
- Add the path to the JDK's bin folder to the `PATH`environment variable
- Set the `PYSPARK_DRIVER_PYTHON` environment variable to the python.exe path of the pipenv environment
- Set the `PYSPARK_PYTHON` environment variable to the python.exe path of the pipenv environment

**Hadoop Executable**
- Download `winutils.exe` and `hadoop.dll` from https://github.com/steveloughran/winutils/tree/master/hadoop-3.0.0/bin
- Create a folder in your local directory named `bin`, and place the `winutils.exe` and `hadoop.dll` inside the bin folder
- Create `HADOOP_HOME` environment variable and put the path to the parent folder of the bin folder created above.
- Add the bin folder to the `PATH` environment variable

You can run the unittest using the following command:
```commandline
python -m unittest discover -s tests
```
