# pip install wheel
# python setup.py bdist_wheel
#
#
#
#
from setuptools import find_packages, setup

setup(
    name='publisher',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask>=2.2.2',
        'rdflib>=6.2.0',
        'requests>=2.28.1',
        'publisher',
    ],
)