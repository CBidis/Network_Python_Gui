# Network_Python_Gui
NetworkPythonGui consists of 3 python files,the guiip.py,the ipconver.py and the pings.py
#The Guiip.py file
This python script is responsible for the creation of the application,it  consists of 6 buttons and 6 entry fields.

The 'Net-id' button and the 2 upper fields are responsible for the calculation of the Net-id  
The 'ip to dns ping' button with the field under it , returns the DNS name of a given ip and sends the given ip
as an input to 'the Ping Adress' field.

The 'dns to ip ping' and the field below it are responsible for the calculation of the ip for a given DNS name
and  sends the ip coresponding to the name to the 'Ping Adress' field.

The 'Ping Adress' button uses the subproccess of ping for a given ip , from the entry field below the button.

The 'Show the entries of succesful pings' button returns all the succesful pinged ips , that were written to the database
and creates a .csv file with all  the entries.

The 'Exit' button , it just terminates the application!

#The ipconver.py file
This python script calculates the Net-id for the button of the Gui , with the function ipconv.
It does all the logical checks for a given ip and returns Messageboxes for errors or Succesful calculations.

#The pings.py file
With the use of pingad() function , it does the ping of the given ip, for every succesful ping it creates an entry
to the database(test.pingt table).

Also for the failed pings there is an entry to the database(test.pingf table). 
For the database entries there is check if there is a duplicate entry using pymysql.err.IntegrityError exception.
Each time the exception is caught we use the 'pass' action to continue .

The dbping() function selects all the entries from the table test.pingt and creates a .csv file with these entries.

The dnstoip() function returns the ip of DNS name and creates an entry to the table dnstoip table for every succesful 
calculation , also checks for duplicate entries to the database .
And uses socket.gaierror exception if there is no IP corresponding to the DNS given.

The iptodns() function, returns the DNS name of a given ip, this time we dont use a table to write our succesful calculation.
And by using socket.herror exception we find the ip's that they dont correspond to any DNS name.
We also use and to this function the socket.gaierror exception.
