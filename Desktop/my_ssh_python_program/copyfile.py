import tkinter as tk
from tkinter import filedialog
import os
import paramiko

# Define the list of devices
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

def browse_file():
    filename = filedialog.askopenfilename(initialdir="~/Downloads", title="Select File")
    entry_filename.delete(0, tk.END)
    entry_filename.insert(0, filename)

def copy_files():
    local_file = entry_filename.get()

    for device in devices:
        remote_host = device["hostname"]
        remote_user = device["username"]
        remote_password = device["password"]
        remote_directory = f"/home/{remote_user}/Desktop/"

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            ssh.connect(remote_host, username=remote_user, password=remote_password)

            sftp = ssh.open_sftp()

            local_file_path = os.path.expanduser(local_file)
            remote_file_path = os.path.join(remote_directory, os.path.basename(local_file))

            sftp.put(local_file_path, remote_file_path)

            result_label.config(text=f"File '{os.path.basename(local_file)}' copied to {device['device_name']}'s Desktop.")

            sftp.close()
            ssh.close()
        except paramiko.AuthenticationException:
            result_label.config(text=f"Failed to authenticate with {device['device_name']} at {remote_host}.")
        except paramiko.SSHException as e:
            result_label.config(text=f"SSH Error with {device['device_name']} at {remote_host}: {str(e)}")
        except Exception as e:
            result_label.config(text=f"Error with {device['device_name']} at {remote_host}: {str(e)}")

# Create the main window
window = tk.Tk()
window.title("File Copy Tool")

# Create a label and entry for the filename
filename_label = tk.Label(window, text="Select File:")
filename_label.pack(pady=10)

entry_filename = tk.Entry(window, width=40)
entry_filename.pack(pady=10)

browse_button = tk.Button(window, text="Browse", command=browse_file)
browse_button.pack(pady=10)

# Create a button to copy files
copy_button = tk.Button(window, text="Copy Files", command=copy_files)
copy_button.pack(pady=10)

# Display the result label
result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Start the GUI event loop
window.mainloop()
