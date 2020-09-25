## kafka-python-handler

kafka-python-handler is a wrapper around kafka-python package. This package is easy to use and can be used to test the Kafka Producer in kafka-python package.

Some important items to note.

* This package includes the basic testing only as of now.

*  Polling, parallelism etc. has not been included yet.

### Installation Instructions

The package is availble in PyPI which is an official repository for python package.
pip is a package management system and is used for installing Python packages from Python Package Index (also known as PyPI). It is the most common way to install Python packages.
Install the package in your environment using:

`pip install kafka-python-handler`


### Pre-requisites

- Python 3.x

- pip3

- Set the environment variables - KAFKA_BROKERS and TOPIC.


### How to Use?

* Import the Handler into your python code.

    `from kafka_python_handler import Handler`

#### Test Producer

To test the producer, perform the below steps.

* Instantiate the handler and then, call the test_producer().

```
handler = Handler()
handler.test_producer()
```
### License

```
Apache License
```

 The complete license terms can be found in `LICENSE` file in this repository.