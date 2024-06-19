
# Cloudflare DNS Auto Update

Este proyecto permite actualizar automáticamente el DNS en Cloudflare utilizando la API de Cloudflare.

## Funcionalidad

El script `app.py` proporciona una interfaz gráfica para solicitar las variables necesarias y generar un archivo nuevo basado en `base.sh`, que se encargará de actualizar el DNS en Cloudflare.

## Requisitos

- Python 3.x
- Tkinter (incluido en la mayoría de las instalaciones de Python)
- Requests library (`pip install requests`)

## Configuración

Antes de ejecutar `app.py`, necesitas preparar la siguiente información:

1. **Correo electrónico:** El correo electrónico asociado a tu cuenta de Cloudflare.
2. **Nombre del registro:** El nombre del registro DNS que deseas actualizar (por ejemplo, `www`).
3. **Nombre del sitio:** El nombre del dominio (por ejemplo, `ejemplo.com`).
4. **ID de la zona:** El identificador de la zona DNS en Cloudflare.

### Obtención del ID de la zona

1. Inicia sesión en tu cuenta de Cloudflare.
2. Selecciona el dominio que deseas actualizar.
3. En la parte superior, encontrarás el identificador de la zona (Zone ID).

### Creación de un token de API

1. En la sección de API Tokens de tu cuenta de Cloudflare, haz clic en "Create Token".
2. Configura los permisos del token:
   - **Permisos de Zona DNS:** Editar.
   - **Permisos de Zona:** Leer.
3. Especifica el dominio para el cual se aplicarán estos permisos.
4. Crea el token y cópialo.

### Configuración en la Interfaz Gráfica

1. Ejecuta `app.py` utilizando Python:

   ```bash
   python app.py
   ```

2. Ingresa la información solicitada en la interfaz gráfica:
   - Correo electrónico
   - Nombre del registro
   - Nombre del sitio
   - ID de la zona
   - Token de API

3. La interfaz gráfica generará un nuevo archivo basado en `base.sh` con la configuración ingresada.

## Uso del Script Generado

Ejecuta el script generado para actualizar el registro DNS con la dirección IP actual de tu dispositivo:

```bash
bash nuevo_script_generado.sh
```

## Automatización con Cron

Para ejecutar el script de forma recurrente, puedes utilizar `cron` en sistemas Unix/Linux. 

1. Abre el archivo crontab para editar:

   ```bash
   crontab -e
   ```

2. Añade una línea al final del archivo para ejecutar el script a intervalos regulares. Por ejemplo, para ejecutarlo cada hora, añade:

   ```bash
   0 * * * * /ruta/al/nuevo_script_generado.sh
   ```

3. Guarda y cierra el archivo crontab.

El script se ejecutará automáticamente según el intervalo definido, manteniendo tu DNS actualizado.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, realiza un fork del repositorio y envía un pull request con tus mejoras o correcciones.
