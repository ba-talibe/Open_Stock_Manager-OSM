#! /usr/bin/python3
import mysql.connector
import json

creds = dict()

with open("/usr/share/osm/creds.json", "r") as jsonfile:
    creds = json.load(jsonfile)

def database():
	global conn, cursor
	conn = mysql.connector.connect(host='localhost',
									user='oms', 
									password='passer123', 
									database='stock', 
									auth_plugin='mysql_native_password')
	cursor = conn.cursor()


def readAll():
	sql = "select * from articles"
	database()
	cursor.execute(sql)
	result = cursor.fetchall()
	for i in result:
		yield i


def consultation(code) -> list:
	database()
	sql = "select * from articles code=%s"
	val = (code,)
	cursor.execute(sql, val)
	result = cursor.fetchall()
	if len(result) == 0:
		message = [0, "Codebar non reconnu"]
	else:
		return result
		
	return message

def deposer(code : str, designation :str, descriptions : str, quantite : str):
	database()
	consul = consultation(code)
	if consul[0] == 0:
		sql = "insert into articles(code, designation, descriptions, quantite) values(%s, %s, %s, %s)"
		val = (code, designation, descriptions, quantite)
		cursor.execute(sql, val)
		conn.commit()
	else:
		nombre = int(consul[0][4]) + int(quantite)
		nombre = str(nombre)
		sql = "update articles set quantite=%s where code=%s"
		val = (nombre, code)
		cursor.execute(sql, val)
		conn.commit()

def retirer(code, quantite):
	database()
	consul = consultation(code)
	if consul[0] == 0:
		return -1
	else:
		quantEnStock = int(consul[0][4])
		if quantite > quantEnStock:
			return -1
		else:
			quantite = quantEnStock - int(quantite)
			if quantite == 0:
				suppression(code)
			else:
				sql = "update articles set quantite=%s where code=%s"
				val = (str(quantite), code)
				cursor.execute(sql, val)
				conn.commit()

def suppression(code):
	database()
	sql = "delete from articles where code=%s"
	cursor.execute(sql, (code,))
	conn.commit()