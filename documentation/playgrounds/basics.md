# Playground: Basics

```shell
# Start
cd /home/vagrant/playgrounds/basics
```

```shell
# Start
docker-compose -f docker-compose.yaml -f service/docker-compose.yaml up --remove-orphans
```

```shell
# Was gibt der Service aus?
curl 127.0.0.1:5000/metrics
```
* [Prometheus Dashboard](http://127.0.0.1:9090/graph)
* [Service A metrics](http://127.0.0.1:5000/metrics)
* [Service B metrics](http://127.0.0.1:5001/metrics)

---
[back](../overview.md)


## Grafana

```shell
docker-compose -f docker-compose.yaml -f service/docker-compose.yaml -f grafana/docker-compose.yaml up --remove-orphans
```

* [Grafana Dashboard](http://127.0.0.1:3000) (Default username/password: *admin/admin*)

### Add Prometheus as Data Source

* [Grafana Data sources](http://127.0.0.1:3000/datasources)

*Add source -> Prometheus -> Url: http://prometheus:9090 -> Save & Test*

## Alert Manager

```shell
docker-compose -f docker-compose-alerting.yaml -f service/docker-compose.yaml up -d --remove-orphans
```
* [Alert Manager UI](http://127.0.0.1:9093)
* [Prometheus Dashboard](http://127.0.0.1:9090/graph)
* [Webmail](http://127.0.0.1:8025)

### Trigger alert

```shell
docker-compose stop service-a
```

[Watch Prometheus](http://127.0.0.1:9090/alerts)
