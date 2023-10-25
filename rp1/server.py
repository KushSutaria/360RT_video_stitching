
import socket

 

localIP     = "192.168.43.188"

localPort   = 20001

bufferSize  = 40960000

 

msgFromServer       = "Hello UDP Client"

bytesToSend         = str.encode(msgFromServer)

 

# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))

 

print("UDP server up and listening")

 

# Listen for incoming datagrams

while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    print(type(message))
    file =  open("2.jpg","wb")
  #  for a in range(len(message)):
  #      print(str(message[a]))
    file.write(message)
    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    
    #print(clientMsg)
    #print(clientIP)

   

    # Sending a reply to client

    UDPServerSocket.sendto(bytesToSend, address)