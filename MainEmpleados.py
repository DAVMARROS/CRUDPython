from tkinter import *
from tkinter import messagebox
from tkinter import Menu
from Database import *
from Reporte import *

def main():
	global w, wver, weditar
	w = Toplevel()
	w.geometry('600x350')
	w.update()
	menu = Menu(w)
	it1 = Menu(menu)
	it1.add_command(label='Empleados')
	menu.add_cascade(label='Catalogos', menu=it1)
	 
	it2 = Menu(menu)
	it2.add_command(label='Generar', command=generarReporte) 
	menu.add_cascade(label='Reportes', menu=it2)

	item3 = Menu(menu)
	item3.add_command(label='Acerca de')
	item3.add_command(label='Salir', command=salir)
	menu.add_cascade(label='Acerca de', menu=item3)

	btnAgregar = Button(w, text="Agregar Empleado", command=mainAgregar)
	btnAgregar.grid(column=5, row=2, padx=(20, 10), pady=(10, 10))

	data = getAll()
	lbl1 = Label(w, text="Clave", font='Helvetica 10 bold')
	lbl1.grid(column=0, row=4, padx=(20, 10))
	lbl2 = Label(w, text="Nombre", font='Helvetica 10 bold')
	lbl2.grid(column=1, row=4, padx=(20, 10))
	lbl3 = Label(w, text="Sueldo", font='Helvetica 10 bold')
	lbl3.grid(column=2, row=4, padx=(20, 10))
	cont=5
	for row in data:
		item = row[0]
		lblclave = Label(w, text=row[0])
		lblclave.grid(column=0, row=cont, padx=(20, 10))
		lblnombre = Label(w, text=row[1])
		lblnombre.grid(column=1, row=cont, padx=(20, 10))
		lblsueldo = Label(w, text=row[2])
		lblsueldo.grid(column=2, row=cont, padx=(20, 10))
		btnVer = Button(w, text="Ver", command=lambda x=item: mainVer(x))
		btnVer.grid(column=3, row=cont, padx=(20, 10), pady=(10, 10))
		btnEditar = Button(w, text="Editar", command=lambda x=item: mainEditar(x))
		btnEditar.grid(column=4, row=cont, padx=(20, 10), pady=(10, 10))
		btnEliminar = Button(w, text="Eliminar", command=lambda x=item: mainEliminar(x))
		btnEliminar.grid(column=5, row=cont, padx=(20, 10), pady=(10, 10))
		cont+=1
	w.config(menu=menu)
	w.mainloop()

def salir():
	w.destroy()

def mainAgregar():
	wagregar = Toplevel()
	salir()
	wagregar.geometry('350x300')
	data = getClave()
	data = int(data[0][0])+1
	lblclave = Label(wagregar, text="Clave")
	lblclave.grid(column=0, row=0, padx=(40, 30), pady=(20, 20))
	txtclave = Label(wagregar,text=data)
	txtclave.grid(column=1, row=0, padx=(40, 30), pady=(20, 20))

	lblnombre = Label(wagregar, text="Nombre")
	lblnombre.grid(column=0, row=1, padx=(40, 30), pady=(20, 20))
	txtnombre = Entry(wagregar,width=20)
	txtnombre.grid(column=1, row=1, padx=(40, 30), pady=(20, 20))

	lblsueldo = Label(wagregar, text="Sueldo")
	lblsueldo.grid(column=0, row=2, padx=(40, 30), pady=(20, 20))
	txtsueldo = Entry(wagregar,width=20)
	txtsueldo.grid(column=1, row=2, padx=(40, 30), pady=(20, 20))

	def agregarEmpleado():
		res = insert(txtclave.cget("text"), txtnombre.get(), txtsueldo.get())
		if(res==1):
			wagregar.destroy()
			main()
		else:
			messagebox.showinfo('Error', 'Intente nuevamente')
	btnCrear = Button(wagregar, text="Guardar", command=agregarEmpleado)
	btnCrear.grid(column=0, row=4, padx=(20, 10), pady=(10, 10))

	def salirAgregar():
		wagregar.destroy()
		main()
	btnImprimir = Button(wagregar, text="Cancelar", command=salirAgregar)
	btnImprimir.grid(column=1, row=4, padx=(20, 20), pady=(10, 10))

def mainVer(clave):
	wver = Toplevel()
	salir()
	wver.geometry('350x300')
	data = get(clave)
	lblclave = Label(wver, text="Clave")
	lblclave.grid(column=0, row=0, padx=(40, 30), pady=(20, 20))
	txtclave = Label(wver,text=data[0][0])
	txtclave.grid(column=1, row=0, padx=(40, 30), pady=(20, 20))

	lblnombre = Label(wver, text="Nombre")
	lblnombre.grid(column=0, row=1, padx=(40, 30), pady=(20, 20))
	txtnombre = Label(wver,text=data[0][1])
	txtnombre.grid(column=1, row=1, padx=(40, 30), pady=(20, 20))

	lblsueldo = Label(wver, text="Sueldo")
	lblsueldo.grid(column=0, row=2, padx=(40, 30), pady=(20, 20))
	txtsueldo = Label(wver,text=data[0][2])
	txtsueldo.grid(column=1, row=2, padx=(40, 30), pady=(20, 20))

	def editar(clave):
		wver.destroy()
		mainEditar(clave)
	btnCrear = Button(wver, text="Editar", command=lambda x=clave: editar(x))
	btnCrear.grid(column=0, row=3, padx=(20, 10), pady=(10, 10))

	def salirVer():
		wver.destroy()
		main()
	btnImprimir = Button(wver, text="Cancelar", command=salirVer)
	btnImprimir.grid(column=1, row=3, padx=(20, 20), pady=(10, 10))

def mainEditar(clave):
	weditar = Toplevel()
	salir()
	weditar.geometry('350x300')
	data = get(clave)
	lblclave = Label(weditar, text="Clave")
	lblclave.grid(column=0, row=0, padx=(40, 30), pady=(20, 20))
	txtclave = Label(weditar,text=data[0][0])
	txtclave.grid(column=1, row=0, padx=(40, 30), pady=(20, 20))

	lblnombre = Label(weditar, text="Nombre")
	lblnombre.grid(column=0, row=1, padx=(40, 30), pady=(20, 20))
	txtnombre = Entry(weditar,width=20)
	txtnombre.grid(column=1, row=1, padx=(40, 30), pady=(20, 20))
	txtnombre.insert(0,data[0][1])

	lblsueldo = Label(weditar, text="Sueldo")
	lblsueldo.grid(column=0, row=2, padx=(40, 30), pady=(20, 20))
	txtsueldo = Entry(weditar,width=20)
	txtsueldo.grid(column=1, row=2, padx=(40, 30), pady=(20, 20))
	txtsueldo.insert(0,data[0][2])

	def editarEmpleado():
		res = edit(txtclave.get(), txtnombre.get(), txtsueldo.get())
		if(res==1):
			weditar.destroy()
			mainVer(clave)
		else:
			messagebox.showinfo('Error', 'Intente nuevamente')
	btnCrear = Button(weditar, text="Editar", command=editarEmpleado)
	btnCrear.grid(column=0, row=4, padx=(20, 10), pady=(10, 10))

	def salirEditar():
		weditar.destroy()
		mainVer(clave)
	btnImprimir = Button(weditar, text="Cancelar", command=salirEditar)
	btnImprimir.grid(column=1, row=4, padx=(20, 20), pady=(10, 10))

def mainEliminar(clave):
	weliminar = Toplevel()
	salir()
	weliminar.geometry('350x200')
	data = get(clave)
	lbl = Label(weliminar, text="¿Desea eliminar el empleado "+data[0][1]+"?")
	lbl.grid(column=0, row=1, padx=(20, 10), pady=(20, 20))
	def eliminarEmpleado():
		res = delete(clave)
		if(res==1):
			weliminar.destroy()
			main()
		else:
			messagebox.showinfo('Error', 'Intente nuevamente')
	btnCrear = Button(weliminar, text="Eliminar", command=eliminarEmpleado)
	btnCrear.grid(column=0, row=2, padx=(10, 10), pady=(10, 10))

	def salirEliminar():
		weliminar.destroy()
		main()
	btnImprimir = Button(weliminar, text="Cancelar", command=salirEliminar)
	btnImprimir.grid(column=1, row=2, padx=(10, 10), pady=(10, 10))