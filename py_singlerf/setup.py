import os
from glob import glob
from setuptools import setup

package_name = 'py_singlerf'

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
        (os.path.join('share', package_name, 'launch'), glob('launch/service.json'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='coco',
    maintainer_email='cocobird231@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'send = py_singlerf.rfAll:main_send', 
            'recv = py_singlerf.rfAll:main_recv', 
            'pub = py_singlerf.rfAll:main'
        ],
    },
)
