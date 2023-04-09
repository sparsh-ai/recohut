# Ternary

## Prompt

At Ternary, we are eager to find ways to help customers gain visibility into all types of cloud services, especially those they may not be paying attention to. One of the areas that often go neglected and result in high costs is bucket storage – Google Cloud Storage (GCS).

In this assignment, please develop a tool that can collect bucket object storage size data from a particular GCS bucket. The tool should take as input the bucket URI and collect the storage information for each object. Then save the usage information into a data format that can be used to generate a chart / report (e.g. Excel) showing either size per bucket or size per object. You can find storage client examples [here](https://cloud.google.com/storage/docs/reference/libraries).

Ternary has set up a bucket with some files in it for your convenience, but please feel free to set up your own bucket if you so desire.  You can find the bucket here:gs://ternary-public. We’ve granted the following [roles](https://cloud.google.com/storage/docs/access-control/iam-roles) to the email we have on file, but if you’d prefer access via a different email, please let us know the email address: Storage Object Viewer, Storage Legacy Bucket Reader.

## Requirements

While this is meant to be an open prompt, here are some minimum requirements to guide your development and give you a better sense of completion.

- The tool is able to analyze the size of the input storage bucket and objects.
  - Extra credit if the tool can analyze multiple buckets, or even all buckets in a particular project.
- The tool generates a file that can be loaded into a visualization tool of your choice.
- **Hint**: Try using Excel/Sheets to plot a chart.
- Please attach some screenshots of charts or images from your created reporting.

## Submission Guidelines

- Email the source code as a zip or tarball or create a GitHub repo.
- Provide instructions via README for running the app locally on Linux or Mac OS (e.g. make, shell script, ...) Note any required dependencies that must be installed.
- (Recommended but optional) Provide a Docker build for automating the build process and distribution of the final product.
