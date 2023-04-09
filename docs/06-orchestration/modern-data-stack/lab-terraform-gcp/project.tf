resource "google_project" "data_project" {
  billing_account = var.billing_id
  name            = var.project_id
  project_id      = var.project_id
  skip_delete     = false
}
