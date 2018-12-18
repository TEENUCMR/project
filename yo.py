import tkinter as tk


from tkinter import *


r = Tk()


L1 = Label(r, text="TEXT")
L1.pack( side = TOP)
E1 = Entry(r, bd =5)
E1.pack(side = TOP)

def myaction():
	f=E1.get()
	print(f)
	d=var.get()



	if(d==1):
		alpha="abcdefghijklmnopqrstuvwxyz"
		key=3
		newmsg=''
		for character in f:
			if character in alpha:
				posi=alpha.find(character)
				nposi=(posi+key)%26
				newcar=alpha[nposi]
				newmsg +=newcar
				L3.config(text=newmsg)
			else:
				newmsg +=character
				L3.config(text=newmsg)

		


	elif(d==2):
		alpha="abcdefghijklmnopqrstuvwxyz"
		key=3
		newmsg=''
		for character in f:
			if character in alpha:
				posi=alpha.find(character)
				nposi=(posi-key)%26
				newcar=alpha[nposi]
				newmsg +=newcar
				L3.config(text=newmsg)
			else:
				newmsg +=character
				L3.config(text=newmsg)
		

	elif(d==3):
		def key():
			u=E.get()
			v=E0.get()
			w=E7.get()

			b=k.get()
			import smtplib
			#IMPORT SMTPLIB
			#TO SEND EMAIL
			smtpserver=smtplib.SMTP("smtp.gmail.com",587)
			smtpserver.starttls()
			#TO USE TLS

			receiver=u
			sender=v
			password=w
			#LOGIN IN TO YOUR ACC
			smtpserver.login(sender,password)

			if(b==1):
				alpha="abcdefghijklmnopqrstuvwxyz"
				key=3
				newmsg=''
				for character in f:
					if character in alpha:
						posi=alpha.find(character)
						nposi=(posi+key)%26
						newcar=alpha[nposi]
						newmsg +=newcar
						L3.config(text=newmsg)
					else:
						newmsg +=character
						L3.config(text=newmsg)
				

			elif(b==2):
				alpha="abcdefghijklmnopqrstuvwxyz"
				key=3
				newmsg=''
		
				for character in f:
					if character in alpha:
						posi=alpha.find(character)
						nposi=(posi-key)%26
						newcar=alpha[nposi]
						newmsg +=newcar
						L3.config(text=newmsg)
					else:
						newmsg +=character
						L3.config(text=newmsg)
				
			
			smtpserver.sendmail(sender,receiver,newmsg)
			L9= Label(text="YOUR MESSAGE HAS BEEN SENT")
			L9.pack()
			smtpserver.close()

		
		L = Label(text="To-")
		L.pack( side = LEFT)
		E= Entry(bd =5)
		E.pack(side =LEFT)

		L0 = Label(text="From-")
		L0.pack( side = LEFT)
		E0= Entry(bd =5)
		E0.pack(side =LEFT)

		L7 = Label(text="Password-")
		L7.pack( side = LEFT)
		E7= Entry(bd =5)
		E7.pack(side =LEFT)



		k = IntVar()
		R = Radiobutton(text="Encrypt", variable=k, value=1)
		R.pack()
		R0 = Radiobutton(text="Decrypt", variable=k, value=2)
		R0.pack()
		button = tk.Button(text="DONE", width=25, command=key) 
		button.pack() 

		

		





var = IntVar()
R1 = Radiobutton(r, text="code", variable=var, value=1)
R1.pack( anchor = W )

R2 = Radiobutton(r, text="decode", variable=var, value=2)
R2.pack( anchor = W )

R3 = Radiobutton(r, text="mail", variable=var, value=3)
R3.pack( anchor = W)



r.title('secret message') 
button = tk.Button(r, text='Submit', width=25, command=myaction) 
button.pack() 


label = Label(r)
label.pack()
L3 = Label(text="OUTPUT")
L3.pack( side = TOP)

r.mainloop()

exit()