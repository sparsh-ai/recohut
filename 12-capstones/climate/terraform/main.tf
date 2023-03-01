terraform {
  required_version = ">= 1.0"
  backend "local" {}  # Can change from "local" to "gcs" (for google) or "s3" (for aws), if you would like to preserve your tf-state online
  required_providers {
    google = {
      source  = "hashicorp/google"
    }
    postgresql = {
      source = "cyrilgdn/postgresql"
      version = "1.15.0"
    }
  }
}

provider "postgresql" {
  host            = "localhost"
  port            = 5432
  database        = "postgres"
  username        = "root"
  password        = "root"
  sslmode         = "disable"
  connect_timeout = 15
}

provider "google" {
  project = var.PROJECT
  region = var.REGION
  // credentials = file(var.credentials)  # Use this if you do not want to set env-var GOOGLE_APPLICATION_CREDENTIALS
}

resource "postgresql_database" "ghcn-d" {
  name = "ghcn-d"
}

resource "postgresql_schema" "ghcn-d" {
  name  = "ghcnd"
  database = "ghcn-d"
}

/*
# Data Lake Bucket
# Ref: https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket
resource "google_storage_bucket" "data-lake-bucket" {
  name          = var.DATA_LAKE_BUCKET # Concatenating DL bucket & Project name for unique naming
  location      = var.REGION

  # Optional, but recommended settings:
  storage_class = var.STORAGE_CLASS
  uniform_bucket_level_access = true

  versioning {
    enabled     = true
  }

  lifecycle_rule {
    action {
      type = "Delete"
    }
    condition {
      age = 90  // days
    }
  }

  force_destroy = true
}

# Data wharehouse
# Ref: https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigquery_dataset
resource "google_bigquery_dataset" "dataset" {
  dataset_id = var.BQ_DATASET
  project    = var.PROJECT
  location   = var.REGION
}

resource "google_bigquery_dataset" "dataset_dbt" {
  dataset_id = var.BQ_DATASET_DBT_DEV
  project    = var.PROJECT
  location   = var.REGION
}

resource "google_bigquery_dataset" "dataset_dbt_prod" {
  dataset_id = var.BQ_DATASET_DBT_PROD
  project    = var.PROJECT
  location   = var.REGION
}
*/
