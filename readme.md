# Kafka Quickstart

This is a quick repo do build Kafka and test run it using Python API of Kafka. Note: this is a minimal working kafka setup.

## Build docker image
Build docker image:
```
docker-compose up -d
```

## Python API
Install python library 
```
pip install kafka-python
```

To run consumer:
```
>>> python consumer.py
```

To run producer:
```
>>> python producer.py
```