
#! /usr/bin/python3
"""
script d'inialisation de la base de donnees
a remplir plutard
"""

import json
import getpass
import mysql.connector
import os

creds = dict()

user = input("enter l'utilisateur a creer : ")
while not user.isalpha():
    print("utilisateur invalide\n")
    user = input("enter l'utilisateur a creer : ")
creds.update({'user': user})


passwd = getpass.getpass("enter un mot de passe : ")
while len(passwd) <= 7:
    passwd = getpass.getpass("enter un mot de passe : ")
creds.update({'password': passwd})

with open("/usr/share/osm/creds.json", "w+") as jsonfile:
    jsonfile.seek(0)
    jsonfile.truncate()
    json.dump(creds, jsonfile)

if not os.system("sudo chown pi  /usr/share/osm/*") == 0:
    print("Une erreur est survenu lors de l'execution de ' sudo chown pi  /usr/share/osm/*'")
    print("veillez penser a changer le proprietaire de du repertoire /usr/share/osm")
passwd = getpass.getpass("enter un mot de passe administrateur de la de donnes (root): ")
rootconn = mysql.connector.connect(host='localhost',
									user='root', 
									password=passwd,
									auth_plugin='mysql_native_password')

cursor = rootconn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS stock")

userquery = f"create user if not exists {creds['user']}@'localhost' identified by '{creds['password']}'"
cursor.execute(userquery)

grantquery = f"grant all privileges on stock.* to \
    {creds['user']}@'localhost'"

cursor.execute(grantquery)
rootconn.close()
