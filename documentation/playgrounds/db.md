# DB integration example

Running Postgres with [PostgreSQL Server Exporter](https://github.com/prometheus-community/postgres_exporter) to expose metrics.
Importing a [preconfigured dashboard](https://grafana.com/grafana/dashboards/9628 ) into Grafana

```shell
cd /home/vagrant/playgrounds/db
```

```shell
docker-compose up
```

* [Prometheus Dashboard](http://127.0.0.1:9090/graph)
* [Postgres Exporter Metrics](http://127.0.0.1:9093/metrics)
* Go to [Dashboards -> Import dashboard](http://127.0.0.1:3000/dashboard/import) (Default username/password: *admin/admin*)
* Paste `https://grafana.com/grafana/dashboards/9628` into field "URL"

---
[back](../overview.md)