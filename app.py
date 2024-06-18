import shutil

def solicitar_variables():
    email = input("Introduce el email: ")
    token = input("Introduce el token: ")
    key = input("Introduce el key: ")
    zone_id = input("Introduce el zone_id: ")
    record_name = input("Introduce el record_name: ")
    sitename = input("Introduce el sitename: ")
    return email, token, key, zone_id, record_name, sitename

def crear_nuevo_archivo(base_file_path, email, token, key, zone_id, record_name, sitename):
    nuevo_nombre_archivo = f"api_dns_{record_name}.{sitename}.sh"
    shutil.copy(base_file_path, nuevo_nombre_archivo)

    with open(nuevo_nombre_archivo, 'r') as file:
        file_data = file.read()

    # Reemplazar los placeholders con las variables proporcionadas
    file_data = file_data.replace("{email}", email)
    file_data = file_data.replace("{token}", token)
    file_data = file_data.replace("{key}", key)
    file_data = file_data.replace("{zone_id}", zone_id)
    file_data = file_data.replace("{record_name}", record_name)
    file_data = file_data.replace("{sitename}", sitename)

    with open(nuevo_nombre_archivo, 'w') as file:
        file.write(file_data)

    print(f"Archivo creado: {nuevo_nombre_archivo}")

def main():
    base_file_path = 'base.sh'  # Ruta del archivo base
    email, token, key, zone_id, record_name, sitename = solicitar_variables()
    crear_nuevo_archivo(base_file_path, email, token, key, zone_id, record_name, sitename)

if __name__ == "__main__":
    main()
