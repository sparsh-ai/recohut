## NO DEFAULT in GCP_PROJECT, Required argument at runtime
variable "GCP_PROJECT" {
  description = "Your GCP Project ID"
  type        = string
}

variable "GCP_REGION" {
  description = "Your project region"
  default     = "us-central1"
  type        = string
}

variable "GCP_ZONE" {
  description = "Your project zone"
  default     = "us-central1-c"
  type        = string
}

variable "NETWORK" {
  description = "Network for your instance/cluster"
  default     = "default"
  type        = string
}