from tkinter import *
import pyperclip
import random
from PIL import Image
from PIL import ImageTk

root = Tk()
root.geometry("1200x700")
passwrd = StringVar()
passlen = IntVar()
passlen.set(0)

root.configure(bg='pink')

def generate(): 
	pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
			'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
			'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
			'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
			'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
			'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
			'9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
			'*', '(', ')']
	password = ""
	for x in range(passlen.get()):
		password = password + random.choice(pass1)
	passwrd.set(password)

def copyclipboard():
	random_password = passwrd.get()
	pyperclip.copy(random_password)
	label3=Label(root,text="Password copied to clipboard successfuly:"+random_password).place(x=520,y=400)

image = Image.open("mickey.jpg")
 
resize_image = image.resize((200, 150))
 
img = ImageTk.PhotoImage(resize_image)

label1 = Label(image=img,bg='purple')
label1.image =img
label1.place(x=0,y=0)
label2=Label(root,text="Mickey Foundation",font="Courier 10 bold").place(x=20,y=180)
Label(root, text="Random Strong Password Generator", font="Courier 30 bold").pack()
Label(root, text="Enter Size of Password",font="Courier 15 bold").place(x=485,y=150)
Entry(root, textvariable=passlen,width=20,font="Arial 12").place(x=530,y=200)
Button(root, text="Tap to get", command=generate).place(x=585,y=250)
Entry(root, textvariable=passwrd,width=20,font='Arial 12').place(x=530,y=300)
Button(root, text="Tap to copy clipboard", command=copyclipboard).place(x=560,y=350)
label4=Label(root,text="Copyright Pankaj More 2023").place(x=550,y=450)
root.mainloop()
