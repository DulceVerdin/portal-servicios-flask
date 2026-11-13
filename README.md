# Portal de Servicios

Proyecto universitario desarrollado con Python y Flask. Presenta información de
una empresa ficticia de tecnología e incluye calculadoras de compra, salario y
conversión de temperatura. La interfaz utiliza Bootstrap 5 mediante CDN.

## Requisitos

- Python 3.9 o posterior.
- Acceso a Internet para cargar Bootstrap desde CDN.
- Las imágenes `banner1.jpg`, `banner2.jpg` y `banner3.jpg` dentro de `static/img/`.

## Estructura del proyecto

```text
portal-servicios_Dulce/
├── .gitignore
├── app.py
├── requirements.txt
├── README.md
├── examen/
│   ├── explicacion.md
│   └── evidencias/
├── static/
│   ├── css/
│   │   └── estilos.css
│   └── img/
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── empresa.html
│   ├── servicios.html
│   ├── contacto.html
│   ├── compra.html
│   ├── salario.html
│   └── temperatura.html
└── .venv/
```

## Crear el entorno virtual en Windows

Abre PowerShell en la carpeta del proyecto y ejecuta:

```powershell
python -m venv .venv
```

Activa el entorno:

```powershell
.\.venv\Scripts\Activate.ps1
```

Si PowerShell impide ejecutar scripts, puedes activar el entorno desde Símbolo
del sistema con:

```bat
.venv\Scripts\activate.bat
```

## Instalar dependencias

Con el entorno virtual activado, instala Flask:

```powershell
python -m pip install -r requirements.txt
```

## Ejecutar la aplicación

Inicia el servidor de desarrollo:

```powershell
python app.py
```

Abre el portal en el navegador:

[http://127.0.0.1:5000](http://127.0.0.1:5000)

Para detener el servidor, vuelve a la terminal y presiona `Ctrl+C`.
