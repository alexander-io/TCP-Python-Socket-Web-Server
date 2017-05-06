Alexander Harris
Network Programming, CS325
Homework 4, Simple Web Server
Spring 2017
Professor Tony Mullen

To test run the program, download use python3 and execute the WebServer.py code on the server side machine.
Issue this command :
  $ python3 WebServer.py

Next we need to send a request for a file to the server from the client side.
We will use two command line arguments to specify the method type and the file_name
The syntax for this command looks like this :
  $ python3 WebClient.py <method> <fila_name>

For example, on the client side issue this command :
  $python3 WebClient.py GET HelloWorld.html

  Note, this should return the contents of the HelloWorld.html file to the requester as long as the file is presently available to the server.
  If you request a file that doesn't exist, like so :
    $python3 WebClient.py GET NonExistentFile.html

  ... then the server should return a 404.html file coupled with http status code of 404 to the requester.
