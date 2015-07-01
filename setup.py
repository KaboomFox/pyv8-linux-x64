
#!/usr/bin/env python

import os

from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="PyV8",
    version="1.0",
    author="The internet",
    author_email="louise.s.fox@gmail.com",
    description="wrapper for PyV8 binary for Linux x64",
    long_description="wrapper for PyV8 binary for Linux x64",
    license="",
    url="https://github.com/louisef/pyv8-linux-x64",
    packages=find_packages(),
    zip_safe=False,
    package_data={
        'pyv8': ['*.so']
    },
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: Linux",
        "Programming Language :: Python",
    ]
)
