#! /usr/bin/bash


sudo su

# verifier mysqlserveur est installer sinon l'installer sur le rasberry pi
service mysql restart || \
echo "Impossible de demarer mysql \n insatllation" &&  apt-get update && \
apt-get upgrade && apt install mariadb-server || \
echo "une erreur est survenue" && exit

# install les librairie python requis
python3 -m pip install -r requirements.txt || echo "impossble d 'installer les pacquet requis " && exit

#on rend executables les script python du repertoire
chmod +x *.py
#on change le plugin de connexion de l'utilisateur root
mysql -u root -p mysql < root_auth_plugin.sql
#on initialise la base de donnes
./init_db.py || echo "une erreur est survenue l'ors de l'initialisation de la besa de donnees"
mysql -u root -p stock < db.sql || echo "impossible de creer les tables de la base de donnees "