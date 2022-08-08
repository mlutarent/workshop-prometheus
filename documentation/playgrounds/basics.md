# Playground: Basics

```shell
# Start
cd /home/vagrant/playgrounds/basics
```

```shell
# Start
docker-compose -f docker-compose.yaml -f shared/service/docker-compose.yaml up --remove-orphans
```

* [Prometheus Dashboard](http://127.0.0.1:9090/graph)
* [Service A metrics](http://127.0.0.1:5000/metrics)
* [Service B metrics](http://127.0.0.1:5001/metrics)

---
[back](../overview.md)