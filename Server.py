#>> Authors: Daniel Walsh, Gareth Holloway
#>> Code not to be used without written permission from both authors
#>> Credit must be given to authors even if written permission is given

import socket
import threading

#>> Create the socket
sock = socket.socket()
#>> Bind the socket to the given address and port
sock.bind(('127.0.0.1',44444))
#>> Define how many clients can be waiting to connect to the server
sock.listen(2)
#>> Create an empty list where currently connected clients will be stored
connections = []

def clientThread(conn, addr):
    ''' This function will be executed when a new thread is opened when any new client connects to the server '''
    while True:
        #>> Recieve a message from the client
        msg = conn.recv(1024)
        #>> Send the message to every client that isn't the one which sent the message
        for connection in connections:
            if connection != conn:
                #>> The message doesn't need to be encoded because it was already encoded by the client
                connection.send(msg)

while True:
    ''' Infinate loop | ENSURE SOME SORT OF ESCAPE IN ANY CODE YOU HAND IN '''
    #>> Accept a connection from a client
    conn, addr = sock.accept()
    #>> Create a thread for the client. The thread will run the target function with the given arguments
    ChatThread = threading.Thread(target = clientThread, args = (conn,addr))
    #>> While daemon is true, if the main program closes, the thread won't keep the program open
    ChatThread.daemon = True
    #>> Start the thread
    ChatThread.start()
    #>> Store the new connection in our list of connections
    connections.append(conn)
        
        
        
        

