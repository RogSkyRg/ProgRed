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
    
    netconf_data = """
<config>
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
 <interface>
 <Loopback>
 <name>100</name>
 <description>TEST1</description>
 <ip>
 <address>
 <primary>
 <address>100.100.100.100</address>
 <mask>255.255.255.0</mask>
 </primary>
 </address>
 </ip>
 </Loopback>
 </interface>
</native>
</config>
"""

netconf_reply = m.edit_config(target="running", config=netconf_data)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())