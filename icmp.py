#!/usr/bin/bash

import sys
import os
import datetime
import socket
import struct

eth_src = "\x00\x00\x00\x00\x00\x00"
eth_dst = "\x00\x00\x00\x00\x00\x00"
eth_type = 0x800
eth_len = 14
overflow_len = 


ip_src = "192.168.1.1."
ip_dst = "192.168.1.110"
options = "\x00\x83\x94\x04"

#ip header
ip_ver = 4
ip_ihl = 6
ip_tos = 0
ip_total_len = 
ip_id = 0
ip_frag_offset = 0
ip_protocol = socket.IPPROTO_ICMP
ip_checksum = 0
ip_src_addr = socket.inet_pton(socket.AF_INET, ip_src)
ip_dst_addr = socket.inet_pton(socket.AF_INET, ip_dst)


def checksum(packet):
    if (len(bData) & 1):
        bData += b'\x00';
    i = 0;
    nSum = 0;
    while i < len(bData):
        nSum += (bData[i] << 8) + bData[i+1];
        i += 2;
    nCarry = nSum >> 16;
    while nCarry:
        nSum = (nSum & 0xffff) + nCarry;
        nCarry = (nSum >> 16);
    nSum = (~nSum & 0xffff);
    return nSum;

def main():
    
