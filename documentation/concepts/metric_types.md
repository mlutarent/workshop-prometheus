# Prometheus Four Core Metric Types

[🔗 Metric Types](https://prometheus.io/docs/concepts/metric_types/#metric-types)

## Counter

A value that can only increase or be reset to zero on restart.

Use cases:
* number of requests served
* number of tasks completed
* number of errors

<details>
<summary>Show / hide</summary>

```shell
# HELP prometheus_tsdb_checkpoint_creations_total Total number of checkpoint creations attempted.
# TYPE prometheus_tsdb_checkpoint_creations_total counter
prometheus_tsdb_checkpoint_creations_total 0
```

</details>

## Gauge

A single numerical value that can arbitrarily go up and down.

Use cases:
* memory/cpu usage
* number of concurrent requests
* ...

<details>
<summary>Show / hide</summary>

```shell
# HELP go_goroutines Number of goroutines that currently exist.
# TYPE go_goroutines gauge
go_goroutines 34
```

</details>

## Histogram

A histogram samples observations and counts them in configurable buckets. 
It also provides a sum of all observed values.

Use cases:
* request durations
* response sizes
* ...

For querying: Uses the [histogram_quantile function](https://prometheus.io/docs/prometheus/latest/querying/functions/#histogram_quantile)

<details>
<summary>Show / hide</summary>

Example: Histogram metrics exposed by a Prometheus instance:

```shell
# HELP prometheus_http_request_duration_seconds Histogram of latencies for HTTP requests.
# TYPE prometheus_http_request_duration_seconds histogram
prometheus_http_request_duration_seconds_bucket{handler="/",le="0.1"} 25547
prometheus_http_request_duration_seconds_bucket{handler="/",le="0.2"} 26688
prometheus_http_request_duration_seconds_bucket{handler="/",le="0.4"} 27760
prometheus_http_request_duration_seconds_bucket{handler="/",le="1"} 28641
prometheus_http_request_duration_seconds_bucket{handler="/",le="3"} 28782
prometheus_http_request_duration_seconds_bucket{handler="/",le="8"} 28844
prometheus_http_request_duration_seconds_bucket{handler="/",le="20"} 28855
prometheus_http_request_duration_seconds_bucket{handler="/",le="60"} 28860
prometheus_http_request_duration_seconds_bucket{handler="/",le="120"} 28860
prometheus_http_request_duration_seconds_bucket{handler="/",le="+Inf"} 28860
prometheus_http_request_duration_seconds_sum{handler="/"} 1863.80491025699
prometheus_http_request_duration_seconds_count{handler="/"} 28860
```

</details>

* [How to visualize Prometheus histograms in Grafana](https://grafana.com/blog/2020/06/23/how-to-visualize-prometheus-histograms-in-grafana/)


## Summary

* like Histograms when you don't know the bucket size beforehand

Uses cases:
* similar to histograms

What's the difference ?

* see [Histograms and Summaries](https://prometheus.io/docs/practices/histograms/)


<details>
<summary>Show / hide</summary>

```shell
# HELP go_gc_duration_seconds A summary of the GC invocation durations.
# TYPE go_gc_duration_seconds summary
go_gc_duration_seconds{quantile="0"} 2.0397e-05
go_gc_duration_seconds{quantile="0.25"} 2.4165e-05
go_gc_duration_seconds{quantile="0.5"} 4.4332e-05
go_gc_duration_seconds{quantile="0.75"} 0.00021932
go_gc_duration_seconds{quantile="1"} 0.001155838
go_gc_duration_seconds_sum 0.001550392
go_gc_duration_seconds_count 7
```

</details>

---
[back](../overview.md)
