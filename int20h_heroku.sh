#!/bin/bash

#root installing
echo "[ ]Installing required packages, please input your password to proceed"
sudo apt update && sudo apt -y upgrade
sudo apt install python3 python3.7 git python-pip python3-pip libpq-dev snap postgres -y
sudo snap install heroku --classic
#root done

#python pip installing
echo "[ ]Changing your python alias to pyhton3"
echo "[ ] (look in tail of .bashrc)"
alias python=python3
echo "[+] OK"
echo "[ ] Installing required pyhton3 modules"
pip3 install django gunicorn django-heroku psycopg2-binary dj-database-url requests
#python done

#postgresql configure
#create user for user
echo "[ ]Configuring postgresql.."
sudo -u postgres psql -c "CREATE USER $(whoami) WITH SUPERUSER;" 
sudo -u postgres psql -c "ALTER USER $(whoami) WITH CREATEDB"
#sudo -u postgres createdb $(whoami)
export DATABASE_URL=postgres://$(whoami)
echo "[+] OK"
#postgresql done

#git config
echo "[ ] Configurating your git.."
echo "[*] Do you wish to set up git ID? [y/N] "
read response
case "$response" in
    [yY][eE][sS]|[yY])
		echo "[>] Please tell your full name: (Name Surname)"
		read Name Surname
		echo "[+] OK"
		echo "[>] Now please specify your emai address: (username@example.com)"
		read Email
		echo "[+] OK"
		git config --global user.name "$Name $Surname"
		git config --global user.email "$Email"
        ;;
    *)
        ;;
esac
#git end


#heroku conf
echo "[ ] Setting up your heroku.."
heroku login
echo "[ ] Cloning git repo.."
read -r -p "[*] Did you put your ssh key on repo? [y/N] " response
case "$response" in
    [yY][eE][sS]|[yY])
		cd ~
  		git clone git@github.com:rmrf-int20h/face_recognition.git
        ;;
    *)
        cd ~ 
        git clone https://github.com/rmrf-int20h/face_recognition.git
        ;;
esac
cd ~/face_recognition
#additional install of packets
echo "[ ] Verifying python3 modules"
pip3 install -r requirements.txt
echo "[+] OK"
echo "[*] You may need to drop old mylocaldb, will you? [y/N]: "
read response
case "$response" in
    [yY][eE][sS]|[yY]) 
		sudo -u postgres psql -c "DROP DATABASE mylocaldb;"
        ;;
    *)
        ;;
esac
#PGUSER=wxowaxhcpecbzi PGPASSWORD=9bb1e5fa868b59b15139f428e53093270bcd8e24badbbe8769993409a38aa156 
heroku pg:pull  postgresql-parallel-33995 mylocaldb --app int20h-rmrf-test
#configuring for local use
echo "[ ] Configuring python and heroku to run locally"
python3 manage.py collectstatic
heroku local &
echo "[+] OK"
echo "[+] All must work now if not please write to t.me/verbalius"
echo "[---------------------------------------------------------]"
echo "[+] Opening browser.."
firefox http://localhost:5000/
