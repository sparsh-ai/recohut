terraform {
  backend "local" {}
  required_providers {
    google = {
      source = "hashicorp/google"
    }
  }
}

provider "google" {
  project = var.GCP_PROJECT
  region  = var.GCP_REGION
  zone    = var.GCP_ZONE
}


## Create the Firewall Rule to open the port
resource "google_compute_firewall" "firewall_port_rules" {
    project     = var.GCP_PROJECT
    name        = "kafkaportvm"
    network     = var.NETWORK
    description = "Opens port 9092 in the Kafka VM for Spark cluster to connect"
    direction   = "INGRESS"
    priority    = 1

    allow {
        protocol = "tcp"
        ports    = ["9092"]
    }

    source_ranges = ["0.0.0.0/0"]
    target_tags   = ["kafkavm"]
}

## Create Storage Buckets for Comments
resource "google_storage_bucket" "comments_bucket" {
  name          = "kafka-reddit-comments-stream"
  location      = var.GCP_REGION
  force_destroy = false
  storage_class = "STANDARD"
}

## Create Storage Buckets for Submissions
resource "google_storage_bucket" "submissions_bucket" {
  name          = "kafka-reddit-submissions-stream"
  location      = var.GCP_REGION
  force_destroy = false
  storage_class = "STANDARD"
}

## Create Storage Buckets for Spark Cluster
resource "google_storage_bucket" "spark_cluster_bucket" {
  name          = "sparkclusterbucket"
  location      = var.GCP_REGION
  force_destroy = false
  storage_class = "STANDARD"
}

## Create the Kafka VM
resource "google_compute_instance" "kafka_vm" {
    name         = "kafkavm"
    machine_type = "e2-medium"
    tags         = ["kafkavm"]
    
    boot_disk {
        initialize_params {
            image = "debian-cloud/debian-11"
            size  = 100
        }
    }

    network_interface {
        ## A default network is created for all GCP projects
        network = "default"
        access_config {
            ## Include this section to give the VM an external IP address
        }
    }
}

## Create Dataproc Cluster for PySpark
resource "google_dataproc_cluster" "spark_cluster" {
    name   = "sparkclustervm"
    region = var.GCP_REGION
    
    cluster_config {
        staging_bucket = "sparkclusterbucket"
    
        gce_cluster_config {
            network = var.NETWORK
            zone    = var.GCP_ZONE
        }

        master_config {
            num_instances = 1
            machine_type  = "e2-standard-2"
            disk_config {
                boot_disk_type    = "pd-standard"
                boot_disk_size_gb = 100
            }
        }

        software_config {
            image_version = "2.0-debian10"
            override_properties = {
                "dataproc:dataproc.allow.zero.workers" = "true"
            }
            optional_components = ["JUPYTER"]
        }
    }
}


## Create Bigquery Dataset
resource "google_bigquery_dataset" "bq_dataset_reddit" {
  dataset_id                 = "fedex_reddit_dataset"
  project                    = var.GCP_PROJECT
  location                   = var.GCP_REGION
  delete_contents_on_destroy = false
}


