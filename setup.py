from setuptools import setup
from setuptools import find_namespace_packages
from setuptools import find_packages

with open(file="README.md", mode="r") as fh:
    long_description = fh.read()

setup(
    name='fin-news',
    author='Alex Reed',
    author_email='coding.sigma@gmail.com',
    version='0.1.0',
    description='A finance news aggregator used to collect articles on different market topics.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/areed1192/finance-news-aggregator',
    install_requires=[
        'requests'
    ],
    packages=find_namespace_packages(
        include=['finnews', 'finnews.*']
    ),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3'
    ],
    python_requires='>3.7'
)
