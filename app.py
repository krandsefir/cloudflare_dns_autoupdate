import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import shutil

def mostrar_ayuda(campo):
    leyenda = {
        "email": "El correo electrónico que usas para iniciar sesión en Cloudflare.",
        "key": "En tu perfil de Cloudflare, obtén tu 'Global API Key' en la pestaña 'API Tokens'.",
        "zone_id": "Inicia sesión en Cloudflare, selecciona tu dominio y encuentra el 'Zone ID' en la pestaña 'Overview'.",
        "record_name": "El nombre del registro DNS que deseas sincronizar (por ejemplo, 'example.com').",
        "sitename": "El título de tu sitio (por ejemplo, 'Mi Sitio Web')."
    }
    messagebox.showinfo(f"Ayuda para {campo}", leyenda[campo])

def crear_nuevo_archivo(base_file_path, email, key, zone_id, record_name, sitename):
    nuevo_nombre_archivo = f"api_dns_{record_name}.{sitename}.sh"
    shutil.copy(base_file_path, nuevo_nombre_archivo)

    # Leer solo las primeras 15 líneas del archivo
    with open(nuevo_nombre_archivo, 'r') as file:
        lines = file.readlines()

    # Modificar las líneas que contienen las variables
    new_lines = []
    for line in lines[:15]:
        modified_line = line.replace("{email}", email).replace("{key}", key).replace("{zone_id}", zone_id)
        modified_line = modified_line.replace("{record_name}", record_name).replace("{sitename}", sitename)
        new_lines.append(modified_line)
    
    # Unir las líneas modificadas con el resto del archivo
    new_content = ''.join(new_lines) + ''.join(lines[15:])

    # Escribir el contenido modificado de nuevo en el archivo
    with open(nuevo_nombre_archivo, 'w') as file:
        file.write(new_content)

    messagebox.showinfo("Archivo Creado", f"Archivo creado: {nuevo_nombre_archivo}")
    root.quit()  # Cierra la aplicación

def guardar_datos():
    email = email_entry.get()
    key = key_entry.get()
    zone_id = zone_id_entry.get()
    record_name = record_name_entry.get()
    sitename = sitename_entry.get()
    
    base_file_path = 'base.sh'  # Asegúrate de que el archivo base.sh esté en el mismo directorio
    crear_nuevo_archivo(base_file_path, email, key, zone_id, record_name, sitename)

# Configuración de la ventana principal
root = ttk.Window(themename="darkly")
root.title("Formulario de Configuración DNS")
root.geometry("400x400")

# Margen
margen = ttk.Frame(root, padding=20)
margen.pack(expand=True, fill='both')

# Labels y Entries
campos = ["email", "key", "zone_id", "record_name", "sitename"]
entries = {}

for campo in campos:
    frame = ttk.Frame(margen)
    frame.pack(fill='x', pady=5)
    
    label = ttk.Label(frame, text=campo.capitalize(), width=15, anchor='w')
    label.pack(side='left')
    
    entry = ttk.Entry(frame, style="TEntry")
    entry.pack(side='left', expand=True, fill='x', padx=10)
    
    entries[campo] = entry
    
    help_button = ttk.Button(frame, text="?", style="secondary.TButton", command=lambda c=campo: mostrar_ayuda(c))
    help_button.pack(side='left')

# Guardar Button
guardar_button = ttk.Button(margen, text="Guardar", style="success.TButton", command=guardar_datos)
guardar_button.pack(pady=20)

# Variables para las entradas
email_entry = entries["email"]
key_entry = entries["key"]
zone_id_entry = entries["zone_id"]
record_name_entry = entries["record_name"]
sitename_entry = entries["sitename"]

# Ejecutar la aplicación
root.mainloop()
