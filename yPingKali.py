import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import tempfile
import ctypes  # An included library with Python install.
import time 

w = tempfile.NamedTemporaryFile()


def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]
    
    #return subprocess.call(command) == 0
    return subprocess.call(command, shell=True, stdout=tempfile.NamedTemporaryFile(), stderr=subprocess.STDOUT, bufsize=0) == 0
    




while True:
    time.sleep(1)
    if ping("8.8.8.8"):
        print("Erisim var.")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Kali'ye erişim yok", "VPN Test", 1)