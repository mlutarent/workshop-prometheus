## Simple Go app using the official prometheus client

## Components

* All components are from a  [third party repo](https://github.com/prometheus-community/prometheus-playground/tree/master/go-app)

## Run playground

```shell
cd /home/vagrant/playgrounds/third_party/prometheus-community/go-app
```

```shell
make run-detached
```

Please note that the app [imports the prometheus go client](https://github.com/prometheus-community/prometheus-playground/blob/master/go-app/myapp/main.go)

## Things to do with this playground

Have a look at the metrics the Go client library exposes:

```shell
curl http://127.0.0.1:2112/metrics
```

## Stop playground

```shell
make kill
```

---
[back](../../overview.md)
