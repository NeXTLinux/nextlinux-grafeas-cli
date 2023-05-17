#!/usr/bin/python
from setuptools import setup, find_packages
import os, shutil, errno
from nextlinux_grafeas import version

version =  version.version

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

package_name = "nextlinux_grafeas"

description = 'Nextlinux Grafeas CLI'
long_description = open('README.rst').read()

url = 'http://www.next-linux.systems'

#package_data = {}
package_data = {
    package_name: [
        'cli/*',
        'clients/*',
        'conf/*'
    ]
}

#data_files = [('conf', ['conf/config.yaml.example'])]
data_files = []
#data_files = [('datafiles', ['datafiles/lynis-data.tar'])]
#data_files = [
#    ('twisted', ['nextlinux_service/twisted/*'])
#]
#packages=find_packages(exclude=('run*', 'log*', 'conf*', 'dead*', 'scripts/*')),
#scripts = ['scripts/nextlinux-service.sh', 'scripts/nextlinux-service']
scripts = []

setup(
    name='nextlinux_grafeas',
    author='Nextlinux Inc.',
    author_email='dev@next-linux.systems',
    license='Apache License 2.0',
    description=description,
    long_description=long_description,
    url=url,
    packages=find_packages(),
    version=version,
    data_files=data_files,
    include_package_data=True,
    package_data=package_data,
    entry_points='''
    [console_scripts]
    nextlinux-grafeas=nextlinux_grafeas.cli:main_entry
    ''',
    install_requires=requirements,
    scripts=scripts
)
#    entry_points='''
#    [console_scripts]
#    nextlinux=nextlinux.cli:main_entry
#    ''',
