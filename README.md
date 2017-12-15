Distributed-File-System
==============================

Distributed File System assignment for Scalable computing in Trinity College Dublin

For this assignment I choose to implement
* File Server
* Directory Server
* Lock Server
* Authentication server

File Server
--------
The file-server uses a flat directory structure to store files. This means that all files uploaded must have a unique name.
The file server contains a method to read or write to a specific file. The file server is able to access the file system.

Directory Server
--------
The directory service or server maps the names of network resources to their respective network addresses. 
If a client wants to read or write a file.They have to first contact the DS and ask for the file path.Then only the user 
will be able to read or write the file.

Lock Server
--------
The lock server checks if the file is ready to be written. If the file is unlocked the server allows the client to write.
If the file is already locked, the server responds with a fail message. The lock will be removed only after the user who 
locked it will complete writing.

Authentication
----------------
There is a part to login or signup for the application. User will have to login and the username and password will be 
tranferred using HTTPBasicAuth.


Running
--------
To test this program execute the following:
directsrv.py
lockserver.py 
fileServer.py 
authentication.py

Then we have to execute client.py and follow further instructions.
