# Alert Manager

```shell
# Start
cd /home/vagrant/playgrounds/alerting
```

```shell
docker-compose -f docker-compose-alerting.yaml -f shared/service/docker-compose.yaml up -d --remove-orphans
```
* [Alert Manager UI](http://127.0.0.1:9093)
* [Prometheus Dashboard](http://127.0.0.1:9090/graph)
* [Webmail](http://127.0.0.1:8025)

## Trigger alert

```shell
docker-compose stop service-a
```

[Watch Prometheus](http://127.0.0.1:9090/alerts)
