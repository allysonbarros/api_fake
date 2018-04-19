echo "this shell script is going to setup a running instance of Fake API application."

echo "switching the OS language"
locale-gen
export LC_ALL="pt_br.UTF-8"
sudo locale-gen pt_br.UTF-8

echo "updating the package manager"
apt-get update -q

echo "installing dependencies available via apt-get"
apt-get install -y -q build-essential git python-dev python-setuptools nginx supervisor

echo "installing pip"
easy_install pip

echo "installing python dependencies available via pip"
pip install virtualenv

echo "creating a new python virtualenv"
virtualenv /var/.virtualenvs/api_fake
source /var/.virtualenvs/api_fake/bin/activate

echo "installing dependencies defined in requirements.txt"
pip install -r requirements.txt
