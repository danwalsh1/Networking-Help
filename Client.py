#>> Authors: Daniel Walsh, Gareth Holloway
#>> Code not to be used without written permission from both authors
#>> Credit must be given to authors even if written permission is given

import socket
import threading

#>> Create the socket
sock = socket.socket()
#>> Connect to the server at the given address and port
sock.connect(('127.0.0.1', 44444))

def sendThread():
    ''' This function will be executed when the thread below is opened '''
    #>> Get user input
    msg = input("")
    #>> Encode the users input
    encodedMsg = msg.encode()
    #>> Send the encoded data to the server
    sock.send(encodedMsg)
    
#>> Create the thread to be opened
ClientThread = threading.Thread(target = sendThread)
#>> While daemon is true, if the main program closes, the thread won't keep the program open
ClientThread.daemon = True
#>> Start the thread
ClientThread.start()

while True:
    ''' Infinate loop | ENSURE SOME SORT OF ESCAPE IN ANY CODE YOU HAND IN '''
    #>> Recieve messages from the server
    msg = sock.recv(1024)
    #>> Decode the recieved message
    decodedMsg = msg.decode()
    #>> Print the decoded message to the screen
    print (decodedMsg)
    
