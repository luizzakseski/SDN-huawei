import paramiko
from paramiko_expect import SSHClientInteraction
from os import system
import config
import switch


def vlan1():
    # this function verify if the switch has mac address in vlan1 and then print the output
    if(ip=='172.16.250.1'):
        comm.send("N")
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
    switch_data = switch.data
    for ip, prompt in switch_data:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=login, password=password)
        comm = SSHClientInteraction(ssh, timeout=1, display=False)
        # verify vlan1
        vlan1()
    else:
        print("loop finished")
