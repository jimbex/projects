from tkinter import *
from PIL import Image,ImageTk
import sqlite3 as sq

root = Tk()

img_file = Image.open("OIP.jpg")
img = ImageTk.PhotoImage(img_file)
mylabel = Label(root, image= img, bg = 'black', pady = 10)
mylabel.grid(row = 0, column = 0, columnspan = 5, ipadx = 120)



def Save():
	con = sq.connect('manage.sqlite')
	cur = con.cursor()
	query = '''Create Table If Not Exists Pasword(Website varchar(50), 
	            Username varchar(50), Password varchar(50))'''
	cur.execute(query)
	con.commit()

	jimbex = Tk()

	jimbex.title('jimbex password manager')


	a = Entry(jimbex, width = 70)
	a.grid(row = 1, column = 1, columnspan = 4, pady = 10, padx = 10, ipady = 5)
	b = Entry(jimbex, width = 70)
	b.grid(row = 2, column = 1, columnspan = 4, pady = 10, padx = 10, ipady = 5)
	c = Entry(jimbex, width = 70)
	c.grid(row = 3, column = 1, columnspan = 4, pady = 10, padx = 10, ipady = 5)

	web = Button(jimbex , text = "Website", padx = 15, pady = 3, state = 'disabled')
	use = Button(jimbex ,text = "Username", padx = 10, pady = 3, state = 'disabled')
	pas = Button(jimbex ,text = "Password", padx = 10, pady = 3, state = 'disabled')

	web.grid(row = 1, column = 0, pady = 10, padx = 10)
	use.grid(row = 2, column = 0, pady = 10, padx = 10)
	pas.grid(row = 3, column = 0, pady = 10, padx = 10)




	def function():
		con = sq.connect('manage.sqlite')
		cur = con.cursor()

		website = a.get()
		username = b.get()
		password = c.get()

		a.delete(0, END)
		b.delete(0, END)
		c.delete(0, END)

		querry = f'''Insert into Pasword(Website, Username, Password)
	            values(?, ?, ?)'''
		cur.execute(querry, (website, username, password))
		con.commit()

		form = f"""
		Website: {website}
		Username: {username}
		Password: {password}
		"""

		file = open('passwords.txt', 'a')
		file.write(form)
		file.close()
		con.close()


	submit = Button(jimbex, text = "save", padx = 20, pady = 10, command = function)
	submit.grid(row = 4, column = 4, pady = 10, padx = 10)

	jimbex.mainloop()


def Retrieve():
	root.quit()

	jago = Tk()

	jago.title('jimbex password manager')

	d = Entry(jago, width = 70)
	web = d.get()
	con = sq.connect('manage.sqlite')
	cur = con.cursor()


	d.grid(row = 1, column = 1, columnspan = 4, pady = 10, padx = 10, ipady = 5)

	ret = Button(jago, text = "Website", padx = 15, pady = 3)

	ret.grid(row = 1, column = 0, pady = 10, padx = 10)




	def function():
		con = sq.connect('manage.sqlite')
		cur = con.cursor()

		web = d.get()

		try:
			cur.execute('Select * from Pasword where Website = ?', (web,))
			fet = cur.fetchall()

			for x in fet:
				a = list(x)

			out = f'website:{a[0]}\nusername:{a[1]}\npassword:{a[2]}'
		except:
			out = 'No such website\nin the database'

		question = Label(jago, text = out, bg = 'white')
		question.grid(row = 2, column = 0)


	submit = Button(jago, text = "Retrieve", padx = 20, pady = 10, command = function)
	submit.grid(row = 2, column = 4, pady = 10, padx = 10)

	jago.mainloop()

save = Button(root, text = "Save", padx = 15, pady = 3, command = Save)
retrive = Button(root, text = "Retrieve", padx = 15, pady = 3, command = Retrieve)

save.grid(row = 1, column = 0, pady = 10, padx = 10)
retrive.grid(row = 1, column = 4, pady = 10, padx = 10)


root.mainloop()