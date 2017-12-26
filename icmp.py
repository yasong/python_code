#!/usr/bin/bash

import sys
import os
import datetime
import socket
import struct


overflow_len = 


ip_src = "192.168.1.1."
ip_dst = "192.168.1.110"

def build_eth_header():
    eth_src = "\x00\x00\x00\x00\x00\x00"
    eth_dst = "\x00\x00\x00\x00\x00\x00"
    eth_type = 0x800
    eth_len = 14
    
    eth_header = struct.pack('', )

def build_ip_header():
    #ip header
    ip_ver = 4
    ip_ihl = 6
    ip_tos = 0
    ip_total_len = 
    ip_id = 0
    ip_frag_offset = 0
    ip_ttl = 255
    ip_protocol = socket.IPPROTO_ICMP
    ip_checksum = 0
    ip_src_addr = socket.inet_pton(socket.AF_INET, ip_src)
    ip_dst_addr = socket.inet_pton(socket.AF_INET, ip_dst)
    ip_options = "\x00\x83\x94\x04"

    ip_header = struct.pack('!BBHHHBBH4s4s4s' , ip_ver_ihl, ip_tos, ip_total_len, ip_id, ip_frag_offset, ip_ttl, \
                    ip_protocol, ip_checksum, ip_src_addr, ip_dst_addr, ip_options)
                    
                    
    return ip_header


def build_icmp():

def checksum(packet):
    if (len(packet) & 1):
        packet += b'\x00';
    i = 0;
    nSum = 0;
    while i < len(packet):
        nSum += (packet[i] << 8) + packet[i+1];
        i += 2;
    nCarry = nSum >> 16;
    while nCarry:
        nSum = (nSum & 0xffff) + nCarry;
        nCarry = (nSum >> 16);
    nSum = (~nSum & 0xffff);
    return nSum;

def build_payload():
    
    
    
def build_packet():



def send_packet():
    
    
def main():



if __name__ == "__main__":
    main()
    
