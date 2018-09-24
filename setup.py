from setuptools import setup, find_packages

__author__ = 'Paola Soto'

with open('requirements.txt') as f:
	requirements = f.read().splitlines()


setup(
    name='demos-ow',
    version='0.0.1',
    packages=find_packages(),
    url = 'https://github.com/paolasoto88/demos-OW.git',
    author='Paola Soto',
    author_email='paolasoto88@gmail.com',
    description='demos-ow',
    install_requires=requirements,
)
