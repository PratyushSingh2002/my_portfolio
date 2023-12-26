import paramiko

devices = [
    {"hostname": "192.168.0.107", "username": "ssv", "password": "123456", "device_name": "PC01"},
    {"hostname": "192.168.0.117", "username": "ssv", "password": "123456", "device_name": "PC03"},
    {"hostname": "192.168.0.123", "username": "ssv", "password": "123456", "device_name": "PC04"},
    {"hostname": "192.168.0.125", "username": "ssv", "password": "123456", "device_name": "PC09"},
    {"hostname": "192.168.0.124", "username": "ssv", "password": "123456", "device_name": "PC10"},
    {"hostname": "192.168.0.119", "username": "ssv", "password": "123456", "device_name": "PC08"},
    {"hostname": "192.168.0.130", "username": "ssv", "password": "123456", "device_name": "PC16"},
    {"hostname": "192.168.0.120", "username": "ssv", "password": "2250028812", "device_name": "PC05"},
]


def send_command(device_info, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(
            device_info['hostname'],
            username=device_info['username'],
            password=device_info['password']
        )

        # Send the user-specified command and capture the output
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode('utf-8')

        print(f"Output from {device_info['device_name']} ({device_info['hostname']}):\n{output}")

    except Exception as e:
        print(f"Failed to connect to {device_info['device_name']} ({device_info['hostname']}): {str(e)}")

    finally:
        ssh.close()

while True:
    user_command = input("Enter the command to execute (or 'no' to quit): ")
    
    if user_command.lower() == 'no':
        break

    # Iterate through the list of devices and send the user-specified command
    for device in devices:
        send_command(device, user_command)
