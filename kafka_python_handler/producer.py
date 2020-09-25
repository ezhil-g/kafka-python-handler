import json
from kafka import KafkaProducer
from kafka.errors import KafkaError
import threading
import logging

class Producer(threading.Thread):
    daemon = True

    def __init__(self, server, topic):
        self.logger = logging.getLogger()
        self.logger.info("Initializing Kafka Producer")
        self.producer = KafkaProducer(bootstrap_servers=server)
        self.topic = topic

    def send_binary_data(self, data:str):
        self.logger.info('Sending the data {} to topic {}'.format(data, self.topic))
        self.producer.send(self.topic, data)
        self.producer.flush(30)


 
