# ComputerSecurity-Project

There are two main ways of using this project. The first is to simulate both the client and the server on one laptop using
two terminal windows, or this project can be used by two laptops communicating with each other over the network,

This can be accomplished by setting the ip_address variable in main.py to the server's ip_address or if simulating on one laptop you can use
127.0.0.1 as the ip_address. Next, you must set the port. Depending on the network, the port may be busy, thus picking a port may require some
expermintation. 

After these variables have been set, both laptop (or terminals) can run the main.py function. From there the user that has chosen to be 
the server will select "s" in the terminal, and the client will select "c". Next, the UI will appear for both the users. From there, the users can 
securely send and recieve messages following the protocols listed for this assignments.

PLEASE NOTE: It is recommended the you use Python 3.9.16 in order for ensured compatibility. You should also run 'pip install -r requirements.txt' to install all the dependencies needed.
