from ncclient import manager

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
    print("#Supported Capabilities (YANG models): ")

    for capatibility in m.server_capabilities:
        print(capatibility)