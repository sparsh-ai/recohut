# Data Contract

## Example

```yaml
 — -
data_product: customer_orders
name: Customer Orders
description: A stream of all Customer Orders
platform: Kafka
uri: <link to data product>
roles: viewer # list of roles/ IAM policies that have access to the Data Product
schema: <link to schema>
owner: devops_team@enterprise.com
cost_centre: cost_centre_a
version: 0.0.1
documentation: <link to documentation>
lineage:
 — data_product_a
 — data_product_b
lineage_specification: <link to lineage definition> # e.g. https://github.com/OpenLineage/OpenLineage/blob/main/spec/OpenLineage.md
service_level_objective: tier_1
service_level_definition: <link to definition> # maybe superfluous
related_data_products:
 — customer
 — product_details
pii: yes
domain: customer
tags:
 — tag_a
 — tag_b
life_cycle: generally_available # as opposed to beta, end of life, deprecated, etc.
development_version: <link> # a version consumers can test against with mock data
```