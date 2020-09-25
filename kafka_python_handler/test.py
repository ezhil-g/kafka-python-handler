from kafka_python_handler import Handler
import os

if __name__ == "__main__":
    # set the environment variable values directly 
    os.environ['KAFKA_BROKERS']='xxxx'
    os.environ['TOPIC']="kafka-topic"
    handler = Handler()
    handler.test_producer()