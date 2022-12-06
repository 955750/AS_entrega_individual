#### Importar librerías necesarias ####
from rethinkdb import r              
import subprocess


#### Programa principal ####
if __name__ == "__main__":

    # Declarar variables necesarias para la conexión con la base de datos 
    host = 'servidor-redb'
    port = 28015

    # Establecer conexión con la base de datos
    r.connect(host = host, port = port).repl()
    subprocess.run(["echo", "Se ha establecido la conexión con la base de datos"])
  
    # Restaurar backup de la base de datos
    subprocess.run(["rethinkdb-restore", "-c", f"{host}:{port}", "data/backup-bbdd.tar.gz"])

    # Crear una nueva tabla
    try:
        r.table_create('entrega_individual').run()
        subprocess.run(["echo", "Se ha creado la tabla 'entrega_individual' con éxito"])
    except:
        subprocess.run(["echo", "No se ha creado ninguna tabla. 'entrega_individual' ya existe"])

    # Insertar datos en la tabla recién creada
    try:
        r.table('entrega_individual').insert({
            'id': '1',
            'tarea_1': 'Explicar funcionalidad', 
            'tarea_2': 'Programar cliente', 
            'tarea_3': 'Subir imagen a DockerHub', 
            'tarea_4': 'Crear entorno compose'
        }).run()
        subprocess.run(["echo", "Se ha subido un dato a la tabla 'entrega_individual'"]) 
    except:
        subprocess.run(["echo", "No se ha subido ningún dato. El dato ya está en la tabla"])

    # Generar backup de la base de datos
    subprocess.run(["rethinkdb-dump", "-c", f"{host}:{port}", "-f", "backup-bbdd.tar.gz"])
    subprocess.run(["mv", "backup-bbdd.tar.gz", "data"])
    subprocess.run(["echo", "Se ha generado un backup de la base de datos"])
