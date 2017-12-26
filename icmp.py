#!/usr/bin/bash

import sys
import os
import datetime
import socket
import struct

eth_src = "\x00\x00\x00\x00\x00\x00"
eth_dst = "\x00\x00\x00\x00\x00\x00"
eth_type = 0x800

ip_src = "192.168.1.1."
ip_dst = "192.168.1.110"

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
    
