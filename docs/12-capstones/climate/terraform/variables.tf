variable "DATA_LAKE_BUCKET" {
  description = "Name of the data lake in GCS where to store the raw files"
  type = string
}

variable "PROJECT" {
  description = "Global Historical Climatology Network Daily Data Engineering"
}

variable "REGION" {
  description = "Region for GCP resources. Choose as per your location: https://cloud.google.com/about/locations"
  type = string
}

variable "STORAGE_CLASS" {
  description = "Storage class type for your bucket. Check official docs for more info."
  default = "STANDARD"
}

variable "BQ_DATASET" {
  description = "BigQuery Dataset that raw data (from GCS) will be written to"
  type = string
}

variable "BQ_DATASET_DBT_DEV" {
  description = "BigQuery Dataset that dbt will use for during development"
  type = string
}

variable "BQ_DATASET_DBT_PROD" {
  description = "BigQuery Dataset that dbt will use for during development"
  type = string
  default = "production"
}
