# Prometheus Four Core Metric Types

[🔗 Metric Types](https://prometheus.io/docs/concepts/metric_types/#metric-types)

## Counter

A value that can only increase or be reset to zero on restart.

Use cases:
* number of requests served
* number of tasks completed
* number of errors

## Gauge

A single numerical value that can arbitrarily go up and down.

Use cases:
* memory/cpu usage
* number of concurrent requests
* ...

## Histogram

A histogram samples observations and counts them in configurable buckets. 
It also provides a sum of all observed values.

Use cases:
* request durations
* response sizes
* ...

## Summary

* using it is discouraged; histograms should be used instead in most scenarios
* like Histograms when you don't know the bucket size beforehand

Uses cases:
* similar to histograms

---
[back](../overview.md)
