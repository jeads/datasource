import os, stat
from distutils.core import setup

try:
    import MySQLdb
except ImportError:
    raise Exception('datasource requires the python module MySQLdb (http://sourceforge.net/projects/mysql-python/')

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

#Set datas_sources.json to be readable by everyone
dirName = os.path.dirname(__file__)
fileName = '.' + dirName + '/datasource/data_sources.json'
os.chmod(fileName, stat.S_IREAD|stat.S_IWRITE|stat.S_IRGRP|stat.S_IWGRP|stat.S_IROTH)

setup(name='datasource',
      version='0.5',
      description='Data Source Encapsulation',
      license='MPL',
      keywords = "data SQL MySQL",
      author='Jonathan Eads (Jeads)',
      packages=['datasource', 'datasource.bases', 'datasource.hubs', 'datasource.t'],
      long_description=read('README'),
      package_data={'datasource':['procs/mysql_procs/*.json',
                                  't/*.txt',
                                  '*.json',
                                  '*.txt',
                                  'README'] }

      )
