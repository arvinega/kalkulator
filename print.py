import numpy

print("coba satu ini ya")
satu = int
dua = int
hurufa = str
satu = 1
dua = 2
tiga = satu + dua 
print(satu + dua + tiga)
if dua > satu :
	print ("dua lebih besar daripada satu")

	import numpy

	speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

	x = numpy.median(speed)

print(x)


import gspread

gc = gspread.service_account()

sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1y5V_5oL7kzq8Z1_ooqt4A9qeaFSCSYYhHMUinkKCIsk/edit#gid=0')

sh.sheet1.update('B1', 'Bingo!')
print(sh.sheet1.get("A1"))

from openpyxl import Workbook

print("masukan nama")
ulang = 1
#nilai1 = int
#ilai2 = int
		#print(ulang)
workbook = Workbook()
sheet = workbook.active
ws1 = workbook.create_sheet("Mysheet", 3)


from tkinter import *
nilai1 = int(0)
  
def masukannilai110():
	global nilai1
	nilai1 = nilai1 + 10
	print (nilai1)
	sheet["B1"] = nilai1
	workbook.save(filename="hello_world.xlsx")
	#sheet["C1"] = nilai2

root = Tk()
#b = Label(root, text = nama)
a = Label(root, text ="Hello World")


tomboltambah = Button(root, text = "tambah nilai 1", command = masukannilai110)
#print (nilai1)

#sheet["A1"] = nama
#sheet["B1"] = nilai1
#sheet["C1"] = nilai2
#while True :
		#nilai2 = nilai1 + 5

#print (nilai2)
ws1["A1"] = ("test")

workbook.save(filename="hello_world.xlsx")

#c = Label(root, text = nilai1 + nilai2)
a.pack()
#b.pack()
#c.pack()
tomboltambah.pack() 
root.mainloop()

