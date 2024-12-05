from ncclient import manager
import xml.etree.ElementTree as ET

host = 'devnetsandboxiosxe.cisco.com'
port = 830
username = 'admin'
password = 'cisco123!'

with manager.connect(host=host, port=port, username=username, password=password, hostkey_verify=False) as m:

    hello_message = '''\
        <hello xmlns="urn:ietf:params:xml:ns:netconft:base:1.0">
        </captabilities>
    </hello>'''

    response = m.dispatch(ET.fromstring(hello_message))
    print("Respuesta del servidor despues de enviar nuestro hello: ")
    print(ET.tostring(response, encoding='unicode'))

    get_rpc = '''\
    <rpc message-id="103" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <get>
            <filter>
                <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
            </filter>
        </get>
    </rpc>'''