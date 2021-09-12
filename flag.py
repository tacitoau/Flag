from scapy.all import *

#Definindo as variáveis

dest = input("/nDestination: ")
destport = input("Port: ")
flag = input("Flags: ")

port = int(destport)
ip = IP(dst=dest)
tcp = TCP(dport=port, flags=flag)

#Encontrando o Resultado

pkt = ip/tcp

srloop(pkt, count=1)
