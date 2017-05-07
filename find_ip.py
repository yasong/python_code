#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author: yasong
# @Date:   2017-04-21 11:08:30
# @Last Modified by:   Xiaokang Yin
# @Last Modified time: 2017-04-27 10:07:51
import os
import sys
import subprocess  
cmd="cmd.exe"

ip_pre = "10.104.171."
baidu = 'www.baidu.com'
empty_ip = []
cmd_ip = 'netsh interface ip set address  "以太网" static '#your Ethernet name
netmask = ' 255.255.255.0'
gateway = ' 10.104.171.1'
def find_ip():
    
    p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)  
    p.stdin.write("arp -a"+"\n");
    p.stdin.close()
    i = 0;
    ip =''
    for line in p.stdout.readlines():
        index = line.find(ip_pre)
        if (index == 6):
            for j in range(6,20):
                ip = ip + line[j]
            print"the ip of this host is %s"%ip
            #print "the empty ip is:"
        if (index == 2):
            i = i + 1
            ip = ip_pre + str(i)
            while  line.find(ip_pre + str(i)) < 0 :
                #print ip_pre + str(i)
                empty_ip.append(ip_pre+str(i))
                i = i + 1
                if i > 255:
                    sys.exit(0)
        
def ping():
    p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
    p.stdin.write("ping "+ baidu + "\n");
    p.stdin.close()
    p.wait()
    result = p.stdout.read()
    #print"result is:%s"%result
    #print result[1]
    if result.find("0%") < 0:
        return 0
    else:
        return 1

def change_ip():
    flag = 0
    for i in range(len(empty_ip)):
        p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
        p.stdin.write(cmd_ip + empty_ip[i] + netmask + gateway + "\n");
        p.stdin.close()
        p.wait()
        result = p.stdout.read()
        print len(result)
        if len(result) == 0:        
            if ping() == 1:
                print "the ip %s address is ok!"%empty_ip[i]
                break
        elif result.find("请求的操作需要提升(作为管理员运行)。"):
            print "you should run it in Administrator privileges"
            break
            
def main():
    find_ip()
    print "the empty ip is:"
    for i in range(len(empty_ip)):
        print empty_ip[i]
    #change_ip()

if __name__ == '__main__':
    main()
