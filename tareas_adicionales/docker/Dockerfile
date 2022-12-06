#### Imagen base ####
FROM python:3.11-alpine

#### Directorio de trabajo ####
WORKDIR /code

#### Crear carpeta para guardar backups de la base de datos ####
RUN mkdir data

#### Copiar ficheros necesarios al contenedor ####
COPY main_app.py /code
COPY requirements.txt .

#### Instalar paquetes y dependencias ####
RUN pip install -r requirements.txt

#### Comando de arranque ####
CMD python3 main_app.py
