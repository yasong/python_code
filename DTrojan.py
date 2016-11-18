import socket
import os
import getopt

def usage():
	print "Detect Trojan Tool"
	print 
	print "Usgae: DTrojan.py"
	
    print "-h --help                    -   show the usage information"
	print "-l --list					- 	list the feature of the Trojan in the local lib"
#	print "-c --command					-	initialize a command shell"
	print "-s --start					-	start the detect program"
#    print "-e --exit                    -   stop the detect program"
#	print "-n --name					-	the name of the Trojan"
#    print "-a --add                        -   add the feature of the Trojan"
    print "-f feature_hex               -   detect the packet feature in hex of the Trojan"
    print "-r feature_raw               -   detect the packet feature in raw of the Trojan"
    print "-m --modify                  -   change the feature or add feature of the Trojan"
	
	print "Example:"
	print "DTrojan.py -l"
	print "DTrojan.py -s"
	
	print "DTrojan.py -m huigezi -f 10 16 08 27"
	print "DTrojan.py -m huigezi -r cow?"

    exit(0)
def show():
    #show the Trojan features in the lib
    #
def detect():
    #start detect the Trojan
    #

def modify():
    #modify the Trojan feature in the lib
    #
def alert():
    #show the alert message
    #

def main():
    global feature
    global name
    global flag = "hex"
    usage();
    try:
        opts, args =getopt.getopt(sys.argv[1:], "hlsf:r:m:",["help","list","start","feature_hex","feature_raw","modify"])
    except getopt.GetoptError as err:
        print str(err)
        usage()
    command = raw_input("You can stop detect the Trojan by input 'exit':");
    name = None
    while command!="exit":
        for o,a in opts:
            if o in ("-h","--help"):
                usage()
            elif o in ("-l","--list"):
                show()
            elif o in ("-s","--start"):
                detect()
            elif o in ("-m","--modify"):
                name = a
            elif o in ("-f","feature_hex"):
                flag = "hex"
                if name =None:
                    print "please input the Trojan name!"
                    usage()
                else :
                    feature = a;
                    modify()
            elif o in ("-r","feature_raw"):
                flag = "raw"
                if name =None:
                    print "please input the Trojan name!"
                    usage()
                else :
                    feature = a;
                    modify()    
main()