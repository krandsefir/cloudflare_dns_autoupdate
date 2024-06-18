import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def mostrar_ayuda(campo):
    leyenda = {
        "email": "El correo electrónico que usas para iniciar sesión en Cloudflare.",
        "token": "Ve a tu perfil de Cloudflare y genera un token de API en la pestaña 'API Tokens'.",
        "key": "En tu perfil de Cloudflare, obtén tu 'Global API Key' en la pestaña 'API Tokens'.",
        "zone_id": "Inicia sesión en Cloudflare, selecciona tu dominio y encuentra el 'Zone ID' en la pestaña 'Overview'.",
        "record_name": "El nombre del registro DNS que deseas sincronizar (por ejemplo, 'example.com').",
        "sitename": "El título de tu sitio (por ejemplo, 'Mi Sitio Web')."
    }
    messagebox.showinfo(f"Ayuda para {campo}", leyenda[campo])

def guardar_datos():
    email = email_entry.get()
    token = token_entry.get()
    key = key_entry.get()
    zone_id = zone_id_entry.get()
    record_name = record_name_entry.get()
    sitename = sitename_entry.get()
    
    # Aquí iría la lógica para crear el archivo con los datos obtenidos
    messagebox.showinfo("Datos Guardados", "Los datos han sido guardados correctamente.")

# Configuración de la ventana principal
root = ttk.Window(themename="darkly")
root.title("Formulario de Configuración DNS")
root.geometry("400x400")

# Margen
margen = ttk.Frame(root, padding=20)
margen.pack(expand=True, fill='both')

# Labels y Entries
campos = ["email", "token", "key", "zone_id", "record_name", "sitename"]
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
token_entry = entries["token"]
key_entry = entries["key"]
zone_id_entry = entries["zone_id"]
record_name_entry = entries["record_name"]
sitename_entry = entries["sitename"]

# Ejecutar la aplicación
root.mainloop()
