import paramiko
import paramiko_expect
from paramiko_expect import SSHClientInteraction
from os import system
import config
import switch


def vlan1():
    comm.expect(switch.prompt)
    comm.send("N\n")
    comm.send("display mac-address vlan 1\n")
    comm.expect(switch.prompt)
    comm.close()
    output = comm.current_output_clean
    print(output)



login = config.login
password = config.password
ip = switch.ip
print(ip)
system('cls')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip, username=login, password=password)
comm = SSHClientInteraction(ssh, timeout=1, display=True)


vlan1()

