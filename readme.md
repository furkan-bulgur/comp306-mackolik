Installing dependencies for mac look internet for windows
https://stackoverflow.com/questions/7225900/how-can-i-install-packages-using-pip-according-to-the-requirements-txt-file-from

$pip3 install -r requirements.txt

installing npm =>
$nodeenv -p
$npm install -g npm

check if installed by

$npm -v

Needed npm installmentes

 npm install react-router-dom
 npm install --save styled-components

before running create .env file in backend and write your database information inside as shown below. Don't put " for strings

DB_USER=<yourdatabaseusername>
PASSWORD=<yourpassword>
HOST=localhost
DATABASE=<databasename>
FLASK_APP=main.py
FLASK_ENV=development


How To RUN
on terminal in app folder run this command to run server

$npm run start-flask-server

then also in app folder run this command to run the frontend

$npm start

Possible errors:
If there is an error in npm start 

Go to package.json > scripts > start and replace
"react-scripts --openssl-legacy-provider start" with
"react-scripts start"