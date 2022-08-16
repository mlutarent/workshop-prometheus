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

<details>
<summary>Show / hide</summary>

Example: Histogram metrics exposed by a Prometheus instance:

```shell
# HELP prometheus_tsdb_compaction_chunk_range_seconds Final time range of chunks on their first compaction
# TYPE prometheus_tsdb_compaction_chunk_range_seconds histogram
prometheus_tsdb_compaction_chunk_range_seconds_bucket{le="100"} 0
prometheus_tsdb_compaction_chunk_range_seconds_bucket{le="400"} 0
prometheus_tsdb_compaction_chunk_range_seconds_bucket{le="1600"} 0
prometheus_tsdb_compaction_chunk_range_seconds_bucket{le="6400"} 0
prometheus_tsdb_compaction_chunk_range_seconds_bucket{le="25600"} 0
prometheus_tsdb_compaction_chunk_range_seconds_bucket{le="102400"} 0
prometheus_tsdb_compaction_chunk_range_seconds_bucket{le="409600"} 0
prometheus_tsdb_compaction_chunk_range_seconds_bucket{le="1.6384e+06"} 0
prometheus_tsdb_compaction_chunk_range_seconds_bucket{le="6.5536e+06"} 0
prometheus_tsdb_compaction_chunk_range_seconds_bucket{le="2.62144e+07"} 0
prometheus_tsdb_compaction_chunk_range_seconds_bucket{le="+Inf"} 0
prometheus_tsdb_compaction_chunk_range_seconds_sum 0
prometheus_tsdb_compaction_chunk_range_seconds_count 0
```

</details>


## Summary

* like Histograms when you don't know the bucket size beforehand
* see [Histograms and Summaries](https://prometheus.io/docs/practices/histograms/)

Uses cases:
* similar to histograms

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
