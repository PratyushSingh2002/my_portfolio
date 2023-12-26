import paramiko

# Define a list of SSH devices
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

# Display the list of devices and let the user select one
print("Select an SSH device:")
for index, device in enumerate(devices):
    print(f"{index + 1}. {device['device_name']} ({device['hostname']})")

selected_index = int(input("Enter the device number: ")) - 1

# Get the selected device's information
selected_device = devices[selected_index]

# Get the command from the user
command = input(f"Enter the command to execute on {selected_device['device_name']} ({selected_device['hostname']}): ")

try:
    # Create an SSH client
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the selected SSH device
    ssh_client.connect(
        selected_device["hostname"],
        username=selected_device["username"],
        password=selected_device["password"]
    )

    # Execute the command and get the output
    stdin, stdout, stderr = ssh_client.exec_command(command)

    # Print the output along with the device name
    output = stdout.read().decode()
    print(f"Output from {selected_device['device_name']} ({selected_device['hostname']}):\n{output}")

    # Close the SSH connection
    ssh_client.close()

except Exception as e:
    print(f"Failed to execute the command on {selected_device['device_name']} ({selected_device['hostname']}): {str(e)}")
