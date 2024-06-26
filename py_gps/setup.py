import os
from glob import glob
from setuptools import setup

package_name = 'py_gps'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*launch.py')),
        (os.path.join('share', package_name, 'launch'), glob('launch/common.yaml')), 
        (os.path.join('share', package_name, 'launch'), glob('launch/service.json')), 
        (os.path.join('lib', package_name), glob(package_name + '/*.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mirdc',
    maintainer_email='mirdc@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pub = py_gps.main:main',
        ],
    },
)
