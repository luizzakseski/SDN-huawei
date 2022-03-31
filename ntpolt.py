import paramiko
from paramiko_expect import SSHClientInteraction
import oltpass
import oltnames


def update_ntp():
    pass

def verify_ntp(ssh,oltprompt):
        with SSHClientInteraction(ssh, timeout=5, display=False) as comm:
            comm.expect(oltprompt+'>')
            comm.send("en")
            comm.expect(oltprompt+'#')
            comm.send("display timezone")
            comm.send("\n")       
            comm.expect(oltprompt+'#')
            cmd_output_uname = comm.current_output_clean            
            comm.close()
            print(cmd_output_uname)



def connect_olt(ip):    
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # config default olt huawei
        ssh.connect(ip, username=oltpass.oltuser, password=oltpass.oltpass)
        return ssh


if __name__ == '__main__':
    data = oltnames.oltdata
    for oltprompt,ip in data.items():
        print("------------------------------------ %s ------------------------------------" %oltprompt)
        ssh = connect_olt(ip)
        verify_ntp(ssh,oltprompt)
    
        

