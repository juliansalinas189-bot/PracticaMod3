import psycopg2
# 1. Conexión a la base de datos
conexion = psycopg2.connect(
    host="localhost",
    port="5432",
    database="credenciales",
    user="Admin",
    password="p4ssw0rdDB"
)

cursor = conexion.cursor()

cursor.execute("SELECT * FROM credenciales;")
registros = cursor.fetchall()

for fila in registros:
    print(fila)

cursor.close()
conexion.close()