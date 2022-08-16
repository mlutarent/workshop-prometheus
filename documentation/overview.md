# Prometheus and Grafana

## Heads Up: Running the playgrounds

* [📕 Running the playgrounds](playgrounds/run.md)

## What Problem does Prometheus try to solve?

* [📕 Features](concepts/features.md)

## How does Prometheus try to solve the Problem?

* [🧰 Playground: Basics](playgrounds/basics.md)
* [📕 Architecture](concepts/architecture.md)
* [📕 Data Model](concepts/data_model.md)
* [📕 Metric Types](concepts/metric_types.md)
* [📕 Jobs and Instances](concepts/jobs_instances.md)
* [📕 Querying](concepts/querying.md)

## Grafana

* [📕 Grafana](concepts/grafana.md)
* [🧰 Playground: Grafana](playgrounds/grafana.md)

## Alerting

* [📕 Alerting](concepts/alerting.md)
* [🧰 Playground: Alerting](playgrounds/alerting.md)

## Integrations

* [📕 Integrations](concepts/integrations.md)
* [🧰 Playground: Simple Go App](playgrounds/third_party/simple_go_app.md)
* [🧰 Playground: DB](playgrounds/db.md)


## Advanced topics

### Pushing Metrics

> Occasionally you will need to monitor components which cannot be scraped. The Prometheus Pushgateway allows you to push time series from short-lived service-level batch jobs to an intermediary job which Prometheus can scrape. Combined with Prometheus's simple text-based exposition format, this makes it easy to instrument even shell scripts without a client library.

[Pushing Metrics](https://prometheus.io/docs/instrumenting/pushing/)

### Recording Rules

> Recording rules allow you to precompute frequently needed or computationally expensive expressions and save their result as a new set of time series. Querying the precomputed result will then often be much faster than executing the original expression every time it is needed.

* [🔗 Recording rules](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/#recording-rules)

### Kubernetes

* [🔗 Prometheus Operator](https://github.com/prometheus-operator/prometheus-operator)

### Third Party Playgrounds

* [🧰 Playground: Google cadvisor](playgrounds/third_party/cadvisor.md)
* [🧰 Playground: Federation](playgrounds/third_party/federation.md)

### High Availability

* [📕 High Availability](concepts/ha.md)
