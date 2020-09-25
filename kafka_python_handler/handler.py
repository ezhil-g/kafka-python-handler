import logging
import time
import os

from producer import Producer

class Handler():

    def __init__(self):
        if 'KAFKA_BROKERS' in os.environ:
            self.kafka_broker = os.environ['KAFKA_BROKERS']
        else:
            raise ValueError('KAFKA_BROKERS environment variable not set')

        if 'TOPIC' in os.environ:
            self.topic = os.environ['TOPIC']
        else:
            raise ValueError('TOPIC environment variable not set')

        self.logger = logging.getLogger()

        self.logger.info("KAFKA_BROKERS={}".format(self.kafka_broker))
        self.logger.info("TOPIC={}".format(self.topic))

    def send_binary_data(self,value):
        producer = Producer(self.kafka_broker, self.topic)
        self.logger.info("Running Kafka Producer")
        self.logger.info("Data")
        self.logger.info(value)
        producer.send_binary_data(value)
        time.sleep(3)

    def test_producer(self):
        logging.info("Let's initialize the kafka server....")
        try:          
            while True:
                value = input('value:')
                value = bytes(value, encoding='utf8')
                self.send_binary_data(value)
        except KeyboardInterrupt:
            print("Press Ctrl-C to terminate while statement")
            pass

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
