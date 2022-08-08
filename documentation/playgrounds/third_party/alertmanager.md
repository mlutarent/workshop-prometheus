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
