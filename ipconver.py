from tkinter import *
def ipconv(ip,ipclass):
    iplen = len(ip)   
    while   ip.isalpha():
        messagebox.showerror("ERROR",'No letters allowed in the ip form')
        raise Exception("problem")
    
                
    if (iplen<10 or iplen>15):
        messagebox.showerror("ERROR",'too small for an ip or too big')
        raise Exception("problem")
    
#findind the position of every dot of the ip given     
    p1 = ip.find('.')
    print('in the position',p1,'the first .')
    p2 = ip[p1+1:iplen].find('.')
    p2 = p2+p1+1
    print('in the position',p2,'the second .')    
    p3 = ip[p2+1:iplen].find('.')
    p3=p2+p3+1
    print('in the position',p3,'the third .')

#converting every part of the ip to integer to do the bitwise end 
    i1 = int(ip[0:p1])
    print('the conversion to integer gives:',i1)
    i2 = int(ip[p1+1:p2])
    print('the conversion to integer gives:',i2)
    i3 = int(ip[p2+1:p3])
    print('the conversion to integer gives:',i3)
    i4 = int(ip[p3+1:iplen])
    print('the conversion to integer gives:',i4)

    if (i1>255 or i2>255 or i3>255 or i4>255) :
        messagebox.showerror("ERROR",'not valid ip')
        raise Exception("problem")
        
        
        
    if ipclass=='A':
        
        submask='255.255.255.0'
        cp1 = (i1 & 255)
        cp2 = (i2 & 255)
        cp3 = (i3 & 255)
        cp4 = (i4 & 0)
        #converting the subnet mask to string inorder to write it to the database
        sp1 = str(cp1)
        sp2 = str(cp2)
        sp3 = str(cp3)
        sp4 = str(cp4)
        net_id =sp1+'.'+sp2+'.'+sp3+'.'+sp4
        messagebox.showinfo("NET-ID",'the net_id produced from the given ip is:'+net_id)
        
    elif ipclass=='B':
        submask='255.255.0.0'
        cp1 = (i1 & 255)
        cp2 = (i2 & 255)
        cp3 = (i3 & 0)
        cp4 = (i4 & 0)
        
        sp1 = str(cp1)
        sp2 = str(cp2)
        sp3 = str(cp3)
        sp4 = str(cp4)
        net_id =sp1+'.'+sp2+'.'+sp3+'.'+sp4
        messagebox.showinfo("NET-ID",'the net_id produced from the given ip is:'+net_id)
        
    elif ipclass=='C':
        submask='255.0.0.0'
        cp1 = (i1 & 255)
        cp2 = (i2 & 0)
        cp3 = (i3 & 0)
        cp4 = (i4 & 0)
        
        sp1 = str(cp1)
        sp2 = str(cp2)
        sp3 = str(cp3)
        sp4 = str(cp4)
        net_id =sp1+'.'+sp2+'.'+sp3+'.'+sp4
        messagebox.showinfo("NET-ID",'the net_id produced from the given ip is:'+net_id)
        
    else:
        messagebox.showerror("ERROR",'not valid class for an ip')
        raise Exception("problem")    
        
    return


 







        
        
    

    
          
            
      
      
    
