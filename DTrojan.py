import socket
import os
import getopt

def usage():
	print "Detect Trojan Tool"
	print 
	print "Usgae: DTrojan.py"
	print "-fx --feature					-	detect the packet feature of the Trojan"
	print "-m --modify					-	change the feature or add feature of the Trojan"
	print "-a --add						-	add the feature of the Trojan"
	print "-l --list					- 	list the feature of the Trojan in the local lib"
#	print "-c --command					-	initialize a command shell"
	print "-s --start					-	start the detect program"
	print "-n --name					-	the name of the Trojan"
	
	print "Example:"
	print "DTrojan.py -l"
	print "DTrojan.py -s"
	
	print "DTrojan.py -m -n huigezi -f 10 16 08 27"
	print 
	
	
