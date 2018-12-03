from __methods__ import Methods
class Program():
    def __init__(self):
        self.method = ""
        self.methods = ["1","2","3"]
        self.host = ""
    def main(self):
        print('\n'
              '        ████▀░░░░░░░░░░░░░░░░░▀████ \n'
              '        ███│░░===============░░│███ \n'
              '        ██▌│░PROGRAM DEVELOPED░│███ \n'
              '        ██░└┐░░==BY KAYAN ==░░┌┘░██ \n'
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
              '        ███████▄░░░░░░░░░░░▄███████')
        self.method = input(" " * 9 + "> Choose which of methods do you wanna use <\n"
        "[1] Reverse-DNS\n[2] Brute DNS with list default\n[3] DNS Brute-Force with a file\n>> ")
        if self.method not in self.methods:
            print("[!] Method not found!")
    def run(self):
        if self.method == "1":
            dns = Methods()
            dns.host()
            dns.dnsreverse()
        elif self.method == "2":
            dns = Methods()
            dns.host()
            dns.getdnsbyhost()
        elif self.method == "3":
            dns = Methods()
            dns.hostwordlist()
            dns.file()
            dns.dnsbywordlist()
    def tag(self):
        while True:
            self.tag = input("\nDo you wanna continue? [s|n]: ")
            if self.tag.lower() == "n":
                return exit()
            elif self.tag.lower() == "s":
                return program.main, program.run()
            else:
                print("Error.. We not has this option here")

program = Program()
program.main()
program.run()
program.tag()
