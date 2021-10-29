import paramiko
from paramiko import SSHClient
import paramiko_expect
from paramiko_expect import SSHClientInteraction
from os import system
import config
import switch


class SSH:
    def __init__(self):
        self.ssh = SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(ip, username=config.login, password=config.password)

    def exec_cmd(self, cmd):
        print(ip)
        print(prompt)
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        if stderr.channel.recv_exit_status() != 0:
            print(stderr.read())
        else:
            print(stdout.read())


if __name__ == '__main__':
    switchdata = switch.data
    for ip, prompt in switchdata:
        ssh = SSH()
        ssh.exec_cmd("display mac-address vlan 1\n")

