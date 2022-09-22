# -*- coding: utf-8 -*-
# @Filename : setup
# @Date : 2022-07-27-11-59
# @Project: content-script-slack-block-builder

import os
import setuptools


def get_version():
    return os.environ.get("ReleaseVersion", "v0.0.0")


def get_description():
    with open("README.md", "r") as fp:
        return fp.read()


setuptools.setup(
    name="slack-blocker-builder-SDK",
    version=get_version(),
    author="stone",
    author_email="github@stone-bo.com",
    description="A utilized tool to construct a slack message block quickly",
    long_description=get_description(),
    url="https://github.com/stone-home/slack-bocker-builder-SDK",
    python_requires=">=3.7",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ]
)