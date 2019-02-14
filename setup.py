from distutils.core import setup
from setuptools import find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='exmplpckg',
    author='Dennis',
    install_requires=requirements,
    packages=find_packages()
)
