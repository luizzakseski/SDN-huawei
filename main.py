import paramiko
from paramiko_expect import SSHClientInteraction
from os import system
import config
import switch


def vlan1():
    # this function verify if the switch has mac address in vlan1 and then print the output
    comm.expect(prompt)
    comm.send("N\n")
    comm.send("display mac-address vlan 1\n")
    comm.expect(prompt)
    comm.close()


if __name__ == '__main__':
    login = config.login
    password = config.password
    switchdata = switch.data
    for ip, prompt in switchdata:
        system('cls')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=login, password=password)
        comm = SSHClientInteraction(ssh, timeout=1, display=True)
        vlan1()
