#ver=2.0
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

import os
import json
import yaml
from yaml import load, Loader

pkgName = 'cpp_webcam'

def generate_launch_description():
    commonFilePath = os.path.join(get_package_share_directory(pkgName), 'launch/common.yaml')
    with open(commonFilePath, 'r') as f:
        data = yaml.load(f, Loader=Loader)

    serviceFilePath = os.path.join(get_package_share_directory(pkgName), 'launch/service.json')
    with open(serviceFilePath, 'r') as f:
        serviceData = json.load(f)

    return LaunchDescription([
        Node(
            package=pkgName,
            namespace=data['generic_prop']['namespace'],
            executable=data['launch_node'],
            output="screen",
            emulate_tty=True,
            parameters=[
                {
                    "topic_Webcam_nodeName" : data['topic_Webcam']['nodeName'] + '_' + str(data['generic_prop']['id']) + '_node', 
                    "topic_Webcam_topicName" : data['topic_Webcam']['topicName'] + '_' + str(data['generic_prop']['id']), 
                    "topic_Webcam_pubInterval_s" : data['topic_Webcam']['publishInterval_s'], 
                    "topic_Webcam_width" : data['topic_Webcam']['width'], 
                    "topic_Webcam_height" : data['topic_Webcam']['height'], 
                    "camera_cap_id" : data['camera_prop']['cap_id'], 
                    "camera_fps" : data['camera_prop']['fps'], 
                    "camera_width" : data['camera_prop']['width'], 
                    "camera_height" : data['camera_prop']['height'], 
                    "camera_use_color" : data['camera_prop']['use_color'], 

                    # Settings for Params class under vehicle_interfaces/params.h
                    # Do not change the settings rashly
                    "nodeName" : data['generic_prop']['nodeName'] + '_' + str(data['generic_prop']['id']) + '_node', 
                    "id" : data['generic_prop']['id'], 
                    "devInfoService" : serviceData['devInfoService'], 
                    "devInterface" : serviceData['devInterface'], 
                    "devMultiNode" : serviceData['devMultiNode'], 
                    "qosService" : serviceData['qosService'], 
                    "qosDirPath" : serviceData['qosDirPath'], 
                    "safetyService" : serviceData['safetyService'], 
                    "timesyncService" : serviceData['timesyncService'], 
                    "timesyncPeriod_ms" : serviceData['timesyncPeriod_ms'], 
                    "timesyncAccuracy_ms" : serviceData['timesyncAccuracy_ms'], 
                    "timesyncWaitService" : serviceData['timesyncWaitService'], 
                }
            ]
        )
    ])