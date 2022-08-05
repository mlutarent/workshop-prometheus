## Prometheus
### Welches Problem will Prometheus loesen?

### Architektur

### Playground: Basics

```shell
# Start
cd /home/vagrant/playgrounds/basics && docker-compose up -d
```

```shell
# Was gibt der Service aus?
curl 127.0.0.1:5000/metrics
```

[Prometheus Dashboard](http://127.0.0.1:55055/graph)

```shell
# clean up
cd /home/vagrant/playgrounds/basics && docker-compose down
```

### What is a time series in Prometheus?

![](https://iximiuz.com/prometheus-metrics-labels-time-series/time-series-2000-opt.png)

### PromQL

### Client Libraries: Beispiel Python

* [Prometheus Client Libs](https://prometheus.io/docs/instrumenting/clientlibs/)
* [Flask integration](https://github.com/prometheus/client_python#flask)

### Exporters and Integrations

* [Exporters and Integrations](https://prometheus.io/docs/instrumenting/exporters/#exporters-and-integrations)
* [Software exposing Prometheus metrics](https://prometheus.io/docs/instrumenting/exporters/#software-exposing-prometheus-metrics)

#### Prometheus & K8s

#### Playground: Prometheus Operator

[microk8s addon](https://microk8s.io/docs/addons)

## Grafana

### Welches Problem will Grafana loesen?

> The expression browser is available at /graph on the Prometheus server, allowing you to enter any expression and see its result either in a table or graphed over time.
> This is primarily useful for ad-hoc queries and debugging. For graphs, use Grafana or Console templates. [1]

[1] https://prometheus.io/docs/visualization/browser/

## Tested Third Party playgrounds

### Simple Go app using the official prometheus client

[Docs](https://github.com/prometheus-community/prometheus-playground/tree/master/go-app)

```shell
cd /home/vagrant/playgrounds/third_party/prometheus-community/go-app && make run
```

### Federation

[Federation Docs](https://prometheus.io/docs/prometheus/latest/federation/)

```shell
cd /home/vagrant/playgrounds/third_party/prometheus-community/federation && make run
```
[http://localhost:9090/graph](http://localhost:9090/graph)


### Google cadvisor

[Google cadvisor - Analyzes resource usage and performance characteristics of running containers](https://github.com/google/cadvisor)

```shell
cd /home/vagrant/playgrounds/third_party/prometheus-community/cadvisor && make run
```
[http://localhost:9090/graph](http://localhost:9090/graph)

> Some example metrics to explore:
> 
> rate(container_cpu_usage_seconds_total{name="redis"}[1m])
> container_memory_usage_bytes{name="redis"}
> rate(container_network_transmit_bytes_total[1m])
> rate(container_network_receive_bytes_total[1m])

### Alert Manager

**Please note: The `amtool` service causes an error when running docker-compose. It's not strictly needed for the lab. Just comment it out in der docker-compose.yml**

```shell
cd /home/vagrant/playgrounds/third_party/prometheus-community/alertmanager && make run-detached
```

```shell
docker-compose stop hello
```

```shell
docker-compose logs webhook
```

[Alert Manager Dashboard](http://localhost:9093/)
