import requests
from requests.auth import HTTPBasicAuth

url = "https://devnetsandboxiosxe.cisco.com/restconf/data/native"
headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}
response = requests.get(url, headers=headers, auth=HTTPBasicAuth("admin", "C1sco12345"), verify=False)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}, {response.text}")
