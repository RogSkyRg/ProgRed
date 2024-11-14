import requests
import json
import logging
from requests.auth import HTTPBasicAuth
import os
import sys

here = os.path.abspath(os.path.dirname(__file__))

project_root = os.path.abspath(os.path.join(here, "../.."))

sys.path.insert(0, project_root)

import env_lab

DNAC_URL = env_lab.DNA_CENTER["host"]
DNAC_USER = env_lab.DNA_CENTER["username"]
DNAC_PASS = env_lab.DNA_CENTER["password"]




def get_auth_token():
    """
    Building out Auth request. Using requests.post to make a call to the Auth Endpoint
    """
    url = 'https://{}/dna/system/api/v1/auth/token'.format(DNAC_URL)                      
    hdr = {'content-type' : 'application/json'}                                           
    try:
        logging.captureWarnings(True)
        resp = requests.post(url, auth=HTTPBasicAuth(DNAC_USER, DNAC_PASS), headers=hdr, verify=False)      
    except Exception as e:
        print("Error: ", e)
    token = resp.json()['Token']                                                          
    return token    


def get_device_list():
   
    token = get_auth_token() # Get Token
    url = "https://{}/api/v1/network-device/1/4".format(DNAC_URL)
    hdr = {'x-auth-token': token, 'content-type' : 'application/json'}
    logging.captureWarnings(True)
    resp = requests.get(url, headers=hdr, verify=False) 
    device_list = resp.json()
    print("{0:25}{1:25}".format("hostname", "id"))
    for device in device_list['response']:
        print("{0:25}{1:25}".format(device['hostname'], device['id']))
    initiate_cmd_runner(token) 


def initiate_cmd_runner(token):
    ios_cmd = "show ver | inc RELEASE"
    device_id = str(input("Copy/Past a device ID here:"))
    print("executing ios command -->", ios_cmd)
    param = {
        "name": "Show Command",
        "commands": [ios_cmd],
        "deviceUuids": [device_id]
    }
    url = "https://{}/api/v1/network-device-poller/cli/read-request".format(DNAC_URL)
    header = {'content-type': 'application/json', 'x-auth-token': token}
    logging.captureWarnings(True)
    response = requests.post(url, data=json.dumps(param), headers=header, verify=False)
    task_id = response.json()['response']['taskId']
    print("Command runner Initiated! Task ID --> ", task_id)
    print("Retrieving Path Trace Results.... ")
    get_task_info(task_id, token)


def get_task_info(task_id, token):
    url = "https://{}/api/v1/task/{}".format(DNAC_URL, task_id)
    hdr = {'x-auth-token': token, 'content-type' : 'application/json'}
    logging.captureWarnings(True)
    task_result = requests.get(url, headers=hdr, verify=False)
    file_id = task_result.json()['response']['progress']
    if "fileId" in file_id:
        unwanted_chars = '{"}'
        for char in unwanted_chars:
            file_id = file_id.replace(char, '')
        file_id = file_id.split(':')
        file_id = file_id[1]
        print("File ID --> ", file_id)
    else:  # keep checking for task completion
        get_task_info(task_id, token)
    get_cmd_output(token, file_id)


def get_cmd_output(token,file_id):
    url = "https://{}/api/v1/file/{}".format(DNAC_URL, file_id)
    hdr = {'x-auth-token': token, 'content-type': 'application/json'}
    logging.captureWarnings(True)
    cmd_result = requests.get(url, headers=hdr, verify=False)
    print(json.dumps(cmd_result.json(), indent=4, sort_keys=True))


if __name__ == "__main__":
    get_device_list()