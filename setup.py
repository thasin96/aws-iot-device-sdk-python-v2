#!/usr/bin/env python

# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0.

from setuptools import setup

setup(
    name='awsiotsdk',
    version='1.0.0-dev',
    description='AWS IoT SDK based on the AWS Common Runtime',
    author='AWS SDK Common Runtime Team',
    url='https://github.com/aws/aws-iot-device-sdk-python-v2',
    packages=['awsiot'],
    install_requires=[
        'awscrt==0.9.10',
    ],
    python_requires='>=3.5',
)
