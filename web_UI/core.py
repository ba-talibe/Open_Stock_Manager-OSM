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

def ajouter(code, designation, descriptions):
	database()
	sql = "insert into articles(code, designation, descriptions) values(%s, %s, %s)"
	val = (code, designation, descriptions )
	cursor.execute(sql, val)
	conn.commit()


def consultation(code) -> list[tuple]:
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

def suppression(code):
	database()
	sql = "delete from articles where code=%s"
	cursor.execute(sql, (code,))
	conn.commit()
