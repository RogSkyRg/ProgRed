from netmiko import ConnectHandler

sshCli = {
    'device_type': 'cisco_ios',
    'host': 'devnetsandboxiosxe.cisco.com',  
    'username': 'admin', 
    'password': 'cisco12345',  
    'port': 22,  
    
}

try:
    connection = ConnectHandler(**sshCli)
    print("Conexión exitosa al dispositivo.")

    output = connection.send_command("show ip interface brief")
    print("Salida del comando 'show ip interface brief':")
    print(output)

    connection.disconnect()
    print("Conexión cerrada.")
except Exception as e:
    print(f"Error al conectar: {e}")
