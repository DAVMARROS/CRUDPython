from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Spacer, Paragraph, Table, TableStyle
from reportlab.lib.pagesizes import letter, inch
from Database import *
from tkinter import messagebox

def generarReporte():
	stylesheet = getSampleStyleSheet()
	doc = SimpleDocTemplate("Reporte_Empleados.pdf", pagesize=letter)

	colwidths = [2*inch, 2*inch, 2*inch]

	elements = []
	elements.append(Paragraph('Reporte de Empleados', stylesheet['Title']))
	elements.append(Spacer(1,12))

	data=getAll()
	data = [list(i) for i in data]
	data.insert(0,["Clave","Nombre","Sueldo"])
	t = Table(data, colwidths)
	t.setStyle(TableStyle([('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
	                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
	                       ]))
	 
	elements.append(t)
	# write the document to disk
	doc.build(elements)
	messagebox.showinfo('Reporte', 'Reporte generado correctamente')