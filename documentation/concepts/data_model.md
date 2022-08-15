# Prometheus Data Model

> Prometheus fundamentally stores all data as time series: streams of timestamped values belonging to the same metric and the same set of labeled dimensions. Besides stored time series, Prometheus may generate temporary derived time series as the result of queries.

## Structure

`<metric name>{<label name>=<label value>, ...}`

## Example

`api_http_requests_total{method="POST", handler="/messages"}`

[🔗 Data model](https://prometheus.io/docs/concepts/data_model/)

## What is a time series in Prometheus?

<details>
<summary>Show / hide</summary>

![](https://iximiuz.com/prometheus-metrics-labels-time-series/time-series-2000-opt.png)

From the excellent article/series [Prometheus Cheat Sheet - Basics (Metrics, Labels, Time Series, Scraping)](https://iximiuz.com/en/posts/prometheus-metrics-labels-time-series/) by Ivan Velichko

</details>


---
[back](../overview.md)
