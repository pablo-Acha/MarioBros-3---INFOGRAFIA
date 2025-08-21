## tiene que entrar a la carpeta del repositorio 
cd MarioBros-3---INFOGRAFIA

## descargar librerias uv SOLO UNA VEZ
pip install uv
uv venv

## activar el entorno virtual cada vez que entres a la carpeta
.\.venv\Scripts\activate

## descargar las librerias SOLO UNA VEZ despues de activar el entorno virtual 
uv add arcade
uv add pymunk


## iniciar el proyecto 
python .\main.py

