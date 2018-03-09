import socket
import os
import subprocess
s = socket.socket()

hosts = ["host", "cal", "nasa", "fbi"]
hostdescs = ["Your standard normal host", "California Institute of Technology", "National Aeronautics and Space Administration", "Federal Bureau of Investigation"]

host_conn_to = hosts[0]

#port = input("Enter port number: ")
#hostname = raw_input("Enter hostname: ")
s.bind(("192.168.1.8", 5000))
print "searching for connections..."
endProgram = False
while endProgram != True:
    s.listen(5)
    c, addr = s.accept()
    print "Connection from ", str(addr)
    c.send(" --Connected to HOST-- \n")
    c.send("\nLogin: ")
    data = c.recv(1024)
        
    c.send(" OK, password required")
    c.send("\nPassword: ")
    data = c.recv(1024)
    c.send("Login Successfull!")
    c.send("\n")
    def chat():
        c.send(host_conn_to+"> ")
        data = c.recv(1024)
        if data.rstrip() == "exit":
            c.send("Exiting...")
	    s.close()
            c.close()
	    exit()

	if data.rstrip() == "help":
	    c.send("List of help commands: \n")
	    c.send("Exit - exits the server\n")
	    c.send("ls - lists the files\n")
	    c.send("cls - clear the screen\n")
	    c.send("netstat - lists directories\n")
	    c.send("telnet - connect to a host\n")
            chat()

        if data.rstrip() == "":
                        chat()
        if data.rstrip() == "ls":
            #c.send(str(os.listdir("/")))
            os.chdir("/home/pi/Desktop/telnet_server/__FILES__/"+host_conn_to)
            file_listings = str(subprocess.check_output(["ls"]))
            #file_listings_1 = ''.join(file_listings)
            c.send(file_listings)
            c.send("\n")
            chat()
        if data.rstrip() == "cls":
	    file_listings = str(subprocess.check_output(["clear"]))
            c.send(file_listings)
            chat()
        if data.rstrip() ==  "netstat":
            c.send("host\tdescription")
            c.send("\n------------------------------------\n")
            for hostx in range(4):
                c.send(hosts[hostx])
                c.send("\t")
                c.send(hostdescs[hostx])
                c.send("\n")
            c.send("\n")
            chat()
            
        if data.rstrip() == "telnet":
            c.send("Host to connect to: ")
            data = c.recv(1024)
            if data.rstrip() in hosts:
                    for hostx in range(4):
                        if hosts[hostx] == data.rstrip():
                            global host_conn_to
                            host_conn_to = hosts[hostx]
                            print hostx
                            

                
            chat()
        c.send("COMMAND NOT FOUND... "+str(data))
        print addr, ":", str(data)
        chat()
    while True:
        while str(data) != "exit":
            chat()
    
    if not data:
        print "(", addr, ") has left"
c.close()
