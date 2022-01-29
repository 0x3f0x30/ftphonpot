#!/bin/python3
try:
    from socket import *
    from logging import *
    from datetime import datetime
    from pyfiglet import figlet_format
except ModuleNotFoundError as moderr:
    print(warning("%s"%(str(moderr))))
    exit(1)

class pot:
    def __init__(self):
        self.sock = socket(AF_INET,SOCK_STREAM)
    def pots(self,LHOST,LPORT=21):
        with self.sock as pot:
            if (len(pot) <= 0):
                print(error("socket ERROR!!"))
            if (pot.bind((LHOST,LPORT))<=0):
                print(error("gagal ngebind!!"))
                exit(0)
            pot.listen(10)
            print(info("FTPHoneypot aktif | [%s]:[%d]" % (LHOST,LPORT)))
            while (not False):
                ip = pot.accept()[1][0]
                print(
                    critical(
                            f"[{datetime.now()}] [{ip}] sangat sus"
                    )
                )

def main():
    honeypot = pot()
    print(figlet_format("FTP HONEYPOT",font="larry3d"))
    print("Author: https://github.com/BenjaminXN")
    print()
    LHOST = input("LHOST: ")
    if (len(LHOST)<=0):
        print(error("LHOST kosong!!"))
        exit(1)
    else:
        honeypot.pots(LHOST)
    return 0

if __name__ == "__main__":
    main()