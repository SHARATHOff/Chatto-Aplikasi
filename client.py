import socket
from tkinter import *
from tkinter import messagebox
import time
import socket
clietname = []
def main():
    root = Tk()
    root.geometry("400x400")
    root.configure(bg="orange")
    root.title("Chat Application")
    root.resizable(False,False)
    hedding = Label(root,text="CLIENT",font="none 70 bold",bg="orange red",fg="white")
    hedding.pack(side=TOP)
    serverbutton = Button(root,text="Client",font="none 55 bold",bg="orange red",fg="white",command=lambda:[root.destroy(),clientconnect()])
    serverbutton.pack(side=BOTTOM,expand=True)
    root.mainloop()
def clientconnect():
    global hostentry,portentry
    clientgui = Tk()
    clientgui.title("[HOST]=> and [PORT]=>")
    clientgui.configure(bg="orange")
    clientgui.geometry("400x500")
    heddign = Label(clientgui,text="Connecting...",font="none 45 bold",bg="orange red",fg="white")
    heddign.pack(side=TOP,expand=True)
    hostentry = Entry(clientgui,font="none 25 bold",bg="orange red",fg="white")
    hostentry.pack(side=TOP,expand=True)
    portentry = Entry(clientgui,font="none 25 bold",bg="orange red",fg="white")
    portentry.pack(side=TOP,expand=True)
    connectButon = Button(clientgui,text="Connect",font="none 25 bold",bg="orange red",fg="white",command=fun2)
    connectButon.pack(side=BOTTOM,expand=True)
    clientgui.mainloop()
def fun2():
    global address , s
    host = hostentry.get()
    port = portentry.get()
    host = host
    port = int(port)
    address = (host,port)
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    while True:
        try:
            s.connect(address)
            messaging()
            break
        except:
            exit()


def messaging():
    global messbox,messageentry,messagegui
    messagegui = Tk()
    messagegui.resizable(False,False)
    messagegui.title("Client...............")
    messagegui.configure(bg="orange")
    messagegui.geometry("600x600")
    messbox = Text(messagegui,height=18,font="none 18 ",bg="skyblue")
    messbox.pack()
    messageentry = Entry(messagegui,font="none 18 ",bg="skyblue",width=30)
    messageentry.pack(expand=True)
    sendbutton = Button(messagegui,text="SEND",font="none 15 ",bg="skyblue",command=all)
    sendbutton.pack()
    messagegui.mainloop()
def all():
    recvmessage()
    messagegui.after(1000,sendmessage)
def sendmessage():
    message = ""
    message = messageentry.get()
    messageentry.delete(0,END)
    messbox.insert("1.0", f"Me: {message} \n")
    s.send(message.encode())
def recvmessage():   
    inmess = s.recv(1024).decode()
    messbox.insert("1.0", f"Client: {inmess} \n")

if __name__=="__main__":
    main()