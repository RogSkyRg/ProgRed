from ncclient import manager
import xml.dom.minidom 

device_ip = "152.160.56.101"
username = "cisco"
password = "cisco123!"
netconf_port = 830

with manager.connect(
    host = device_ip,
    port = netconf_port,
    username = username,
    password = password,
    hostkey_verify=False
) as m:
    netconft_reply = m.get_config(source="running")

    print(xml.dom.minidom.parseString(netconft_reply.xml).toprettyxml())

netconft_filter= """
<filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
<filter>
"""

