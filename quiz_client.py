import socket
from threading import Thread
from tkinter import *

nickname = input("Choose your nickname: ")


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '189.34.56.7'
port = 7000

client.connect((ip_address, port))
print("Connected with the server...")

def receive():
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            if message == 'NICKNAME':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break
        
def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('utf-8'))

receive_thread = Thread(target=receive)
receive_thread.start()
write_thread = Thread(target=write)
write_thread.start()

class GUI:
    def __init__(self):
        self.Window = Tk()
        self.Window.withdraw()
        
        self.login = Toplevel()
        self.login.title("Login")
        
        self.go = Button(self.login,
                         text = "CONTINUE",
                         font = "Helvetica 14 bold",
                         command = lambda: self.goAhead(self.entryName.get()))
        
    def goAhead(self, name):
        self.login.destroy()
        self.layout(name)
        self.Name = name
        rcv = Thread(target=self.receive)
        rcv.start()
            
def layout(self,name):
		
		self.name = name
		self.Window.deiconify()
		self.Window.title("CHATROOM")
		self.Window.resizable(width = False,
							height = False)
		self.Window.configure(width = 470,
							height = 550,
							bg = "#17202A")
		self.labelHead = Label(self.Window,
							bg = "#17202A",
							fg = "#EAECEE",
							text = self.name ,
							font = "Helvetica 13 bold",
							pady = 5)
		
		self.labelHead.place(relwidth = 1)
		self.line = Label(self.Window,
						width = 450,
						bg = "#ABB2B9")
		
		self.line.place(relwidth = 1,
						rely = 0.07,
						relheight = 0.012)
		
		self.textCons = Text(self.Window,
							width = 20,
							height = 2,
							bg = "#17202A",
							fg = "#EAECEE",
							font = "Helvetica 14",
							padx = 5,
							pady = 5)
		
		self.textCons.place(relheight = 0.745,
							relwidth = 1,
							rely = 0.08)
		
		self.labelBottom = Label(self.Window,
								bg = "#ABB2B9",
								height = 80)
		
		self.labelBottom.place(relwidth = 1,
							rely = 0.825)
		
		self.entryMsg = Entry(self.labelBottom,
							bg = "#2C3E50",
							fg = "#EAECEE",
							font = "Helvetica 13")
		
		self.entryMsg.place(relwidth = 0.74,
							relheight = 0.06,
							rely = 0.008,
							relx = 0.011)
		
		self.entryMsg.focus()
		
		self.buttonMsg = Button(self.labelBottom,
								text = "Send",
								font = "Helvetica 10 bold",
								width = 20,
								bg = "#ABB2B9",
								command = lambda: self.sendButton(self.entryMsg.get()))
		
		self.buttonMsg.place(relx = 0.77,
							rely = 0.008,
							relheight = 0.06,
							relwidth = 0.22)
		
		self.textCons.config(cursor = "arrow")
		
		scrollbar = Scrollbar(self.textCons)

		scrollbar.place(relheight = 1,
						relx = 0.974)
		
		scrollbar.config(command = self.textCons.yview)
		
		self.textCons.config(state = DISABLED)

def sendButton(self, msg):
		self.textCons.config(state = DISABLED)
		self.msg=msg
		self.entryMsg.delete(0, END)
		snd= Thread(target = self.write)
		snd.start()

def show_message(self, message):
		self.textCons.config(state = NORMAL)
		self.textCons.insert(END, message+"\n\n")
		self.textCons.config(state = DISABLED)
		self.textCons.see(END)

def receive(self):
		while True:
			try:
				message = client.recv(2048).decode('utf-8')
				if message == 'NICKNAME':
					client.send(self.name.encode('utf-8'))
				else:
					self.show_message(message)
			except:
				print("An error occured!")
				client.close()
				break

def write(self):
		self.textCons.config(state=DISABLED)
		while True:
			message = (f"{self.name}: {self.msg}")
			client.send(message.encode('utf-8'))
			self.show_message(message)	
			break

g = GUI()