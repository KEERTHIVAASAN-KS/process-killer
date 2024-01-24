import os
import psutil
import socket

blocklist=[]

def readblocklist():
    file=open("tcpblocklist.txt","r")
    content=file.readlines()
    for i in range(len(content)):
        content[i]=content[i].rstrip("\n")
    for i in range(len(content)):
        content[i]=content[i].split()
        content[i][1]=int(content[i][1])
        blocklist.append(content[i])
    file.close()

def blocker():
    activeconnections=psutil.net_connections()
    for i in activeconnections:
        if len(i.raddr)==0:
            continue
        if [i.raddr[0],i.raddr[1]] in blocklist:
            os.kill(i.pid,9)
            

#main
readblocklist()
while True:
    blocker()



    
