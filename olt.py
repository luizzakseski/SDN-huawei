import paramiko
from paramiko_expect import SSHClientInteraction
from os import system


def hostname():
    # this function change the hostname of the olt
    prompt = ""
    comm.expect(prompt)
    comm.send("display mac-address vlan 1")
    comm.expect(prompt)
    output = comm.current_output_clean
    print("MACs = ", output.split("Total items displayed =", 1)[1])

def boardenable(comm,prompt):
    # this function enable boards and ont auto find
    comm.expect(prompt)
    comm.send("board confirm 0/1\n\n")
    comm.send("board confirm 0/2\n\n")
    comm.expect(prompt)
    print("board enabled !!!")
    #board1
    comm.send("interface gpon 0/1\n")
    comm.expect("MA5800-X2(config-if-gpon-0/1)#")
    for pon in range(16):
        comm.send("port", pon, "ont-auto-find enable\n\n")
    comm.expect("MA5800-X2(config-if-gpon-0/1)#")
    comm.send("quit\n")
    comm.expect(prompt)
    #board2
    comm.send("interface gpon 0/2\n")
    comm.expect("MA5800-X2(config-if-gpon-0/2)#")
    for pon in range(16):
        comm.send("port", pon, "ont-auto-find enable\n\n")
    comm.expect("MA5800-X2(config-if-gpon-0/2)#")
    comm.send("quit\n")
    return()

def confaaa(comm,prompt):
    # this function configure the aaa
    comm.expect(prompt)
    comm.send("board confirm 0/1\n\n")
    comm.send("board confirm 0/2\n\n")
    comm.expect(prompt)
    print("board enabled")
    comm.send("interface gpon 0/1\n")
    return ()



if __name__ == '__main__':
    print("Bem Vindo ao configurador automatizado de OLTs da Certto, configure o ip 10.11.104.1/255.255.255.0 no seu pc")
    promptu = "MA5800-X2>"
    prompten = "MA5800-X2#"
    prompt = "MA5800-X2(config)#"
    input("Entre qualquer tecla para iniciar o processo")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #config default olt huawei
    ssh.connect("10.11.104.2", username="root", password="admin123")
    comm = SSHClientInteraction(ssh, timeout=1, display=False)
    comm.expect(promptu)
    comm.send("en")
    comm.expect(prompten)
    comm.send("config")
    #initial configuration
    testboard = input("Habilitar as boards? y/n")
    if testboard ==" y" :
        boardenable(comm,prompt)
    testaaa= input("Configurar usuarios e senhas? y/n")
    if testaaa == "y" :
        confaaa(comm,prompt)



    # configure hostname
    #hostname()


























