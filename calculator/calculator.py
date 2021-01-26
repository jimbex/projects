from tkinter import *
import math

root = Tk()

root.title("learn")
root.iconbitmap("")


def statistics():

	stats = Tk()

	stats.title("statistics")

	e = Entry(stats, width  = 50)
	e.grid(row = 0, column = 0, pady = 10, columnspan = 5)
	global count
	global total

	total = 0
	count = 0
	def button_click(number):
	#e.delete(0, END)
		current = e.get()
		e.delete(0, END)
		e.insert(0, str(current) + str(number))




	def avg():
		global num
		global inp
		inp = "next"
		f_num = list(e.get().split(" "))
		e.delete(0, END)
		total = 0
		count = 0
		for x in f_num:
			total = total + float(x)
			count = count + 1

		#x = list(map(int, f_num.split(",")))
		e.delete(0, END)
		e.insert(0, total / count)


	def variance():
		global num
		global inp
		inp = "next"
		f_num = array(e.get().split(" "))
		e.delete(0, END)
		total = 0
		count = 0
		for x in f_num:
			total = total + float(x)
			count = count + 1
			total = total / count
		
		a = 0
		sums = 0

		while a < count:
			num = float(f_num[a]) - total
			sums = sums + (num ** 2) 
			a = a + 1

		sums = sums / a
		e.insert(0, sums)

	

	def sd():
		global num
		global inp
		inp = "next"
		f_num = array(e.get().split(" "))
		e.delete(0, END)
		total = 0
		count = 0
		for x in f_num:
			total = total + float(x)
			count = count + 1
			total = total / count
		
		a = 0
		sums = 0

		while a < count:
			num = float(f_num[a]) - total
			sums = sums + (num ** 2) 
			a = a + 1

		sums = sums / a
		e.insert(0, math.sqrt(sums))



	


	def clear():
		e.delete(0, END)



	


	num1 = Button(stats, text = "1", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(1))
	num2 = Button(stats, text = "2", padx = 31, pady = 20, fg = "black", bg = "white", command = lambda: button_click(2))
	num3 = Button(stats, text = "3", padx = 32, pady = 20, fg = "black", bg = "white", command = lambda: button_click(3))
	num4 = Button(stats, text = "4", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(4))
	num5 = Button(stats, text = "5", padx = 31, pady = 20, fg = "black", bg = "white", command = lambda: button_click(5))
	num6 = Button(stats, text = "6", padx = 32, pady = 20, fg = "black", bg = "white", command = lambda: button_click(6))
	num7 = Button(stats, text = "7", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(7))
	num8 = Button(stats, text = "8", padx = 31, pady = 20, fg = "black", bg = "white", command = lambda: button_click(8))
	num9 = Button(stats, text = "9", padx = 32, pady = 20, fg = "black", bg = "white", command = lambda: button_click(9))
	num0 = Button(stats, text = "0", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(0))
	point = Button(stats, text = ".", padx = 32, pady = 20, fg = "black", bg = "white", command = lambda: button_click("."))
	next_num = Button(stats, text = "next", padx = 24, pady = 20, fg = "black", bg = "white", command = lambda: button_click(" "))
	mean = Button(stats, text = "mean", padx = 22, pady = 20, fg = "black", bg = "white", command = avg)
	var = Button(stats, text = "σ2", padx = 30, pady = 20, fg = "black", bg = "white", command = variance)
	erase = Button(stats, text = "clear", padx = 24, pady = 20, fg = "black", bg = "white", command = clear)
	sdev = Button(stats, text = "σ", padx = 32, pady = 20, fg = "black", bg = "white", command = sd)

	num1.grid(row = 1, column = 1)
	num2.grid(row = 1, column = 2)
	num3.grid(row = 1, column = 3)
	num4.grid(row = 2, column = 1)
	num5.grid(row = 2, column = 2)
	num6.grid(row = 2, column = 3)
	num7.grid(row = 3, column = 1)
	num8.grid(row = 3, column = 2)
	num9.grid(row = 3, column = 3)
	num0.grid(row = 4, column = 1)
	point.grid(row = 4, column = 2)
	next_num.grid(row = 4, column = 3)
	mean.grid(row = 1, column = 4)
	var.grid(row = 2, column = 4)
	erase.grid(row = 3, column = 4)
	sdev.grid(row = 4, column = 4)


	stats.mainloop()

def motion():
	jimbex = Tk()
	jimbex.title("Physiscs Calculator")
	#motion all kinds
	e = Entry(jimbex, width = 40)
	e.grid(row = 0, column = 0, columnspan = 4, pady = 5)

	def button_click(number):
			#e.delete(0, END)
			current = e.get()
			e.delete(0, END)
			e.insert(0, str(current) + str(number))


	def initial():
		f_num = e.get()
		global ini
		global numb1
		ini = "ini"
		numb1 = int(f_num)
		e.delete(0, END)
			
			

	def final():
		s_num = e.get()
		global fin
		global parameter
		global numb2
		parameter = "fin"
		fin = "fin"
		numb2 = int(s_num)
		e.delete(0, END)

	def length():
		t_num = e.get()
		global parameter
		global numb3
		parameter = "len"
		numb3 = int(t_num)
		e.delete(0, END)
		
		

	def seconds():
		i_num = e.get()
		global parameter
		global fin
		global numb4
		fin = "sec"
		parameter = "sec"
		numb4 = int(i_num)
		e.delete(0, END)


	def acceleration():
		a_num = e.get()
		global acc
		global numb5
		acc = "acc"
		numb5 = int(a_num)
		e.delete(0, END)

	def find_ini():
		if acc == "acc":
			if parameter == "sec" and fin == "fin":
				e.insert(0, numb2 - (numb5 * numb4))
			if fin == "fin" and parameter == "len":
				e.insert(0, sqrt((numb2 * numb2) - (numb3 * numb5 * 2)))
			if parameter == "len" and fin == "sec":
				e.insert(0, (numb3 - (0.5 * numb5 * (numb4 * numb4))) / numb4)
		
		

	def find_len():
		if acc == "acc":
			if ini == "ini" and parameter == "sec":
				e.insert(0, (numb1 * numb4) + (0.5 * numb5 *(numb4 * numb4)) )
			if ini == "ini" and parameter == "fin":
				e.insert(0, ((numb2 * numb2) - (numb1 * numb1)) / (2 * numb5))

	def find_fin():

		if acc == "acc":
			if ini == "ini" and parameter == "sec":
				e.insert(0, numb1 + (numb5 * numb4) )
			if ini == "ini" and parameter == "len":
				e.insert(0, sqrt((numb1 * numb1) + (2 * numb5 * numb3)))

			
			
	def find_acc():
		if ini == "ini":
			if fin == "fin" and parameter == "sec":
				e.insert(0, (numb2 - numb1) / numb4)
			if fin == "fin" and parameter == "len":
				e.insert(0, ((numb2 * numb2) - (numb1 * numb1)) / (2 * numb3))
			if fin == "sec" and parameter == "len":
				e.insert(0, (numb3 - (numb1 * numb4)) / (0.5 * (numb4 * numb4)))

	def find_time():
		if ini == "ini" and acc == "acc":
			if fin == "fin":
				e.insert(0, (numb2 - numb1) / numb5)






	def find():
		e.delete(0, END)
		


	num1 = Button(jimbex, text = "1", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(1))
	num2 = Button(jimbex, text = "2", padx = 31, pady = 20, fg = "black", bg = "white", command = lambda: button_click(2))
	num3 = Button(jimbex, text = "3", padx = 32, pady = 20, fg = "black", bg = "white", command = lambda: button_click(3))
	num4 = Button(jimbex, text = "4", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(4))
	num5 = Button(jimbex, text = "5", padx = 31, pady = 20, fg = "black", bg = "white", command = lambda: button_click(5))
	num6 = Button(jimbex, text = "6", padx = 32, pady = 20, fg = "black", bg = "white", command = lambda: button_click(6))
	num7 = Button(jimbex, text = "7", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(7))
	num8 = Button(jimbex, text = "8", padx = 31, pady = 20, fg = "black", bg = "white", command = lambda: button_click(8))
	num9 = Button(jimbex, text = "9", padx = 32, pady = 20, fg = "black", bg = "white", command = lambda: button_click(9))
	num0 = Button(jimbex, text = "0", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(0))
	let1 = Button(jimbex, text = "u", padx = 30, pady = 20, fg = "black", bg = "white", command = find_ini)
	let2 = Button(jimbex, text = "v", padx = 30, pady = 20, fg = "black", bg = "white", command = find_fin)
	let3 = Button(jimbex, text = "s", padx = 32, pady = 20, fg = "black", bg = "white", command = find_len)
	let4 = Button(jimbex, text = "t", padx = 31, pady = 20, fg = "black", bg = "white", command = lambda: button_click("t"))
	let5 = Button(jimbex, text = "a", padx = 30, pady = 20, fg = "black", bg = "white", command = find_acc)
	point = Button(jimbex, text = ".", padx = 32, pady = 20, fg = "black", bg = "white", command = lambda: button_click("."))
	F_vel = Button(jimbex, text = "Fvel", padx = 28, pady = 20, fg = "black", bg = "white", command = final)
	I_vel = Button(jimbex, text = "Ivel", padx = 28, pady = 20, fg = "black", bg = "white", command = initial)
	Distance = Button(jimbex, text = "Dist", padx = 28, pady = 20, fg = "black", bg = "white", command = length)
	time = Button(jimbex, text = "Time", padx = 25, pady = 20, fg = "black", bg = "white", command = seconds)
	answer = Button(jimbex, text = "clear", padx = 22, pady = 20, fg = "black", bg = "white", command = find)
	accelerate = Button(jimbex, text = "Accl", padx = 27, pady = 20, fg = "black", bg = "white", command = acceleration)






	num1.grid(row = 1, column = 0)
	num2.grid(row = 1, column = 1)
	num3.grid(row = 1, column = 2)
	num4.grid(row = 2, column = 0)
	num5.grid(row = 2, column = 1)
	num6.grid(row = 2, column = 2)
	num7.grid(row = 3, column = 0)
	num8.grid(row = 3, column = 1)
	num9.grid(row = 3, column = 2)
	num0.grid(row = 4, column = 0)
	point.grid(row = 4, column = 1)
	F_vel.grid(row = 4, column = 3)
	I_vel.grid(row = 1, column = 3)
	let1.grid(row = 5, column = 0)
	let2.grid(row = 5, column = 1)
	let3.grid(row = 5, column = 2)
	let4.grid(row = 6, column = 1)
	let5.grid(row = 6, column = 0)
	Distance.grid(row = 2, column = 3)
	time.grid(row = 3, column = 3)
	answer.grid(row = 4, column = 2)
	accelerate.grid(row = 5, column = 3)


def Projectile():
	jimbex = Tk()

	jimbex.title("Projectile")

	#motion all kinds

	e = Entry(jimbex, width = 40)
	e.grid(row = 0, column = 0, columnspan = 4, pady = 5)

	def button_click(number):
			#e.delete(0, END)
			current = e.get()
			e.delete(0, END)
			e.insert(0, str(current) + str(number))


	def Time():
		f_num = e.get()
		global parameter
		global numb1
		parameter = "time"
		numb1 = int(f_num)
		e.delete(0, END)


	def Hmax():
		f_num = e.get()
		global parameter
		global numb2
		parameter = "Height"
		numb2 = int(f_num)
		e.delete(0, END)


	def Range():
		f_num = e.get()
		global parameter
		global numb3
		parameter = "range"
		numb3 = int(f_num)
		e.delete(0, END)

	def Rmax():
		f_num = e.get()
		global parameter
		global numb4
		parameter = "rmax"
		numb4 = int(f_num)
		e.delete(0, END)

	def ini():
		f_num = e.get()
		global parameter
		global numb4
		parameter = "ini"
		numb4 = int(f_num)
		e.delete(0, END)

	def tita():
		f_num = e.get()
		global parameter
		global numb5
		parameter = "tita"
		numb5 = int(f_num)
		e.delete(0, END)

	def find_time():
		e.insert(0, (2 * numb4 * math.sin(math.radians(numb5))) / 10)

	def find_Hmax():
		e.insert(0, ((numb4 * numb4) * (math.sin(math.radians(numb5)) * math.sin(math.radians(numb5)))) / 20 )

	def find_range():
		e.insert(0, ((numb4 * numb4) * math.sin(math.radians(numb5 * 2))) / 10)

	def find_Rmax():
		e.insert(0, (numb4 * numb4) / 10)

	def find_u():
		if parameter == "time":
			e.insert(0, (10 * numb1) / (2 * math.sin(math.radians(numb5))))
		if parameter == "Height":
			e.insert(0, math.sqrt(()))
		if parameter == "range":
			e.insert(0, math.sqrt((numb3 * 10) / math.sin(math.radians(numb5))))
		if parameter == "rmax":
			e.insert(0, math.sqrt(numb4 * 10))

	def find_tita():
		if parameter == "time":
			e.insert(0, (10 * numb1) / (2 * math.sin(math.radians(numb5))))
		if parameter == "Height":
			e.insert(0, math.sqrt())
		if parameter == "range":
			e.insert(0, math.degrees(math.asin((numb3 * 10) / (2 * (numb4 * numb4)))))

	def clear():
		e.delete(0, END)
		






	num1 = Button(jimbex, text = "1", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(1))
	num2 = Button(jimbex, text = "2", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(2))
	num3 = Button(jimbex, text = "3", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(3))
	num4 = Button(jimbex, text = "4", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(4))
	num5 = Button(jimbex, text = "5", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(5))
	num6 = Button(jimbex, text = "6", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(6))
	num7 = Button(jimbex, text = "7", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(7))
	num8 = Button(jimbex, text = "8", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(8))
	num9 = Button(jimbex, text = "9", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(9))
	num0 = Button(jimbex, text = "0", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(0))
	point = Button(jimbex, text = ".", padx = 31, pady = 20, fg = "black", bg = "white", command = lambda: button_click("."))
	Height = Button(jimbex, text = "Hmax", padx = 17, pady = 20, fg = "black", bg = "white", command = Hmax)
	sec = Button(jimbex, text = "time", padx = 20, pady = 20, fg = "black", bg = "white", command = Time)
	rang = Button(jimbex, text = "range", padx = 17, pady = 20, fg = "black", bg = "white", command = Range)
	maxR = Button(jimbex, text = "Rmax", padx = 18, pady = 20, fg = "black", bg = "white", command = Rmax)
	speed = Button(jimbex, text = "U", padx = 30, pady = 20, fg = "black", bg = "white", command = ini)
	teeta = Button(jimbex, text = "θ", padx = 30, pady = 20, fg = "black", bg = "white", command = tita)
	find_height = Button(jimbex, text = "Hmax =", padx = 18, pady = 20, fg = "black", bg = "white", command = find_Hmax)
	find_sec = Button(jimbex, text = "t =", padx =  31, pady = 20, fg = "black", bg = "white", command = find_time)
	find_rang = Button(jimbex, text = "Range =", padx = 18, pady = 20, fg = "black", bg = "white", command = find_range)
	find_maxr = Button(jimbex, text = "Rmax =", padx = 18, pady = 20, fg = "black", bg = "white", command = find_Rmax)
	find_speed = Button(jimbex, text = "u =", padx = 30, pady = 20, fg = "black", bg = "white", command = find_u)
	find_teeta = Button(jimbex, text = "θ =", padx = 30, pady = 20, fg = "black", bg = "white", command = find_tita)
	erase = Button(jimbex, text = "clear", padx = 20, pady = 20, fg = "black", bg = "white", command = clear)







	num1.grid(row = 1, column = 0)
	num2.grid(row = 1, column = 1)
	num3.grid(row = 1, column = 2)
	num4.grid(row = 2, column = 0)
	num5.grid(row = 2, column = 1)
	num6.grid(row = 2, column = 2)
	num7.grid(row = 3, column = 0)
	num8.grid(row = 3, column = 1)
	num9.grid(row = 3, column = 2)
	num0.grid(row = 4, column = 0)
	point.grid(row = 4, column = 1)
	Height.grid(row = 4, column = 2)
	sec.grid(row = 5, column = 0)
	rang.grid(row = 5, column = 1)
	maxR.grid(row = 5, column = 2)
	erase.grid(row = 6, column = 2)
	speed.grid(row = 6, column = 0)
	teeta.grid(row = 6, column = 1)
	find_height.grid(row = 1, column = 3)
	find_sec.grid(row = 2, column = 3)
	find_rang.grid(row = 3, column = 3)
	find_maxr.grid(row = 4, column = 3)
	find_speed.grid(row = 5, column = 3)
	find_teeta.grid(row = 6, column = 3)




	jimbex.mainloop()

def arithmetic():
	jago = Tk()
	jago.title("Jimbex Calculator") 
	e = Entry(jago, width  = 70)
	e.grid(row = 0, column = 0, pady = 10, columnspan = 7)
	def button_click(number):
		#e.delete(0, END)
		current = e.get()
		e.delete(0, END)
		e.insert(0, str(current) + str(number))

	def delete():
		e.delete(0, END)

	def add():
		f_num = e.get()
		global num
		global maths
		maths = "add"
		num = float(f_num)
		e.delete(0, END)

	def multiply():
		f_num = e.get()
		global num
		global maths
		maths = "multiply"
		num = float(f_num)
		e.delete(0, END)
	

	def divide():
		f_num = e.get()
		global num
		global maths	
		maths = "divide"
		num = float(f_num)
		e.delete(0, END)

	def subtract():
		f_num = e.get()
		global num
		global maths
		maths = "subtract"
		num = float(f_num)
		e.delete(0, END)

	def powe():
		f_num = e.get()
		global num
		global maths
		maths = "power"
		num = float(f_num)
		e.delete(0, END)

	def square():
		global maths
		global f_num
		maths = "square"
		e.delete(0, END)


	def cent():
		f_let = e.get()
		global num
		global maths
		maths = "percent"
		num = float(f_num)
		e.delete(0, END)

	def cosine():
		global maths
		global f_num
		maths = "cos"
		e.delete(0, END)

	def sine():
		global maths
		global f_num
		maths = "sin"
		e.delete(0, END)

	def tangent():
		global maths
		global f_num
		maths = "tan"
		e.delete(0, END)

	def arccos():
		global maths
		global f_num
		maths = "anticos"
		e.delete(0, END)

	def arcsin():
		global maths
		global f_num
		maths = "antisin"
		e.delete(0, END)

	def arctan():
		global maths
		global f_num
		maths = "cotan"
		e.delete(0, END)
	

	

	def equal():
		global maths
		s_num = e.get()
		final = float(s_num)
		e.delete(0, END)

		if maths == "add":
			e.insert(0, num + final)
			e.insert(0, str(num) + " + " + s_num + " = ")

		if maths == "subtract":
			e.insert(0, num - final)

		if maths == "multiply":
			e.insert(0, num * final)

		if maths == "divide":
			e.insert(0, num / final)

		if maths == "power":
			e.insert(0, num ** final)

		if maths == "square":
			ans = math.sqrt(final)
			e.insert(0, "_/" + s_num + " = " + str(ans))

		if maths == "cos":
			ans = math.cos(math.radians(final))
			e.insert(0, "cos" + s_num + " = " + str(ans))

		if maths == "sin":
			ans = math.sin(math.radians(final))
			e.insert(0, "_sin" + s_num + " = " + str(ans))

		if maths == "tan":
			ans = math.tan(math.radians(final))
			e.insert(0, "tan" + s_num + " = " + str(ans))

		if maths == "anticos":
			ans = math.degrees(math.acos(final))
			e.insert(0, "arccos" + s_num + " = " + str(ans))

		if maths == "antisin":
			ans = math.degrees(math.asin(final))
			e.insert(0, "arcsec" + s_num + " = " + str(ans))
		
		if maths == "cotan":
			ans = math.degrees(math.atan(final))
			e.insert(0, "cot" + s_num + " = " + str(ans))
		
		









	num1 = Button(jago, text = "1", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(1))
	num2 = Button(jago, text = "2", padx = 31, pady = 20, fg = "black", bg = "white", command = lambda: button_click(2))
	num3 = Button(jago, text = "3", padx = 32, pady = 20, fg = "black", bg = "white", command = lambda: button_click(3))
	num4 = Button(jago, text = "4", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(4))
	num5 = Button(jago, text = "5", padx = 31, pady = 20, fg = "black", bg = "white", command = lambda: button_click(5))
	num6 = Button(jago, text = "6", padx = 32, pady = 20, fg = "black", bg = "white", command = lambda: button_click(6))
	num7 = Button(jago, text = "7", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(7))
	num8 = Button(jago, text = "8", padx = 31, pady = 20, fg = "black", bg = "white", command = lambda: button_click(8))
	num9 = Button(jago, text = "9", padx = 32, pady = 20, fg = "black", bg = "white", command = lambda: button_click(9))
	num0 = Button(jago, text = "0", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(0))
	point = Button(jago, text = ".", padx = 32, pady = 20, fg = "black", bg = "white", command = lambda: button_click("."))
	cos = Button(jago, text = "cos", padx= 26, pady = 20, fg = "black", bg = "white", command = cosine)
	sin = Button(jago, text = "sin", padx= 27.5, pady = 20, fg = "black", bg = "white", command = sine)
	tan = Button(jago, text = "tan", padx= 26.5, pady = 20, fg = "black", bg = "white", command = tangent)
	cosec = Button(jago, text = "arccos", padx= 18, pady = 20, fg = "black", bg = "white", command = arccos)
	sec = Button(jago, text = "arcsin", padx= 20, pady = 20, fg = "black", bg = "white", command = arcsin)
	cot = Button(jago, text = "arctan", padx= 19, pady = 20, fg = "black", bg = "white", command = arctan)
	
# fg fore ground colour
# bg back ground colour
# command what to do
# padx horizontal size
# pady vertical size


	plus = Button(jago, text = "+", padx = 30, pady = 20, fg = "black", bg = "white", command = add)
	subtr = Button(jago, text = "-", padx = 31, pady = 20, fg = "black", bg = "white", command = subtract)
	div = Button(jago, text = "/", padx = 31, pady = 20, fg = "black", bg = "white", command = divide)
	mult = Button(jago, text = "x", padx = 31, pady = 20, fg = "black", bg = "white", command = multiply)
	power = Button(jago, text = "^", padx = 31, pady = 20, fg = "black", bg = "white", command = powe)
	sqare = Button(jago, text = "_/", padx = 30, pady = 20, fg = "black", bg = "white", command = square)
	percent = Button(jago, text = "%", padx = 30, pady = 20, fg = "black", bg = "white", command = cent)
#cos = Button(jago, text = "cos", padx = 30, pady = 20, fg = "black", bg = "white")
#sin = Button(jago, text = "sin", padx = 30, pady = 20, fg = "black", bg = "white")
#tan = Button(jago, text = "tan", padx = 30, pady = 20, fg = "black", bg = "white")
#cosec = Button(jago, text = "cosec", padx = 30, pady = 20, fg = "black", bg = "white")
#sec = Button(jago, text = "sec", padx = 30, pady = 20, fg = "black", bg = "white")
#cot = Button(jago, text = "cot", padx = 30, pady = 20, fg = "black", bg = "white")
	clear = Button(jago, text = "clear", padx = 174.5, pady = 20, fg = "black", bg = "white", command = delete)
	equals = Button(jago, text = "=", padx = 183.5, pady = 20, fg = "black", bg = "white", command = equal)
	back = Button(jago, text = "back", padx = 22, pady = 20, fg = "black", bg = "white")
	quit = Button(jago, text = "quit", padx = 24, pady = 20, fg = "black", bg = "white", command = jago.quit)

	num1.grid(row = 1, column = 1)
	num2.grid(row = 1, column = 2)
	num3.grid(row = 1, column = 3)
	num4.grid(row = 2, column = 1)
	num5.grid(row = 2, column = 2)
	num6.grid(row = 2, column = 3)
	num7.grid(row = 3, column = 1)
	num8.grid(row = 3, column = 2)
	num9.grid(row = 3, column = 3)
	num0.grid(row = 4, column = 1)
	point.grid(row = 4, column = 2)
	plus.grid(row = 1, column = 4)
	subtr.grid(row = 2, column = 4)
	div.grid(row = 3, column = 4)
	mult.grid(row = 4, column = 4)
	power.grid(row = 4, column = 3)
	sqare.grid(row = 1, column = 5)
	percent.grid(row = 2, column = 5)
	back.grid(row = 3, column = 5)
	quit.grid(row = 4, column = 5)
	cos.grid(row = 1, column = 6)
	sin.grid(row = 2, column = 6)
	tan.grid(row = 3, column = 6)
	cosec.grid(row = 4, column = 6)
	sec.grid(row = 5, column = 6)
	cot.grid(row = 6, column = 6)


#cos.grid(row = 1, column = 5)
#sin.grid(row = 2, column = 5)
#tan.grid(row = 3, column = 5)
	clear.grid(row = 5, column = 1, columnspan = 5)
#cosec.grid(row = 1, column = 6)
#sec.grid(row = 2, column = 6)
#cot.grid(row = 3, column = 6)
	equals.grid(row = 6, column = 1, columnspan = 5)
	#jago.mainloop()

def back():
	main()

# columnspan

def Physics():

	frame1 = LabelFrame(root, text = "motion", padx = 20, pady = 10)
	frame1.grid(row = 0, column = 0)

	button = Button(frame1, text = "start", command = motion)
	button.pack()

	frame2 = LabelFrame(root, text = "Projectile", padx = 20, pady = 10)
	frame2.grid(row = 0, column = 1)

	button2 = Button(frame2, text = "start", command = Projectile)
	button2.pack()

	frame3 = LabelFrame(root, text = "back", padx = 20, pady = 10)
	frame3.grid(row = 0, column = 2)

	button3 = Button(frame3, text = "<-", command = back)
	button3.pack()


def Mathematics():

	frame1 = LabelFrame(root, text = "arithmetic", padx = 20, pady = 10)
	frame1.grid(row = 0, column = 0)

	button = Button(frame1, text = "start", command = arithmetic)
	button.pack()

	frame2 = LabelFrame(root, text = "statistics", padx = 20, pady = 10)
	frame2.grid(row = 0, column = 1)

	button2 = Button(frame2, text = "start", command = statistics)
	button2.pack()

	frame3 = LabelFrame(root, text = "back", padx = 20, pady = 10)
	frame3.grid(row = 0, column = 2)

	button3 = Button(frame3, text = "<-", command = back)
	button3.pack()



def main():
	frame1 = LabelFrame(root, text = "Maths", padx = 20, pady = 10)
	frame1.grid(row = 0, column = 0)

	button = Button(frame1, text = "start", command = Mathematics)
	button.pack()

	frame2 = LabelFrame(root, text = "Physics", padx = 20, pady = 10)
	frame2.grid(row = 0, column = 1)

	button2 = Button(frame2, text = "start", command = Physics)
	button2.pack()

main()











root.mainloop()

