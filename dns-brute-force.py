import socket,os,sys
class Methods(object):

    def __init__(self):
        self.filelocation = ""
        self.file = ""
        self.subdomains = ["ns1", "ns2", "ww2", "www", "admin", "intranet", "ftp"]
        self.subdomainwordlistfile = ''
        self.host = ""
        self.method = ''
        self.ports = [80,8080,443,21,25,135,23,11,111,67,13,7,19,17,53]
     
    def main(self):
        print('\n'
              '        ████▀░░░░░░░░░░░░░░░░░▀████ \n'
              '        ███│░░===============░░│███ \n'
              '        ██▌│░PROGRAM DEVELOPED░│███ \n'
              '        ██░└┐░=== BY KAYAN===░┌┘░██ \n'
              '        ██░░└┐░░░░░░░░░░░░░░░┌┘░░██ \n'
              '        ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██ \n'
              '        ██▌░│██████▌░░░▐██████│░▐██ \n'
              '        ███░│▐███▀▀░░▄░░▀▀███▌│░███ \n'
              '        ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██ \n'
              '        ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██\n'
              '        ████▄─┘██▌░░░░░░░▐██└─▄████\n'
              '        █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████\n'
              '        ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████ \n'
              '        █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████ \n'
              '        ███████▄░░░░░░░░░░░▄███████\n')
        self.method = input("Choose the mode:\n"
                            "[1] Default list\n"
                            "[2] Brute-Force with file.txt\n"
                            "[3] Port Scanner\n"
                            ">> ")
        while self.method not in ["1","2","3"]:
            print("[!] Method not found!")
            self.method = input("\nChoose the mode:\n"
                                "[1] Default list\n"
                                "[2] Brute-Force with file.txt\n"
                                "[3] Port Scanner\n"
                                ">> ")
        if self.method == "1":
            self.host_function()
            self.dns_default_bruteforce()
        elif self.method == "2":
            self.file_function()
            self.host_function()
            self.dns_bruteforce_wordlist()
        elif self.method == "3":
            self.port_scanner()

    def file_function(self):
        self.filelocation = input("File name: ")
        while self.filelocation[-4:] != '.txt' or os.path.exists(self.filelocation) != True:
            print("[!] Invalid file name: ")
            self.filelocation = input("File name: ")

    def host_function(self):
        self.host = input("Host: ")
        try:
            if self.host.replace('.', '').isdigit():
                self.host = socket.gethostbyaddr(self.host)
            else:
                if "www." in self.host:
                    self.host = self.host[4:]
                    pass
                if ".com" not in self.host:
                    self.host = self.host + ".com"
                    pass
            print(f"Host Ip: {socket.gethostbyname(self.host)}")
        except socket.herror:
            print("[!] HOST NOT FOUND ")
            sys.exit()
        except socket.gaierror:
            print("[!] HOST NOT FOUND OR CORRUPTED HOST")
            sys.exit()

    def dns_default_bruteforce(self):
        for subdomain in self.subdomains:
            dns = subdomain + "." + self.host
            try:
                print(f"{dns} : {socket.gethostbyname(dns)}")
            except socket.herror:
                pass
            except socket.gaierror:
                pass

    def dns_bruteforce_wordlist(self):
        try:
            self.subdomainwordlistfile = open(self.filelocation, 'r')
            self.subdomainwordlist = self.subdomainwordlistfile.read().strip().split()
            for item in self.subdomainwordlist:
                dns = item + "." + self.host
                try:
                    print(f'{dns} : {socket.gethostbyname(dns)}')
                except socket.herror:
                    pass
                except socket.gaierror:
                    pass
        except FileNotFoundError:
            print("[!] FILE NOT FOUND [!]")

    def port_scanner(self):
        self.host = input("Host: ")
        if "www." in self.host:
            self.host = self.host[4:]
            pass
        for port in self.ports:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            code = client.connect_ex((self.host,port))
            if code == 0:
                try:
                    print(f" {port} OPEN")
                except socket.gaierror:
                    pass
dnsbruteforce = Methods()
dnsbruteforce.main()
