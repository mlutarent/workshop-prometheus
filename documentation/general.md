## Prometheus
### Welches Problem will Prometheus loesen?

### Architektur

### Playground: Basics

```shell
# Start
cd /home/vagrant/synced_folder/playgrounds/basics && docker-compose up -d
```

```shell
# Was gibt der Service aus?
curl 127.0.0.1:5000/metrics
```

[Prometheus Dashboard](http://127.0.0.1:55055/graph)

```shell
# clean up
cd /home/vagrant/synced_folder/playgrounds/basics && docker-compose down
```

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
