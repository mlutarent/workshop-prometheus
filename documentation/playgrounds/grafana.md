# Grafana

```shell
# Start
cd /home/vagrant/playgrounds/grafana
```

```shell
docker-compose -f docker-compose.yaml -f shared/service/docker-compose.yaml --remove-orphans
```

* [Grafana Dashboard](http://127.0.0.1:3000) (Default username/password: *admin/admin*)

## Add Prometheus as Data Source

* [Grafana Data sources](http://127.0.0.1:3000/datasources)

*Add source -> Prometheus -> Url: http://prometheus:9090 -> Save & Test*
