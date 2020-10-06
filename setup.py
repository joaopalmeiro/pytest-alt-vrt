#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import os

from setuptools import find_packages, setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding="utf-8").read()


setup(
    name="pytest-alt-vrt",
    version="0.1.0",
    author="João Palmeiro",
    author_email="jm.palmeiro@campus.fct.unl.pt",
    maintainer="João Palmeiro",
    maintainer_email="jm.palmeiro@campus.fct.unl.pt",
    license="MIT",
    url="https://github.com/joaopalmeiro/pytest-alt-vrt",
    description="A simple plugin to use with pytest",
    long_description=read("README.rst"),
    packages=find_packages(),
    python_requires=">=3.6, <=3.8",
    install_requires=["pytest-selenium", "Pillow", "scikit-image", "altair"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={"pytest11": ["alt_vrt = pytest_alt_vrt.plugin"]},
)
