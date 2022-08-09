# Prometheus and Grafana

## Heads Up: Running the playgrounds

* [📕 Running the playgrounds](playgrounds/run.md)

## What Problem does Prometheus try to solve?

    From metrics to insight

    Power your metrics and alerting with the leading
    open-source monitoring solution. [1] 

    [1] https://prometheus.io/

* [🔗 Main Features](https://prometheus.io/docs/introduction/overview/#features)

## How does Prometheus try to solve the Problem?

* [📕 Architecture](concepts/architecture.md)
* [🧰 Playground: Basics](playgrounds/basics.md)
* [📕 Concepts](concepts/concepts.md)
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

## When does Prometheus fit? When does it not?

* [🔗 When does it fit?](https://prometheus.io/docs/introduction/overview/#when-does-it-fit)
* [🔗 When does it not fit?](https://prometheus.io/docs/introduction/overview/#when-does-it-not-fit)

## Advanced topics

### Recording Rules

> Recording rules allow you to precompute frequently needed or computationally expensive expressions and save their result as a new set of time series. Querying the precomputed result will then often be much faster than executing the original expression every time it is needed.

* [🔗 Recording rules](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/#recording-rules)

### Third Party Playgrounds

* [🧰 Playground: Google cadvisor](playgrounds/third_party/cadvisor.md)
* [🧰 Playground: Federation](playgrounds/third_party/federation.md)

### High Availability

* [📕 High Availability](concepts/ha.md)
