import socket
import time
import threading
from tkinter import *
 
root=Tk(className="ChatPhrase")
root.geometry("300x500")
root.config(bg="white")
 
def threadReceiveMsg():
    t=threading.Thread(target=recv)
    t.start()
 
 
def recv():
    listensocket=socket.socket()
    port=3050
    maxconnection=99
    ip=socket.gethostname()
    print(ip)
 
    listensocket.bind(('',port))
    listensocket.listen(maxconnection)
    (clientsocket,address)=listensocket.accept()
     
    while True:
        sendermessage=clientsocket.recv(1024).decode()     #utf-8 decoding
        if not sendermessage=="":
            time.sleep(5)
            lstbx.insert(0,"Client : "+sendermessage)
 
 
xr = 0
 
def SendMsg():
    global xr
    if xr == 0:
        s=socket.socket()
        hostname=''                                       #insert the destination system name
        port=4050
        s.connect((hostname,port))
        xr += 1

    msg=messagebox.get()
    lstbx.insert(0,"You : "+msg)
    s.send(msg.encode())                                   #utf-8 encoding
 
 
def threadSendMsg():
    th=threading.Thread(target=SendMsg)
    th.start()
 

startchatimage=PhotoImage(file='start.png')
 
buttons=Button(root,image=startchatimage,command=threadReceiveMsg,borderwidth=0)
buttons.place(x=90,y=10)
 
message=StringVar()
messagebox=Entry(root,textvariable=message,font=('calibre',10,'normal'),border=2,width=32)      #textbox 
messagebox.place(x=10,y=444)
 
sendmessageimg=PhotoImage(file='send.png')
 
sendmessagebutton=Button(root,image=sendmessageimg,command=threadSendMsg,borderwidth=0)
sendmessagebutton.place(x=260,y=440)
 
lstbx=Listbox(root,height=20,width=43)                  #entire chat history
lstbx.place(x=15,y=80)
 
user_name = Label(root,text =" Number" ,width=10)
 
root.mainloop()