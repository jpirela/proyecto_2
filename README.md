# ProyectoFlask_RafaelCastro
sudo apt install python3
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Base de datos
crear la base de datos (con postgresql por ejemplo)
crear con touch .env con FLASK_ENV y DATABASE_URL para ejecutarlo en localhost

## Ejecutar en localhost
python3 main.py
esto ejecutara una ventana de registro en el puerto 5000, se puede visualizar en el navegador
