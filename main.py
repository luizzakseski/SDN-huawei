import paramiko
from paramiko_expect import SSHClientInteraction
from os import system


def vlan1() {
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

}


def lldp_enable(){
    system('cls')


    ip =
    oltname =

    usuario =
    senha =

    prompt = oltname + '>'

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=usuario, password=senha)

    commands = SSHClientInteraction(ssh, timeout=1, display=True)

    commands.send("\n")
    commands.expect(prompt)

    commands.send("en\n")
    prompt = oltname + '#'
    commands.expect(prompt)

    commands.send("conf\n")
    prompt = oltname + '(config)#'
    commands.expect(prompt)

# MA5608T
# commands.send("lldp enable port 0/2\n\n")
# commands.expect(prompt)

# MA5800-x2
# commands.send("lldp enable port 0/3\n\n")
# commands.expect(prompt)

# olt grande
    commands.send("lldp enable port 0/8\n\n")
    commands.expect(prompt)

    commands.close()
    output = commands.current_output_clean

    print(output)

}

lldp_enable()





