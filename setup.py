import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kafka_python_handler",
    version="0.0.2",
    author="Ezhil Gowthaman",
    author_email="ezhilgowtha@gmail.com",
    description="A simple package to test kafka-python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ezhil-g/kafka-python-handler",
    keywords=['kafka', 'kafka-python', 'producer', 'consumer'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=['kafka-python;python_version>="3.6"'],
    python_requires='>=3.6',
    zip_safe=False
)



