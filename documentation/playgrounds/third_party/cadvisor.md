### Google cadvisor

[Google cadvisor - Analyzes resource usage and performance characteristics of running containers](https://github.com/google/cadvisor)

```shell
cd /home/vagrant/playgrounds/third_party/prometheus-community/cadvisor && make run
```
[http://localhost:9090/graph](http://localhost:9090/graph)

> Some example metrics to explore:
> 
> rate(container_cpu_usage_seconds_total{name="redis"}[1m])
> container_memory_usage_bytes{name="redis"}
> rate(container_network_transmit_bytes_total[1m])
> rate(container_network_receive_bytes_total[1m])

---
[back](../../overview.md)