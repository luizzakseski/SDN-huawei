import paramiko
from paramiko_expect import SSHClientInteraction
import oltpass


def hostname():
    # this function change the hostname of the olt
    prompt = "test"
    comm.expect(prompt)
    hostname = input("Digite o Hostename da olt")
    comm.send("sysname", hostname)
    prompthn=(hostname,"#")
    comm.expect(prompthn)
    output = comm.current_output_clean
    print("hostname configurado")
    print (output)


def boardenable(comm, prompt):
    # this function enable boards and ont auto find
    comm.expect(prompt)
    comm.send("board confirm 0\n\n")
    comm.expect(prompt)
    print("board enabled !!!")
    # board1
    comm.send("interface gpon 0/1\n")
    comm.expect("MA5800-X2(config-if-gpon-0/1)#")
    # pon loop
    for pon in range(16):
        comm.send("port", pon, "ont-auto-find enable\n\n")
    comm.expect("MA5800-X2(config-if-gpon-0/1)#")
    comm.send("quit\n")
    comm.expect(prompt)
    # board2
    comm.send("interface gpon 0/2\n")
    comm.expect("MA5800-X2(config-if-gpon-0/2)#")
    # pon loop
    for pon in range(16):
        comm.send("port", pon, "ont-auto-find enable\n\n")
    comm.expect("MA5800-X2(config-if-gpon-0/2)#")
    comm.send("quit\n")
    print("Pons configured to autofind onts !!!")
    return()


def confaaa(comm, prompt):
    # this function configure the aaa
    user1 = input("Digite o primeiro usuario")
    pass1 = input("Digite a senha do primeiro usuario")
    comm.expect(prompt)
    comm.send("terminal user name\n")
    comm.expect("User Name(length<6,15>):")
    comm.send(user1, "\n")
    comm.expect("User Password(length<6,15>):")
    comm.send(pass1, "\n")
    comm.expect("Confirm Password(length<6,15>):")
    comm.send(pass1, "\n")
    comm.expect("User's Level:")
    comm.send("3\n")
    comm.expect("Permitted Reenter Number(0--4):")
    comm.send("4\n")
    comm.expect("User's Appended Info(<=30 chars):")
    comm.send("\n")
    comm.expect("Repeat this operation? (y/n)[n]:")
    comm.send("n\n")
    comm.expect(prompt)
    user2 = input("Digite o segundo usuario")
    pass2 = input("Digite a senha do segundo usuario")
    comm.send("terminal user name\n")
    comm.expect("User Name(length<6,15>):")
    comm.send(user2, "\n")
    comm.expect("User Password(length<6,15>):")
    comm.send(pass2, "\n")
    comm.expect("Confirm Password(length<6,15>):")
    comm.send(pass2, "\n")
    comm.expect("User's Level:")
    comm.send("3\n")
    comm.expect("Permitted Reenter Number(0--4):")
    comm.send("4\n")
    comm.expect("User's Appended Info(<=30 chars):")
    comm.send("\n")
    comm.expect("Repeat this operation? (y/n)[n]:")
    comm.send("n\n")
    comm.expect(prompt)
    comm.send("rsa local-key-pair create \n")
    comm.expect(prompt)
    comm.send("y \n")
    comm.expect(prompt)
    return ()

def confvlan(comm, prompt):
    #configure vlans
    vlanbase = [1400,1410,1420,1498,1499,300,399]
    for vlan in vlanbase:
        comm.expect(prompt)
        comm.send("vlan",vlan, "smart \n\n")
        comm.send("port vlan", vlan, "0/3 0  \n\n")
    comm.expect(prompt)
    #set uplinks at 10GB
    comm.send("interface mpu 0/3 \n\n")
    comm.send("auto-neg 0 disable \n\n")
    comm.send("auto-neg 0 disable \n\n")
    comm.send("speed 0 10000 \n\n")
    comm.send("speed 1 10000 \n\n")
    comm.send("quit \n")
    comm.expect(prompt)
    #configure port channel between 2 interfaces
    comm.send("link-aggregation 0/3 0 0/3 1 egress-ingress workmode lacp-static \n\n")
    comm.expect(prompt)
    return()


def confprofile(comm, prompt):
    prof_ftth = input("aperte y para criar o profile FTTH")
    if prof_ftth == 'y':
        comm.expect(prompt)
        comm.send("dba-profile add profile-name DBA_FTTH type3 assure 5120 max 1024000 \n\n")
        comm.expect(prompt)
        comm.send("ont-lineprofile gpon profile-id 1 profile-name FTTH \n \n")
        promptline = "MA5800-X2(config-gpon-lineprofile-1)#"
        comm.expect(promptline)
        comm.send("tcont 4 dba-profile-name DBA_FTTH\n \n")
        comm.expect(promptline)
        #creat GEM
        comm.send("gem add 11 eth tcont 4 \n \n")
        comm.expect(promptline)
        comm.send("gem add 12 eth tcont 4 \n \n")
        comm.expect(promptline)
        comm.send("gem add 13 eth tcont 4 \n \n")
        comm.expect(promptline)
        comm.send("gem add 14 eth tcont 4 \n \n")
        comm.expect(promptline)
        #map GEM to VLAN
        comm.send("gem mapping 11 0 vlan 1499 \n \n")
        comm.expect(promptline)
        comm.send("gem mapping 12 0 vlan 1481  \n \n")
        comm.expect(promptline)
        comm.send("gem mapping 13 0 vlan 1482  \n \n")
        comm.expect(promptline)
        comm.send("gem mapping 14 0 vlan 1480 \n \n")
        comm.expect(promptline)
        comm.send("commit\n \n")
        comm.expect(promptline)
        comm.send("quit\n\n")
        comm.expect(prompt)
    prof_ded = input("digite y para criar o profile dedicados")
    if prof_ded == "y":
        comm.expect(prompt)
        comm.send("dba-profile add profile-name DBA_FTTH type3 assure 5120 max 1024000 \n\n")
        comm.expect(prompt)
        comm.send("ont-lineprofile gpon profile-id 2 profile-name DEDICADOS \n \n")
        promptline2 = "MA5800-X2(config-gpon-lineprofile-2)#"
        comm.expect(promptline2)
        comm.send("tcont 4 dba-profile-name DBA_FTTH\n \n")
        comm.expect(promptline2)
        comm.send("gem add 95 eth tcont 4 \n \n")
        comm.expect(promptline2)
        comm.send("gem add 94 eth tcont 4 \n \n")
        comm.expect(promptline2)
        comm.send("gem mapping 95 0 vlan 300\n \n")
        comm.expect(promptline2)
        comm.send("gem mapping 94 0 vlan 399 \n \n")
        comm.expect(promptline2)
        comm.send("commit\n \n")
        comm.expect(promptline2)
        comm.send("quit\n\n")
        comm.expect(prompt)
    # create srv profile
    prof_srv = input("Digite y para criar o profile srv")
    if prof_srv == 'y':
        comm.send("ont-srvprofile gpon profile-name FTTH\n\n")
        promptsrv = "MA5800-X2(config-gpon-srvprofile-1)#"
        comm.expect(promptsrv)
        comm.send("ont-port eth adaptive pots adaptive\n\n ")
        comm.expect(promptsrv)
        comm.send("commit\n\n ")
        comm.expect(promptsrv)
        comm.send("quit\n\n")
        comm.expect(prompt)
    prof_tr069 =  input("Digite Y para criar o profile srv")
    if prof_tr069 == "y":
        comm.send("ont tr069-server-profile add profile-name ", oltpass.tr069name, " url ", oltpass.tr069url,"\n\n")
        comm.expect(prompt)
        comm.send("ont tr069-server-profile modify profile-name ",oltpass.tr069name," auth-realm auth\n\n")
        comm.expect(prompt)
        comm.send("ont tr069-server-profile modify profile-name ",oltpass.tr069name," user ",oltpass.tr069user," ",oltpass.tr069name,"\n\n")
        comm.expect(prompt)
    prof_tr069 = input("Digite Y para criar o profile SIP")
    if prof_tr069 == "y":
        comm.send("ont-sipagent-profile add profile-name ",oltpass.SIPname," proxy-server ",
                  oltpass.SIPserver," proxy-server-port ",oltpass.SIPport," server-type 1\n\n")
        comm.expect(prompt)
        comm.send("ont-sipagent-profile modify profile-name ", oltpass.SIPname," registration server-uri ",
                  oltpass.SIPserver," server-port ", oltpass.SIPport, "\n\n")
        comm.expect(prompt)
    print("Finalizada configuração dos profiles")
    return()


def confbasic(comm,prompt):
    mgmttest = input("Digite y para configurar o IP de gerencia")
    if mgmttest == 'y':
        mgmt_vlan = input("Digite a VLAN de mgmt")
        mgmt_ip = input("digite o IP da olt")
        mgmt_mask = input("Digite a mascara de rede")
        mgmt_gw = input("Digite o Gateway")
        comm.expect(prompt)
        comm.send("interface vlanif ",mgmt_vlan)
        promptif = ("MA5800-X2(config-if-vlanif", mgmt_vlan, ")#\n\n")
        comm.expect(promptif)
        comm.send("ip address ",mgmt_ip, " ", mgmt_mask, "\n\n")
        comm.expect(promptif)
        comm.send("quit\n\n")
        comm.expect(prompt)
        comm.send("ip route-static 0.0.0.0 0.0.0.0 ",mgmt_gw, "\n\n")
    dnstest = input("Digite y para configurar o DNS")
    if dnstest == 'y':
        dns1 = input("digite o servidor de dns primario")
        dns2 = input("digite o servidor de dns secundario")
        comm.expect(prompt)
        comm.send("dns resolve\n\n")
        comm.expect(prompt)
        comm.send("dns server ",dns1,"\n\n")
        comm.expect(prompt)
        comm.send("dns server ",dns2,"\n\n")
        comm.expect(prompt)



if __name__ == '__main__':
    print("Bem vindo ao configurador automatizado de OLTs da Certto, configure o ip 10.11.104.1/255.255.255.0 no seu pc")
    promptu = "MA5800-X2>"
    prompten = "MA5800-X2#"
    prompt = "MA5800-X2(config)#"
    input("Entre qualquer tecla para iniciar o processo")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # config default olt huawei
    ssh.connect("10.11.104.2", username="root", password="admin123")
    comm = SSHClientInteraction(ssh, timeout=1, display=False)
    comm.expect(promptu)
    comm.send("en")
    comm.expect(prompten)
    comm.send("config")
    # initial configuration
    testboard = input("Habilitar as boards? y/n")
    if testboard == "y":
        boardenable(comm, prompt)
    testaaa = input("Configurar usuarios e senhas? y/n")
    if testaaa == "y":
        confaaa(comm, prompt)
    testvlan = input("Configurar VLAN?  y/n")
    if testvlan == "y":
        confvlan(comm, prompt)
    testprofile = input("Configurar profile de ftth?  y/n")
    if testprofile == "y":
        confprofile(comm, prompt)
    testbasic = input("Configurar IP, DNS , SNMP e NTP?  y/n")
    if testbasic == "y":
        confbasic(comm, prompt)


    # configure hostname
    # hostname()


























