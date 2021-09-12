#!/usr/bin/python3

from scapy.all import *

dest = input("/nDestination: ")
destport = input("Port: ")
flag = input("Flags: ")

port = int(destport)
ip = IP(dst=dest)
tcp = TCP(dport=port, flags=flag)

pkt = ip/tcp

srloop(pkt, count=1)
