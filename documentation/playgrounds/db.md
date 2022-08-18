# Exporter: DB integration example

## Components

* Postgres instance with [PostgreSQL Server Exporter](https://github.com/prometheus-community/postgres_exporter) to expose metrics.
  * [docker-compose.yaml](../../playgrounds/db/docker-compose.yaml)

## Run playground

```shell
cd /home/vagrant/playgrounds/db
```

```shell
./run.sh
```

* [Prometheus Dashboard](http://127.0.0.1:9090/graph)

* Paste `https://grafana.com/grafana/dashboards/9628` into field "URL"

## Things to do with this playground
* Check out the [Postgres Exporter Metrics](http://127.0.0.1:9093/metrics)
* Import a [preconfigured dashboard](https://grafana.com/grafana/dashboards/9628 ) into Grafana
  * [Grafana Dashboard Json](https://github.com/lstn/misc-grafana-dashboards/blob/master/dashboards/postgresql-database.json) 
  * Add prometheus as [Data Source ](http://127.0.0.1:3000/datasources)
    * http://prometheus:9090
  * Go to [Dashboards -> Import dashboard](http://127.0.0.1:3000/dashboard/import) 
    * (username: admin,  password: admin)

---
[back](../overview.md)
