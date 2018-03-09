import os
from random import *

print("Working...")
def scan():
	ip1 = str(randint(0,255))
	ip2 = str(randint(0,255))
	ip3 = str(randint(0,255))
	ip4 = str(randint(0,255))
	hostname = ip1+"."+ip2+"."+ip3+"."+ip4
	print "trying "+hostname
	os.system("ping -c 1 -i 0.6  "+hostname+" | grep -o ttl > realsite.txt & sleep 0.3; kill $!")
	f = open("realsite.txt", "r")
	realsite = f.read(3)
	print "opened and read file with "+realsite
	if realsite == "ttl":
		print "Success"
		with open("ipaddrs.txt", "a") as myfile:
    			myfile.write(hostname+"\n")
	else:
		print "fail"
	f.close()
	scan()
scan()