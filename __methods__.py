import socket,dns,re
class Methods():

    def file(self):
        self.file = input("File name: ")
    def host(self):
        self.host = input("Host: ")
        if "www" in self.host:
            print("[!] Type without subdomain")
            pass
    def hostwordlist(self):
        self.hostw = input("Host: ")
        if self.hostw.isdigit():
            self.hostw = dnsreverse(self.host)
        else:
            pass
    def dnsreverse(self):
        try:
            print(socket.gethostbyaddr(self.host))
        except socket.herror:
            return "[!] HOST NOT FOUND "
        except socket.gaierror:
            pass
    def getdnsbyhost(self):
        subdomains = ["ns1", "ns2", "www", "ftp", "admin", "intranet", "ww2"]
        for subdomain in subdomains:
            DNS = subdomain + "." + self.host
            try:
                print(DNS + ":" + socket.gethostbyname(DNS.lower()))
            except socket.gaierror:
                print(f"[!] {subdomain} NOT FOUND ")
    def dnsbywordlist(self):
        try:
            with open(self.file) as self.file:
                subdomains = self.file.readlines()
                for subdomain in subdomains:
                    DNS = subdomain.strip("\n") + "." + self.hostw
                    try: print(DNS + ":" + socket.gethostbyname(DNS))
                    except socket.gaierror:
                        print("[!] HOST NOT FOUND ")
                        exit()
                        pass
        except FileNotFoundError:
            print('[!] FILE NOT FOUND [!]')
