#! /usr/bin/bash

# verifier mysqlserveur est installer sinon l'installer sur le rasberry pi
sudo service mysql restart || \
echo "Impossible de demarer mysql \n insatllation" &&  sudo apt-get update && \
sudo apt-get upgrade && sudo apt install mariadb-server || \
echo "une erreur est survenue" && exit

# install les librairie python requis
python3 -m pip install -r requirements.txt || echo "impossble d 'installer les modules requis " && exit

#on rend executables les script python du repertoire
sudo chmod +x /web_UI/*.py
sudo chmod +x /desktop_ui/*.py

#on change le plugin de connexion de l'utilisateur root
sudo mysql -u root -p mysql < ./web_UI/root_auth_plugin.sql

sudo mkdir /usr/share/osm  || echo  "le repertoire existe deja" 
sudo mkdir /var/lib/cgi-bin/osm || echo  "le repertoire existe deja" 
sudo cp ./web_UI/core.py /usr/share/osm
#on initialise la base de donnes
sudo cp ./web_UI/index.py /usr/lib/cgi-bin/osm
sudo cp ./desktop_ui/*.py /usr/share/osm

touch run-osm
chmod a+x run-osm
echo "#! /usr/bin/bash" >> run-osm 
echo "python3 /usr/share/osm/main.py" >> run-osm

python3 init_db.py || echo "une erreur est survenue l'ors de l'initialisation de la besa de donnees"
sudo mysql -u root -p stock < ./web_UI/db.sql || echo "impossible de creer les tables de la base de donnees " 

echo "[+] Done ..."