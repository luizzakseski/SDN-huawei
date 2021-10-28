import paramiko
from paramiko_expect import SSHClientInteraction
from os import system

system('cls')

ip =
usuario =
senha =
prompt =

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip, username=usuario, password=senha)


commands = SSHClientInteraction(ssh, timeout=1, display=True)


commands.expect(prompt)
commands.send("N\n")

commands.expect(prompt)
commands.send("display mac-address vlan 1\n")

commands.expect(prompt)

commands.close()
output = commands.current_output_clean

print (output)





