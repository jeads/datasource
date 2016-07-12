#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os

kwargs = {}
try:
    from setuptools import setup
    kwargs["install_requires"] = ["mysqlclient"]
except ImportError:
    from distutils.core import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='datasource',
    version='0.10.0',
    description='Data Source Encapsulation',
    license='MPL',
    keywords="data SQL MySQL",
    author='Jonathan Eads (Jeads)',
    packages=['datasource', 'datasource.bases', 'datasource.hubs', 'datasource.t'],
    long_description=read('README.md'),
    package_data={'datasource': ['procs/mysql_procs/*.json',
                                 't/*.txt',
                                 '*.json',
                                 '*.txt',
                                 'README.md']},
    **kwargs
)
