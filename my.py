from tkinter import *
import subprocess
import os

#top = Tk()
master = Tk()
master.geometry("300x170")
def helloCallBack():
	os.system("useradd %s username" %(username))
	#os.system("passwd %s" % username)
#master = Tk()
Label(master, text="First user").grid(row=0)
Label(master, text="Second user").grid(row=1)


e1 = Entry(master)
e2 = Entry(master)

username = e1.get()
#password = e2.get()

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)



B = Button(master, text = "Add", command = helloCallBack)
B.place(x=50,y=50)
mainloop()











