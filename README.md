# ProyectoFlask_RafaelCastro
sudo apt install python3
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Base de datos
crear la base de datos (con postgresql por ejemplo)
crear con touch .env con FLASK_ENV y DATABASE_URL para ejecutarlo en localhost
Se debera crear una tabla llamada 'Administradores' en que contenga los campos 
usuario y contrasena en donde se insertaran un admin con su contrasena para realizar el CRUD 
posteriormente

## Ejecutar en localhost
python3 main.py
esto ejecutara una ventana de registro en el puerto 5000, se puede visualizar en el navegador

## Administrar
En el directorio Administar_Usuarios se encuentra el codigo que ejecuta la ventana de administrador
python3 app.py
Se debe ingresar el usuario y contrasena insertados anteriormente al crear la base de datos

