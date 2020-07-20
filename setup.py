from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='finnews',
    author='Alex Reed',
    author_email='coding.sigma@gmail.com',
    version='0.0.1',
    description='A finance news aggregator used to collect articles on different market topics.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/areed1192/finance-news-aggregator',
    install_requires=[
        'requests'
    ],
    packages=find_packages(include=['finnews']),
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
