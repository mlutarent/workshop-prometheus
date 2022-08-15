#!/bin/bash

docker-compose -f docker-compose.yaml -f ../shared/service/docker-compose.yaml up -d --remove-orphans
