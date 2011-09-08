import os
from distutils.core import setup

try:
	import MySQLdb
except ImportError:
	raise Error('datasource requires the python module MySQLdb (http://sourceforge.net/projects/mysql-python/')

def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='datasource',
		version='0.5',
		description='Data Source Encapsulation',
		license='MPL',
		keywords = "data SQL MySQL", 
		author='Jonathan Eads (Jeads)',
		packages=['datasource', 'datasource.bases', 'datasource.hubs', 'datasource.t'],
		long_description=read('README'),
		package_data={'datasource':['procs/mysql/*.json',
											 't/*.txt',
											 '*.json',
											 '*.txt',
											 'README'] }
		)
