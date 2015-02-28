import subprocess
import socket
import pymysql
from tkinter import *
def pingad(sadress):
#sadress=input('give the starting ip\n')
   num = 0
   conn = pymysql.connect(host="localhost", port=3306, user="chrigeta", passwd="vegeta1988", db="test")
   cur = conn.cursor()
   for ping in range(0,11):
       address = sadress+ str(ping)
       res = subprocess.call(['ping',address])
       try:
           if res == 0:
               print("Succesful Ping","Succesful Ping to address:"+address)
               num = num + 1
               cur.execute('INSERT INTO test.pingt  VALUES (%s,%s,%s)',(sadress,address,'OK'))
               conn.commit()
               print('Succesful Database Entry')
               print ("ping to", address, "OK")
           elif res == 2:
               print ("no response from", address)
           else:
               
               print ("ping to", address, "failed!")
               try:
                   cur.execute('INSERT INTO test.pingf  VALUES (%s,%s,%s)',(sadress,address,'FAILED'))
                   conn.commit()
               except pymysql.err.IntegrityError:
                   pass
       except pymysql.err.IntegrityError:
          pass
        
   messagebox.showinfo("Succesful Pings","The number of Succesful Pings is:"+str(num))
   
def dbping(dbip):
      conn = pymysql.connect(host="localhost", port=3306, user="chrigeta", passwd="vegeta1988", db="test")
      cur = conn.cursor()
      row_count=cur.execute("SELECT adress FROM test.pingt WHERE sadress=%s",(dbip))
      if row_count >0:
         fo=open('succesful_pings.xls', 'a')
         fo.write('Succesful IPs for the ip:  '+dbip)
         fo.write('\n')
         for r in cur.fetchall():
             print(r)
             fo.write(str(r).strip("('',)"))
             fo.write('\n')
         print(fo.closed)
         if fo.closed==False:
            fo.close()
            print(fo.closed)
         else:
            pass    
      else:
          messagebox.showerror("ERROR","No data corresponding to the given IP")
   
def dnstoip(name):   
    try:
       dnstoip.addr = socket.gethostbyname(name)
       messagebox.showinfo('Succesful Transformation',' The address of   '+name+'  is  '+dnstoip.addr)
       try:
           conn = pymysql.connect(host="localhost", port=3306, user="chrigeta", passwd="vegeta1988", db="test")
           cur = conn.cursor()
           cur.execute('INSERT INTO test.dnstoip  VALUES (%s,%s)',(name,dnstoip.addr))
           conn.commit()
       except pymysql.err.IntegrityError:
           pass
    except socket.gaierror as msg:
       messagebox.showerror('Error','No IP corresponding to the given DNS name')
       
def iptodns(ipname):
   try:
      a=socket.gethostbyaddr(ipname)
      messagebox.showinfo('Succesful Transformation',' The Name of the adress is: '+str(a))
      print(a)
   except socket.herror as msg:
       messagebox.showerror('Error','host NOT found')
   except socket.gaierror as msg1: 
       messagebox.showerror('Error','Not valid ip')
          




     
  
   
          
