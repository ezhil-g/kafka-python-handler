from kafka_python_handler import Handler
import logging
import time
import os

if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:' +
               '%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
    )
    # set the environment variable values directly 
    os.environ['KAFKA_BROKERS']='xxx'
    os.environ['TOPIC']="kafka-topic"
    handler = Handler()
    handler.test_producer()