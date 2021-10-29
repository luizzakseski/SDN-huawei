import paramiko
from paramiko_expect import SSHClientInteraction
from os import system
import config
import switch


def vlan1():
    # this function verify if the switch has mac address in vlan1 and then print the output
    comm.expect(prompt)
    comm.send("display mac-address vlan 1")
    comm.expect(prompt)
    output = comm.current_output_clean
    print(prompt)
    print("MACs = ", output.split("Total items displayed =", 1)[1])
    comm.close()


if __name__ == '__main__':
    login = config.login
    password = config.password
    switchdata = switch.data
    for ip, prompt in switchdata:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=login, password=password)
        comm = SSHClientInteraction(ssh, timeout=1, display=False)
        vlan1()
    else:
        print("loop finished")
