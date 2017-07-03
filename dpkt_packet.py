#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Xiaokang Yin
# @Date:   2017-05-25 14:22:34
# @Last Modified by:   xiaokang
# @Last Modified time: 2017-07-03 15:25:28

import dpkt
import datetime
import socket
import win_inet_pton
from dpkt.compat import compat_ord


def mac_addr(addr):
    """
    Convert a MAC address to a readable/printable string
    """
    return '-'.join('%02x' % compat_ord(b) for b in addr)

def inet_to_str(inet):
    """
    Convert inet object to a string
    """
    # First try ipv4 and then ipv6
    try:
        return socket.inet_ntop(socket.AF_INET, inet)       #if error please install win_inet_pton// pip install win_inet_pton
    except ValueError:
        return socket.inet_ntop(socket.AF_INET6, inet)

def print_eth(eth):
    """
    print the ethernet header 
    """
    print 'Ethernet Frame:'
    print 'src: %s\tdst: %s'%(mac_addr(eth.src),mac_addr(eth.dst))
    if (eth.type == 0x800):
        print 'Type: IP'
    elif (eth.type == 0x806):
        print 'Type: ARP'
    else:
        print 'Type:Unknown'
    print
    
def print_arp(arp):
    """
    print the arp information
    """
    print 'ARP:'
    print 'Hardware type:0x%x\tProtocol type:0x%x' %(arp.hrd,arp.pro)
    print 'Hardware addr length:0x%x bytes\tProtocal addr length:0x%x bytes\t Operation code:0x%x' %(arp.hln,arp.pln,arp.op)
    print 'Hardware src:%s\tProtocal src:%s'%(mac_addr(arp.sha),inet_to_str(arp.spa))
    print 'Hardware dst:%s\tProtocal dst:%s'%(mac_addr(arp.tha),inet_to_str(arp.tpa))
    print 
    
def print_dns(dns):
    """
    print the dns information
    """
    #TODO.
    

def print_ip(ip):
    """
    print the ip header
    """
    print("IP:")
    print 'version: %d  header length: %d(*4 bytes) Service type:0x%x\tTotal length:%d' %(ip.v,ip.hl,ip.tos,ip.len)
    print 'Identifier:0x%x\tFlag:0x%x\tOffset:0x%x'%(ip.id,ip.df,ip.offset)
    print 'TTL:%d\tProtocol:0x%x\tChecksum:0x%x'%(ip.ttl,ip.p,ip.sum)
    print 'Src:%s\tDst:%s' %(inet_to_str(ip.src),inet_to_str(ip.dst))
    print

        
def print_tcp(tcp):
    """    
    print the tcp header
    """
    print 'TCP:'
    print 'Source port:%d\tDestination port:%d' %(tcp.sport,tcp.dport)
    print 'Sequnce number:%d' %(tcp.seq)
    print 'ACK number:%d' %(tcp.ack)
    print 'Windows size:%d' %(tcp.win)
    print 'Checksum:%d\tUrgent pointer:0x%x' %(tcp.sum, tcp.urp)
    print

def print_udp(udp):
    """
    print the upd header
    """
    print 'UDP:'
    print 'Source port:%d\tDestination port:%d' %(udp.sport,udp.dport)
    print 'Checksum:0x%x' %(udp.sum)
    print 'length: %d' %(udp.ulen)
    print 

def print_http(http):
    """
    print the http header
    """
    try:
        request = dpkt.http.Request(http)
        #http = dpkt.http(tcp.data)
    except (dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError):
            return
    print 'HTTP request:\n %s\n' % repr(request)
    print 
    print

def print_tls(tcp):
    """
    print the ssl/tsl information
    """
    try:
        tls = dpkt.ssl.TLS(tcp.data)
    except dpkt.NeedData:
        return 'UNKNOWN'
    if tls.version in (dpkt.ssl.SSL3_V, dpkt.ssl.TLS1_V,dpkt.ssl.TLS11_V,dpkt.ssl.TLS12_V):
        print '########################'
        if tls.version == dpkt.ssl.SSL3_V:
            sslversion = 'SSL3_V'
        elif tls.version == dpkt.ssl.TLS1_V:
            sslversion = 'TLS1_V'
        elif tls.version == dpkt.ssl.TLS11_V:
            sslversion = 'TLS11_V'
        elif tls.version == dpkt.ssl.TLS12_V:
            sslversion = 'TLS12_V'
    print 'ssl/TSL version:%s'% sslversion
    print 'HTTPS'
    print 'Length:%d\t Type:0x%x'%(tls.len,tls.type)
    print
    
def print_icmp(icmp):
    """
    print the icmp header
    """
    print('ICMP:')
    print ('type:%d code:%d checksum:%d data: %s\n' % (icmp.type, icmp.code, icmp.sum, repr(icmp.data)))
    print


def resolve_packet(pcap):
    """ 
    print out the TCP/IP header
    """
    for timestamp, buf in pcap:
        #ethernet fram (mac src/dst, ethertype)
        print '************************************************'
        print'Timestamp: %s'% str(datetime.datetime.utcfromtimestamp(timestamp))
        eth = dpkt.ethernet.Ethernet(buf)
        print_eth(eth)
         # Make sure the Ethernet data contains an IP packet
        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data
            print_ip(ip)

            # TCP in the transport layer
            if isinstance(ip.data, dpkt.tcp.TCP):
                tcp = ip.data
                print_tcp(tcp)
                #http
                print_http(tcp.data)
                print_tls(tcp)
            if isinstance(ip.data, dpkt.icmp.ICMP):
                icmp = ip.data
                print_icmp(icmp)
            if isinstance(ip.data, dpkt.udp.UDP):
                udp = ip.data
                print_udp(udp)
        if isinstance(eth.data, dpkt.arp.ARP):
            arp = eth.data
            print_arp(arp)

def main():
    """
    Open up the pcap file and resolve the pcakets
    """ 
    
    with open("tls.pcap",'rb') as f:  #读取数据包，更改为你需要读取数据包的文件名
        pcap = dpkt.pcap.Reader(f)
        resolve_packet(pcap)

if __name__ == '__main__':
    main()
