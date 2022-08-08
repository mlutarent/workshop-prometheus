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
---
[back](../overview.md)
