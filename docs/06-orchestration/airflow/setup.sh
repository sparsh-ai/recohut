airflow db init
airflow users create \
    --username admin \
    --password admin \
    --firstname Sparsh \
    --lastname Agarwal \
    --role Admin \
    --email sparsh@example.com

export AIRFLOW_HOME=$(pwd)
export AIRFLOW__CORE__LOAD_EXAMPLES=False
export AIRFLOW__CORE__ENABLE_XCOM_PICKLING=True

export AIRFLOW__EMAIL__BACKEND=airflow.providers.amazon.aws.utils.emailer.send_email
export AIRFLOW__EMAIL__CONN_ID=aws_default
export AIRFLOW__EMAIL__DEFAULT_EMAIL_ON_RETRY=True
export AIRFLOW__EMAIL__DEFAULT_EMAIL_ON_FAILURE=True
export AIRFLOW__EMAIL__FROM_EMAIL="Airflow <sprsag@gmail.com>"

airflow standalone

airflow variables set 's3_redshift_iam_role' 'arn:aws:iam::684199068947:role/service-role/AmazonRedshift-CommandsAccessRole-20220921T223853'
airflow variables set 's3_redshift_region' 'us-east-1'
airflow variables set 's3_movies_source_url' 'https://hudsonmendes-datalake.s3.eu-west-2.amazonaws.com/kaggle/hudsonmendes/tmdb-movies-with-imdb_id.zip'
airflow variables set 's3_movie_reviews_source_url' 'https://hudsonmendes-datalake.s3.eu-west-2.amazonaws.com/kaggle/hudsonmendes/tmdb-reviews.zip'
airflow variables set 'http_cast_source_url' 'https://datasets.imdbws.com/title.principals.tsv.gz'
airflow variables set 'http_cast_names_source_url' 'https://datasets.imdbws.com/name.basics.tsv.gz'
airflow variables set 's3_staging_bucket' 'wysde2'
airflow variables set 's3_staging_movies_folder' 'tmdb-movies-with-imdb_id'
airflow variables set 's3_staging_movie_reviews_folder' 'tmdb-reviews'
airflow variables set 's3_staging_cast_path' 'imdb-cast/imdb-cast.tsv.gz'
airflow variables set 's3_staging_cast_names_path' 'imdb-cast/imdb-cast-names.tsv.gz'
airflow variables set 'redshift_db' 'dev'
airflow variables set 'path_images_dir' '/tmp/images'
airflow variables set 'path_working_dir' '/tmp/working'
airflow variables set 's3_report_bucket' 'wysde2'
airflow variables set 's3_report_folder' 'reports-sentiment'
airflow variables set 'model_max_length' '30'
airflow variables set 'model_output_path' '/tmp/models'