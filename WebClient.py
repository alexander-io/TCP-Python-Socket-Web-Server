# Alexander Harris
# Network Programming, CS325
# Homework 4, Simple Web Server
# Spring 2017
# Professor Tony Mullen


# To test run the program, download use python3 and execute the WebServer.py code on the server side machine.
# Issue this command :
#   $ python3 WebServer.py
#
# Next we need to send a request for a file to the server from the client side.
# We will use two command line arguments to specify the method type and the file_name
# The syntax for this command looks like this :
#   $ python3 WebClient.py <method> <fila_name>
#
# For example, on the client side issue this command :
#   $python3 WebClient.py GET HelloWorld.html
#
#   Note, this should return the contents of the HelloWorld.html file to the requester as long as the file is presently available to the server.
#   If you request a file that doesn't exist, like so :
#     $python3 WebClient.py GET NonExistentFile.html
#
#   ... then the server should return a 404.html file coupled with http status code of 404 to the requester.


# import system specific params
import sys

# import socket module
from socket import *

# test printing command line arguments
# print('method : ', sys.argv[1])
# print('file to open: ', sys.argv[2])

# determine server name, localhost for testing | replace with ip address
serverName = 'localhost'

# include the port at which the server is listening
serverPort = 12000

# init the client socket with 2 params :
# @param AF_INET address family that is used to determine the type of addresses that the socket can communicate with : IPv4 addresses
# @param SOCK_STREAM connection based protocol commonly used for TCP
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect clientSocket to the server name and server port.
clientSocket.connect((serverName, serverPort))

# assign the sentence to send to have a string with two tokens :
# @token method a request to the server to execute a GET request
# @token file_name the file requested from the server
sentence = sys.argv[1] + ' ' + sys.argv[2]

# send the request to the server
clientSocket.send(sentence.encode('utf-8'))

# init response to store incoming data
response = ''

while True:
    # collect incoming data from clientSocket using .recv()
    # and concatenate it to response. Remember to decode
    # incoming binary data into a string using .decode('utf-8')
    response += clientSocket.recv(1024).decode()
    print(response)
    break

clientSocket.close()
