from setuptools import setup, find_packages

setup(
    name="institutional-crypto-funding-analyzer",
    version="2.1.0",
    packages=find_packages(),
    install_requires=open("requirements.txt").readlines(),
    author="Vishnu Govind",
    description="A tool for analyzing crypto funding rates",
    license="MIT",
)
