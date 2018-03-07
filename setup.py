from distutils.core import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='exmplpckg',
    author='Dennis',
    install_requires=requirements
)
