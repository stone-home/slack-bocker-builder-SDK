# -*- coding: utf-8 -*-
# @Filename : setup
# @Date : 2022-07-27-11-59
# @Project: content-script-slack-block-builder

import os
import setuptools


def get_version():
    if os.path.exists("version.txt"):
        with open("version.txt", "r") as fp:
            version = fp.read()
    else:
        version = "v0.0.0"
    version = version.replace("v", "")
    return version


def get_description():
    with open("README.md", "r") as fp:
        return fp.read()


setuptools.setup(
    name="slack-block-builder",
    version=get_version(),
    author="Jiabo Shi",
    author_email="jiabo.shi01@sap.com",
    description="A utilized tool to construct a slack message block quickly",
    long_description=get_description(),
    url="https://github.tools.sap/IO-ContentStore/content-script-slack-block-builder",
    python_requires=">=3.7",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ]
)