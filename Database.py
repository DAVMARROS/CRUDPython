import pymysql

def getClave():
	db = pymysql.connect("localhost","root","","msc2019")
	cursor = db.cursor()
	sql = "select clave from empleados ORDER by clave DESC limit 1"
	cursor.execute(sql)
	result = cursor.fetchall()
	return result

def getAll():
	db = pymysql.connect("localhost","root","","msc2019")
	cursor = db.cursor()
	sql = "select * from empleados"
	cursor.execute(sql)
	result = cursor.fetchall()
	db.close()
	return result

def get(clave):
	db = pymysql.connect("localhost","root","","msc2019")
	cursor = db.cursor()
	sql = "select * from empleados where clave="+str(clave)
	cursor.execute(sql)
	result = cursor.fetchall()
	db.close()
	return result

def insert(clave, nombre, sueldo):
	db = pymysql.connect("localhost","root","","msc2019")
	cursor = db.cursor()
	sql = "insert into empleados(clave, nombre, sueldo) values({0},'{1}',{2})".format(int(clave),nombre,float(sueldo))
	try:
		cursor.execute(sql)
		db.commit()
		db.close()
		return 1
	except:
		db.rollback()

def edit(clave, nombre, sueldo):
	db = pymysql.connect("localhost","root","","msc2019")
	cursor = db.cursor()
	sql = "update empleados set nombre='{0}', sueldo={1} where clave={2}".format(nombre,float(sueldo),clave)
	try:
		cursor.execute(sql)
		db.commit()
		db.close()
		return 1
	except:
		db.rollback()

def delete(clave):
	db = pymysql.connect("localhost","root","","msc2019")
	cursor = db.cursor()
	sql = "delete from empleados where clave={0}".format(clave)
	try:
		cursor.execute(sql)
		db.commit()
		db.close()
		return 1
	except:
		db.rollback()
