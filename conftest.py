#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# @Filename : conftest
# @Date : 2022-01-26-21-32
# @Project: content-service-chat-assistant

import pytest


def pytest_collection_modifyitems(items):
    for item in items:
        if "__ut__" in item.nodeid:
            item.add_marker(pytest.mark.unittest)
        elif "__it__" in item.nodeid:
            item.add_marker(pytest.mark.integrationtest)