"""
Nombre: MainCRUD.py
Objetivo: interfaz del crud
Autor: 
Fecha: 14/11/2019
"""

from tkinter import *
 
from tkinter import Menu
from MainEmpleados import *
from Reporte import *
 
window = Tk()
window.geometry('350x250')
window.title("Registro de Empleados")
 
menu = Menu(window)

item1 = Menu(menu)
item1.add_command(label='Empleados', command=main)
menu.add_cascade(label='Catalogos', menu=item1)
 
item2 = Menu(menu)
item2.add_command(label='Generar', command=generarReporte) 
menu.add_cascade(label='Reportes', menu=item2)

def salir():
	window.destroy()
item3 = Menu(menu)
item3.add_command(label='Acerca de')
item3.add_command(label='Salir', command=salir)
menu.add_cascade(label='Acerca de', menu=item3)

window.config(menu=menu)
window.mainloop()
