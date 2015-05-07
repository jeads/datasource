import os, stat
kwargs = {}
try:
    from setuptools import setup
    kwargs["install_requires"] = ["MySQL-python"]
except ImportError:
    from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='datasource',
    version='0.7',
    description='Data Source Encapsulation',
    license='MPL',
    keywords = "data SQL MySQL", 
    author='Jonathan Eads (Jeads)',
    packages=['datasource', 'datasource.bases', 'datasource.hubs', 'datasource.t'],
    long_description=read('README.md'),
    package_data={'datasource':['procs/mysql_procs/*.json',
                                  't/*.txt',
                                  '*.json',
                                  '*.txt',
                                  'README.md'] },
    **kwargs
    )
