echo "this shell script is going to setup a running instance of Fake API application."

echo "switching the OS language"
locale-gen
export LC_ALL="pt_br.UTF-8"
sudo locale-gen pt_br.UTF-8

echo "updating the package manager"
sudo apt-get update -q

echo "installing dependencies available via apt-get"
sudo apt-get install -y -q build-essential git python-dev python-setuptools nginx supervisor

echo "installing pip"
sudo easy_install pip

echo "installing python dependencies available via pip"
sudo pip install virtualenv

echo "creating a new python virtualenv"
virtualenv /var/.virtualenvs/api_fake
source /var/.virtualenvs/api_fake/bin/activate

echo "installing dependencies defined in requirements.txt"
pip install -r requirements.txt

echo "creating logs' folder"
mkdir deploy/logs

echo "changing owner of deploy's folder"
sudo chown -R www-data:www-data deploy

echo "copying nginx's configuration file"
sudo cp deploy/api_fake.nginx /etc/nginx/sites-enabled/

echo "restarting nginx"
sudo service nginx restart

echo "copying supervisor's configuration file"
sudo cp deploy/api_fake.conf.supervisor /etc/supervisor/conf.d/

echo "restarting supervisor"
sudo service supervisor restart