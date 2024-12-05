from ncclient import manager
import xml.dom.minidom 
import xmltodict

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
    <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
<filter>
"""

with manager.connect(**manager.connect) as m:
    netconft_reply = m.get(filter=netconft_filter)

print(xml.dom.minidom.parseString(netconft_filter).toprettyxml)

netconft_reply_dict = xmltodict.parse(netconft_reply.xml)


print("\nResumen de estadisticas de interfaces:\n")
print("{:<15} {:<20} {:<15} {:<15} ".format('Nombre', 'Direccion MAC', 'Bytes de Entradas', 'Bites de Salidas'))

for interfaz in netconft_reply_dict["rpc-reply"]["data"]["Interfaces-state"]["interface"]:
    print("{:<15} {:<20} {:<15} {:<15}" .format (
        interfaz["name"],
        interfaz["phys-address"],
        interfaz["statiscs"]["in-octets"],
        interfaz["statiscs"]["out-octets"]
    ))
