## Prometheus Data Model

`<metric name>{<label name>=<label value>, ...}`

`api_http_requests_total{method="POST", handler="/messages"}`

[🔗 Data model](https://prometheus.io/docs/concepts/data_model/)

### What is a time series in Prometheus?

<details>
<summary>Show / hide</summary>

![](https://iximiuz.com/prometheus-metrics-labels-time-series/time-series-2000-opt.png)

</details>

Read the excellent article/series [Prometheus Cheat Sheet - Basics (Metrics, Labels, Time Series, Scraping)](https://iximiuz.com/en/posts/prometheus-metrics-labels-time-series/) by Ivan Velichko

## Prometheus Four Core Metric Types

[🔗 Metric Types](https://prometheus.io/docs/concepts/metric_types/#metric-types)


### Counter

A value that can only increase or be reset to zero on restart.

Use cases:
* number of requests served
* number of tasks completed
* number of errors

### Gauge

A single numerical value that can arbitrarily go up and down.

Use cases:
* memory/cpu usage
* number of concurrent requests
* ...

### Histogram

A histogram samples observations and counts them in configurable buckets. 
It also provides a sum of all observed values.

Use cases:
* request durations
* response sizes
* ...

### Summary

* using it is discouraged; histograms should be used instead in most scenarios
* like Histograms when you don't know the bucket size beforehand

Uses cases:
* similar to histograms

## Prometheus Jobs and Instances

When Prometheus scrapes a target, it attaches some labels automatically to the scraped time series which serve to identify the scraped target:

* **job:** The configured job name that the target belongs to.
* **instance**: The \<host>:\<port> part of the target's URL that was scraped.

For each instance scrape, Prometheus stores a sample in the following time series:

    up{job="<job-name>", instance="<instance-id>"}: 1 if the instance is healthy, i.e. reachable, or 0 if the scrape failed.
    scrape_duration_seconds{job="<job-name>", instance="<instance-id>"}: duration of the scrape.
    scrape_samples_post_metric_relabeling{job="<job-name>", instance="<instance-id>"}: the number of samples remaining after metric relabeling was applied.
    scrape_samples_scraped{job="<job-name>", instance="<instance-id>"}: the number of samples the target exposed.
    scrape_series_added{job="<job-name>", instance="<instance-id>"}: the approximate number of new series in this scrape. New in v2.10

The *up* time series is useful for instance availability monitoring.

[🔗 Jobs and instances](https://prometheus.io/docs/concepts/jobs_instances/#jobs-and-instances)

---
[back](../overview.md)
