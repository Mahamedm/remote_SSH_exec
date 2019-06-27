import re
import paramiko as pm

# ui = str(input('nmap_ip: '))
# command = f'nmap -sV -v {ui}'


class ssh:
    @staticmethod
    def routine(ip, uname, passwd, port):
        try:
            s = pm.SSHClient()
            s.set_missing_host_key_policy(pm.AutoAddPolicy)
            s.connect(ip, username=uname, password=passwd, port=port)
            print(f'connected to {ip}')
            while 1:
                ui = str(input(">> "))
                stdin, stdout, stderr = s.exec_command(ui)
                res = stdout.readlines()
                filt = re.findall(r"'.*?\'", str(res))
                print(filt)
        except KeyboardInterrupt:
            print("connection closed!")


s = ssh()
ip, uname, passwd, port = input("Ip: "), input("Username: "), input("Password: "), input("Port: ")
s.routine(ip=ip, uname=uname, passwd=passwd, port=port)

