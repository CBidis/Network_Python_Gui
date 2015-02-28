from tkinter import *
from PIL import ImageTk
from PIL import Image

#main function callings
def ips():
   from ipconver import ipconv
   ipconv(v1.get(),v2.get())
           
def pingtr():
   from pings import pingad
   pingad(v3.get())
   
def sspings():
   from pings import dbping
   dbping(v4.get())
   
def dnstran():
   from pings import dnstoip
   dnstoip(v5.get())
   #finding the position of the last dot to create the staritng ip for the ping     
   p1 = dnstoip.addr.find('.')
   p2 = dnstoip.addr[p1+1:len(dnstoip.addr)].find('.')
   p2 = p2+p1+1  
   p3 = dnstoip.addr[p2+1:len(dnstoip.addr)].find('.')
   p3=p2+p3+1
   startip = dnstoip.addr[0:p3+1]
   v3.set(startip)
   
def iptran():
   from pings import iptodns
   iptodns(v6.get())
   p1 = v6.get().find('.')
   p2 = v6.get()[p1+1:len(v6.get())].find('.')
   p2 = p2+p1+1  
   p3 = v6.get()[p2+1:len(v6.get())].find('.')
   p3=p2+p3+1
   startip = v6.get()[0:p3+1]
   v3.set(startip)
   


#set basic window information and size
ipg = Tk()
ipg.title("IP-Conversion")
ipg.minsize(1024, 768)
ipg.resizable(width=FALSE, height=FALSE)
#set basic window information and size
#for background image!
background_image=ImageTk.PhotoImage(file="C:/Users/chrigeta/Desktop/pythont/linux.jpg")
background_label = Label(ipg, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
#for background image!
#adding buttons and functionality
#main buttons
b = Button(ipg,text ="Net-ID", command =ips,height=5, width=50,bg='cyan')
c = Button(ipg,text ="Exit", command =quit,height=5, width=50,bg='cyan')
d = Button(ipg,text ="Ping Adrress", command =pingtr,height=5, width=50,bg='cyan')
e = Button(ipg,text ="Show the entries of succesful pings", command =sspings,height=5, width=50,bg='cyan')
f = Button(ipg,text ="DNS to IP Ping", command =dnstran,height=5, width=50,bg='cyan')
g = Button(ipg,text ="IP to DNS Ping", command =iptran,height=5, width=50,bg='cyan')
#main buttons
#entry widgets
v1 = StringVar()
eip = Entry(textvariable=v1)
eip.place(x=50,y=0,relheight=0.05,relwidth=0.2)
v1.set('give the ip number')
t1=v1.get()
#entry widgets
v2 = StringVar()
ecl = Entry(textvariable=v2)
ecl.place(x=780,y=0,relheight=0.05,relwidth=0.2)
v2.set('give the class IP')
t2=v2.get()
#entry widgets
v3 = StringVar()
pip = Entry(textvariable=v3)
pip.place(x=70,y=430,relheight=0.05,relwidth=0.2)
v3.set('Give the Starting ip'+'(ex.192.168.1.)')
t3=v3.get()
#entry widgets
v4 = StringVar()
spip = Entry(textvariable=v4)
spip.place(x=740,y=430,relheight=0.05,relwidth=0.2)
v4.set('Write the ip to see the entries')
t4=v4.get()
#entry widgets
v5 = StringVar()
dnpip = Entry(textvariable=v5)
dnpip.place(x=410,y=540,relheight=0.05,relwidth=0.2)
v5.set('Give the DNS please')
t5=v5.get()
#entry widgets
v6 = StringVar()
ippip = Entry(textvariable=v6)
ippip.place(x=410,y=190,relheight=0.05,relwidth=0.2)
v6.set('Give the IP please')
t6=v6.get()
#entry widgets


#packing everything to frame
b.pack(side="top")
c.pack(side="bottom")
d.pack(side="left")
e.pack(side="right")
f.place(x=330,y=450)
g.place(x=330,y=230)

ipg.mainloop()
