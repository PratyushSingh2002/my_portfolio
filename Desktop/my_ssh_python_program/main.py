import subprocess
import tkinter as tk
from tkinter import simpledialog

def ssh_status():
    subprocess.run(["/usr/bin/python3", "ssh_status.py"])

def enter_command():
    subprocess.run(["/usr/bin/python3", "single_command.py"])

def select_device():
    subprocess.run(["/usr/bin/python3", "select_ssh_device.py"])

def copy_files():
    subprocess.run(["/usr/bin/python3", "copyfile.py"])

class SSHToolApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SSH Tool")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Select an option:").pack()

        options = [
            ("SSH status", self.ssh_status),
            ("Enter Command For Devices", self.enter_command),
            ("Select Device", self.select_device),
            ("Copy Files to all system", self.copy_files),
            ("Exit", self.quit)
        ]

        for text, command in options:
            tk.Button(self, text=text, command=command).pack()

    def ssh_status(self):
        subprocess.run(["/usr/bin/python3", "ssh_status.py"])

    def enter_command(self):
        subprocess.run(["/usr/bin/python3", "single_command.py"])

    def select_device(self):
        subprocess.run(["/usr/bin/python3", "select_ssh_device.py"])

    def copy_files(self):
        subprocess.run(["/usr/bin/python3", "copyfile.py"])

if __name__ == "__main__":
    app = SSHToolApp()
    app.mainloop()
