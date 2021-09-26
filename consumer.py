from kafka import KafkaConsumer

#define a consumer that waits for new messages
def kafka_python_consumer():
    consumer  = KafkaConsumer('mytesttopic', group_id='mypthonconsumer', bootstrap_servers='localhost:9092')
    for msg in consumer:
        print(msg)

print("start consuming")

kafka_python_consumer()

print("done")