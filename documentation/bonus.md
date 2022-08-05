* [Thanos - Highly available Prometheus setup with long term storage capabilities. A CNCF Incubating project. ](https://github.com/thanos-io/thanos)

![](https://camo.githubusercontent.com/4720f0b558ad470b8b73a6e459bac133bef772c92f96e4f327ae303e21254fbd/68747470733a2f2f646f63732e676f6f676c652e636f6d2f64726177696e67732f642f652f32504143582d31765442464b4b6766385944496e4a7952616b504538655a5a67397068546c4f734242326f674e6b4676684e47625a385944767a5f63474d6278575a42473147366870735166535831343546705963762f7075623f773d39363026683d373230)


* [Collection of Prometheus alerting rules ](https://github.com/samber/awesome-prometheus-alerts)


<details>
  <summary>💡 Solution</summary>

  ```
#
# /etc/prometheus/prometheus.yml
#

global:
  scrape_interval: 30s

scrape_configs:
  - job_name: 'node-exporter'
    scrape_interval: 10s
    static_configs:
      - targets: ['node-exporter:9100']
  ```

</details>