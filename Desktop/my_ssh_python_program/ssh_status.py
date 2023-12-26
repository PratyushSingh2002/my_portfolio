import paramiko

# List of devices to connect to
devices = [
    {"hostname": "192.168.0.103", "username": "pratush", "password": "2250028812", "device_name": "HP"},
    {"hostname": "192.168.0.107", "username": "ssv", "password": "123456", "device_name": "PC01"},
    {"hostname": "192.168.0.117", "username": "ssv", "password": "123456", "device_name": "PC03"},
    {"hostname": "192.168.0.123", "username": "ssv", "password": "123456", "device_name": "PC04"},
    {"hostname": "192.168.0.125", "username": "ssv", "password": "123456", "device_name": "PC09"},
    {"hostname": "192.168.0.124", "username": "ssv", "password": "123456", "device_name": "PC10"},
    {"hostname": "192.168.0.119", "username": "ssv", "password": "123456", "device_name": "PC08"},
    {"hostname": "192.168.0.130", "username": "ssv", "password": "123456", "device_name": "PC16"},
    {"hostname": "192.168.0.120", "username": "ssv", "password": "2250028812", "device_name": "PC05"},
    # Add more devices as needed
]


def ssh_connect(device):
    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect using password authentication
        client.connect(
            hostname=device["hostname"],
            username=device["username"],
            password=device["password"]
        )

        # Execute commands or perform actions on the device
        # For example:
        # stdin, stdout, stderr = client.exec_command("ls")
        # print(stdout.read())

        client.close()
        print(f"Connected to {device['device_name']} successfully")
    except Exception as e:
        print(f"Failed to connect to {device['device_name']}: {str(e)}")


if __name__ == '__main__':
    for device in devices:
        ssh_connect(device)

