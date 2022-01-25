import paramiko
from paramiko_expect import SSHClientInteraction
import oltpass
import sys

def hostname(comm,prompt):
    # this function change the hostname of the olt
    comm.expect(prompt)
    hostname = input("Digite o Hostname da olt")
    comm.send("sysname %s" % hostname)
    prompthn=("%s#" % hostname)
    comm.expect(prompthn)
    print("hostname configurado")


def boardenable(comm, prompt):
    # this function enable boards and ont auto find
    comm.send("board confirm 0")
    comm.expect(prompt)
    print("board enabled !!!")
    # board1
    comm.send("interface gpon 0/0")
    comm.expect("MA5608T\(config\-if\-gpon\-0\/0\)\#")
    # pon loop
    for pon in range(16):
        comm.send("port %s ont-auto-find enable" % str(pon))
        comm.expect("MA5608T\(config\-if\-gpon\-0\/0\)\#")
    comm.send("quit")
    comm.expect(prompt)
    # board2
    comm.send("interface gpon 0/1")
    comm.expect("MA5608T\(config\-if\-gpon\-0\/1\)\#")
    # pon loop
    for pon in range(16):
        comm.send("port %s ont-auto-find enable" % str(pon))
        comm.expect("MA5608T\(config\-if\-gpon\-0\/1\)\#")
    comm.send("quit")
    print("Pons configured to autofind onts !!!")

    return()

def boardenableX2(comm, prompt):
    # this function enable boards and ont auto find
    comm.send("board confirm 0")
    comm.expect(prompt)
    print("board enabled !!!")
    # board1
    comm.send("interface gpon 0/1")
    comm.expect("MA5800-X2\(config\-if\-gpon\-0\/1\)\#")
    # pon loop
    for pon in range(16):
        comm.send("port %s ont-auto-find enable" % str(pon))
        comm.expect("MA5800-X2\(config\-if\-gpon\-0\/1\)\#")
    comm.send("quit")
    comm.expect(prompt)
    # board2
    comm.send("interface gpon 0/2")
    comm.expect("MA5800-X2\(config\-if\-gpon\-0\/2\)\#")
    # pon loop
    for pon in range(16):
        comm.send("port %s ont-auto-find enable" % str(pon))
        comm.expect("MA5800-X2\(config\-if\-gpon\-0\/2\)\#")
    comm.send("quit")
    print("Pons configured to autofind onts !!!")
    return()


def confaaa(comm, prompt):
    # this function configure the aaa
    user1 = input("Digite o primeiro usuario <6-15> ")
    pass1 = input("Digite a senha do primeiro usuario <6-15> ")
    comm.send("")
    comm.expect(prompt)
    comm.send("terminal user name")
    comm.expect("  User Name\(length\<6,15\>\)\:")
    comm.send("%s" % user1)
    comm.expect("  User Password\(length\<6,15\>\)\:")
    comm.send("%s" % pass1)
    comm.expect("  Confirm Password\(length\<6,15\>\)\:")
    comm.send("%s" % pass1)
    comm.expect("  User profile name\(\<=15 chars\)\[root\]\:")
    comm.send("root")
    comm.expect("User's Level\:")
    comm.send("2")
    comm.expect("  Permitted Reenter Number\(0--4\)\:")
    comm.send("4")
    comm.expect("  User's Appended Info\(\<=30 chars\)\:")
    comm.send("\n")
    comm.expect("  Repeat this operation? \(y\/n\)\[n\]:")
    comm.send("n")
    comm.expect(prompt)
    user2 = input("Digite o segundo usuario <6-15> ")
    pass2 = input("Digite a senha do segundo usuario <6-15> ")
    comm.send("")
    comm.expect(prompt)
    comm.send("terminal user name")
    comm.expect("  User Name\(length\<6,15\>\)\:")
    comm.send("%s" % user2)
    comm.expect("  User Password\(length\<6,15\>\)\:")
    comm.send("%s" % pass2)
    comm.expect("  Confirm Password\(length\<6,15\>\)\:")
    comm.send("%s" % pass2)
    comm.expect("  User profile name\(\<=15 chars\)\[root\]\:")
    comm.send("root")
    comm.expect("User's Level\:")
    comm.send("2")
    comm.expect("  Permitted Reenter Number\(0--4\)\:")
    comm.send("4")
    comm.expect("  User's Appended Info\(\<=30 chars\)\:")
    comm.send("\n")
    comm.expect("  Repeat this operation? \(y\/n\)\[n\]:")
    comm.send("n")
    comm.expect(prompt)
    testrsa = input("Digite y to configure RSA")
    if testrsa == "y":
        comm.send("rsa local-key-pair create")
        comm.expect("Confirm to replace them? Please select \(y\/n\)\[n\]:")
        comm.send("y \n")
        comm.expect(prompt, TIMEOUT=30)
    return ()

def confvlan(comm, prompt):
    #configure vlans
    vlanbase = [1400, 1410, 1420, 1498, 1499, 300, 399]
    comm.send("\n")
    comm.expect(prompt)
    for vlan in vlanbase:
        comm.send("vlan %s smart " % vlan)
        comm.send("port vlan %s 0/2 0 " % vlan)
        comm.expect(prompt)
    #set uplinks at 10GB
    test10g = input("digite y para configurar as portas em 10g: ")
    if test10g == "y":
        comm.send("interface mcu 0/2 ")
        comm.send("auto-neg 0 disable")
        comm.send("auto-neg 0 disable")
        comm.send("speed 2 10000 ")
        comm.send("speed 3 10000 ")
        comm.send("quit")
        comm.expect(prompt)
    #configure port channel between 2 interfaces
    testlag = input("press y to configure lag between 10g interfaces: ")
    if testlag == "y":
        comm.send("link-aggregation 0/2 2 0/2 3 egress-ingress workmode lacp-static ")
        comm.expect(prompt)
    return()

def confvlanX2(comm, prompt):
    #configure vlans
    vlanbase = [1400, 1410, 1420, 1498, 1499, 300, 399]
    comm.send("\n")
    comm.expect(prompt)
    for vlan in vlanbase:
        comm.send("vlan %s smart " % vlan)
        comm.send("port vlan %s 0/3 0 " % vlan)
        comm.expect(prompt)
    #set uplinks at 10GB
    test10g = input("digite y para configurar as portas em 10g")
    if test10g == "y":
        comm.send("interface mpu 0/3 ")
        comm.send("auto-neg 0 disable")
        comm.send("auto-neg 0 disable")
        comm.send("speed 0 10000 ")
        comm.send("speed 1 10000 ")
        comm.send("quit")
        comm.expect(prompt)
    #configure port channel between 2 interfaces
    testlag = input("\npress y to configure lag between 10g interfaces")
    if testlag == "y":
        comm.send("link-aggregation 0/3 0 0/3 1 egress-ingress workmode lacp-static ")
        comm.expect(prompt)
    return()


def confprofile(comm, prompt, promptEx):
    prof_ftth = input("aperte y para criar o profile FTTH")
    if prof_ftth == 'y':
        comm.expect(prompt)
        comm.send("dba-profile add profile-name DBA_FTTH type3 assure 5120 max 1024000 ")
        comm.expect(prompt)
        comm.send("ont-lineprofile gpon profile-id 1 profile-name FTTH")
        promptline = ("%s\(config-gpon-lineprofile-1\)\#" % promptEx)
        comm.expect(promptline)
        comm.send("tcont 4 dba-profile-name DBA_FTTH")
        comm.expect(promptline)
        #creat GEM
        comm.send("gem add 11 eth tcont 4\n")
        comm.expect(promptline)
        comm.send("gem add 12 eth tcont 4 \n")
        comm.expect(promptline)
        comm.send("gem add 13 eth tcont 4 \n")
        comm.expect(promptline)
        comm.send("gem add 14 eth tcont 4\n ")
        comm.expect(promptline)
        #map GEM to VLAN
        comm.send("gem mapping 11 0 vlan 1499\n ")
        comm.expect(promptline)
        comm.send("gem mapping 12 0 vlan 1481\n ")
        comm.expect(promptline)
        comm.send("gem mapping 13 0 vlan 1482\n ")
        comm.expect(promptline)
        comm.send("gem mapping 14 0 vlan 1480\n ")
        comm.expect(promptline)
        comm.send("commit")
        comm.expect(promptline)
        comm.send("quit")
        comm.expect(prompt)
    prof_ded = input("digite y para criar o profile dedicados")
    if prof_ded == "y":
        comm.expect(prompt)
        comm.send("dba-profile add profile-name DBA_FTTH type3 assure 5120 max 1024000 \n\n")
        comm.expect(prompt)
        comm.send("ont-lineprofile gpon profile-id 2 profile-name DEDICADOS \n \n")
        promptline2 = ("%s\(config-gpon-lineprofile-2\)\#" %promptEx)
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
        promptsrv = ("%s(config-gpon-srvprofile-1)#" % promptEx)
        comm.expect(promptsrv)
        comm.send("ont-port eth adaptive pots adaptive\n\n ")
        comm.expect(promptsrv)
        comm.send("commit\n\n ")
        comm.expect(promptsrv)
        comm.send("quit")
        comm.expect(prompt)
    prof_tr069 =  input("Digite Y para criar o profile srv")
    if prof_tr069 == "y":
        comm.send("ont tr069-server-profile add profile-name %s url %s \n\n" % (oltpass.tr069name, oltpass.tr069url))
        comm.expect(prompt)
        comm.send("ont tr069-server-profile modify profile-name %s auth-realm auth\n\n" % oltpass.tr069name)
        comm.expect(prompt)
        comm.send("ont tr069-server-profile modify profile-name %s user %s %s\n\n" % (oltpass.tr069name,oltpass.tr069user,oltpass.tr069name))
        comm.expect(prompt)
    prof_tr069 = input("Digite Y para criar o profile SIP")
    if prof_tr069 == "y":
        comm.send("ont-sipagent-profile add profile-name %s proxy-server %s proxy-server-port %s server-type 1\n\n"
                  % (oltpass.SIPname,oltpass.SIPserver,oltpass.SIPport))
        comm.expect(prompt)
        comm.send("ont-sipagent-profile modify profile-name %s registration server-uri %s server-port %s\n\n"
                  %(oltpass.SIPname,oltpass.SIPserver,oltpass.SIPport))
        comm.expect(prompt)
    print("Finalizada configuração dos profiles")
    return()


def confbasic(comm,prompt,promptEx ):
    mgmttest = input("Digite y para configurar o IP de gerencia")
    if mgmttest == 'y':
        mgmt_vlan = input("Digite a VLAN de mgmt")
        mgmt_ip = input("digite o IP da olt")
        mgmt_mask = input("Digite a mascara de rede")
        mgmt_gw = input("Digite o Gateway")
        comm.expect(prompt)
        comm.send("interface vlanif %s"% mgmt_vlan)
        promptif = ("%s(config-if-vlanif%s)" % (promptEx, mgmt_vlan))
        comm.expect(promptif)
        comm.send("ip address %s %s\n" % (mgmt_ip, mgmt_mask))
        comm.expect(promptif)
        comm.send("quit")
        comm.expect(prompt)
        comm.send("ip route-static 0.0.0.0 0.0.0.0 %s\n\n" % mgmt_gw)
        print("Ip e rota default configurados")
    dnstest = input("Digite y para configurar o DNS")
    if dnstest == 'y':
        dns1 = input("digite o servidor de dns primario")
        dns2 = input("digite o servidor de dns secundario")
        comm.send("\n")
        comm.expect(prompt)
        comm.send("dns resolve\n\n")
        comm.expect(prompt)
        comm.send("dns server %s\n\n" % dns1)
        comm.expect(prompt)
        comm.send("dns server %s\n\n" % dns2)
        comm.expect(prompt)
        print("DNS configurado")
    snmptest = input("Digite y para configurar o SNMP")
    if snmptest == 'y':
        comm.expect(prompt)
        snmp_community = input("Digite a community SNMP")
        comm.send("snmp-agent community read %s \n\n" % snmp_community)
        comm.expect(prompt)
        snmp_loc = input("Digite a cidade e he do equipamento ex: TOO-he1")
        comm.send("snmp-agent sys-info location %s\n\n" % snmp_loc)
        comm.expect(prompt)
        comm.send("snmp-agent sys-info version v2c\n\n")
        comm.expect(prompt)
    ntptest = input("Digite y para configurar o NTP")
    if ntptest == 'y':
        comm.send("time time-stamp utc")
        comm.expect(prompt)
        comm.send("timezone GMT- 03:00")
        comm.expect(prompt)
        ntp1 = input("\nEnter first ntp server: ")
        ntp2 = input("\nEnter second ntp server: ")
        comm.send("ntp-service unicast-server %s\n" % ntp1)
        comm.expect(prompt)
        comm.send("ntp-service unicast-server %s\n" % ntp2)
        comm.expect(prompt)
        print("NTP configurado")
    lldptest = input("Digite y para configurar o lldp")
    if lldptest == 'y':
        if promptEx == "MA5800-X2":
            comm.send("lldp enable \n")
            comm.expect(prompt)
            comm.send("lldp enable port 0/3/0\n")
            comm.expect(prompt)
            comm.send("lldp enable port 0/3/1\n")
        elif promptEx == "MA5608T":
            comm.send("lldp enable\n")
            comm.expect(prompt)
            comm.send("lldp enable port 0/2/2\n")
            comm.expect(prompt)
            comm.send("lldp enable port 0/2/3\n")
        print("lldp configurado")
    savetest = input("Digite y para configurar o autosave")
    if savetest == 'y':
        comm.send("autosave interval on\n")
        comm.expect(prompt)
        comm.send("autosave time off\n")
        comm.expect(prompt)
        comm.send("autosave interval 120\n")
        comm.expect(prompt)
        comm.send("autosave interval configuration 120\n")
        comm.expect(prompt)
        comm.send("autosave type all\n")
        comm.expect(prompt)
        print("autosave configurado")
    alarmtest = input("Digite y para configurar o alarme")
    if alarmtest == 'y':
        comm.send('emu add 2 h901vesc 0 25  "H901VESC"\n')
        comm.expect(prompt)
        comm.send("interface emu 2")
        promptemu = ("%s(config-if-emu-0/2)" % promptEx)
        comm.expect(promptemu)
        comm.send('vesc digital 0 available-level low-level name "alm_fan"\n')
        comm.expect(promptemu)
        comm.send('vesc digital 1 available-level low-level name "porta_aberta"\n')
        comm.expect(promptemu)
        comm.send('vesc digital 2 available-level low-level name "desc_bateria"\n')
        comm.expect(promptemu)
        comm.send('vesc digital 3 available-level low-level name "alm_energia"\n')
        comm.expect(promptemu)
        comm.send("quit")
        comm.expect(prompt)
    return()


if __name__ == '__main__':
    print("Bem vindo ao configurador automatizado de OLTs da Certto, configure o ip 10.11.104.1/255.255.255.0 no seu pc")
    model = input("Digite o modelo da OLT\n 1 - MA5608T \n 2 - MA5800-X2\n")
    if model == "1":
        promptu = "MA5608T>"
        prompten = "MA5608T#"
        promptEx = "MA5608T"
        prompt = "MA5608T\(config\)\#"
    elif model == "2":
        promptu = "MA5800-X2>"
        prompten = "MA5800-X2#"
        promptEx = "MA5800-X2"
        prompt = "MA5800-X2\(config\)\#"
    else:
        print("error")
        sys.exit()
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # config default olt huawei
    ssh.connect("10.11.104.2", username=oltpass.oltuser, password=oltpass.oltpass)
    with SSHClientInteraction(ssh, timeout=5, display=True) as comm:
        comm.expect(promptu)
        comm.send("en")
        comm.expect(prompten)
        comm.send("config")
        comm.expect(prompt)
        if comm.last_match == prompt:
            print("worked")
    # initial configuration
        testboard = input("Habilitar as boards? y/n ")
        if testboard == "y" and model =="1":
            boardenable(comm, prompt)
        elif testboard == "y" and model == "2":
            boardenableX2(comm, prompt)
        testaaa = input("Configurar usuarios e senhas? y/n ")
        if testaaa == "y" :
            confaaa(comm, prompt)
        testvlan = input("Configurar VLAN?  y/n ")
        if testvlan == "y" and model == "1":
            confvlan(comm, prompt)
        elif testvlan == "y" and model == "2":
            confvlanX2(comm, prompt)
        testprofile = input("Configurar profile de ftth?  y/n")
        if testprofile == "y":
            confprofile(comm, prompt, promptEx)
        testbasic = input("Configurar IP, DNS , SNMP e NTP?  y/n")
        if testbasic == "y":
            confbasic(comm, prompt, promptEx)
    # configure hostname
        testhostname = input("Configurar hostname? (fazer por ultimo)  y/n")
        if testhostname == "y":
            hostname(comm, prompt)
        comm.close()
    print("****************************configuração finalizada*********************************")