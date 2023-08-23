# 1. Introducción

Este script Python nos permite extraer un listado de libros a partir de la información de episodios de un podcast.

# 2. Requisitos

Para ejecutar este script necesitamos las siguientes herramientas:

1. Python 3.8 o superior
2. pip
3. Ambiente virtual
4. Base de datos SQLite
5. Python dot-env
6. Selenium

# 3. Instalación

1. Clonar el repositorio

```bash
git clone https://github.com/Fhernd/extractor_titulos_libros.git
```

2. Crear un ambiente virtual

```bash
python -m venv venv
```

3. Activar el ambiente virtual

3.1 Linux/macOS:

```bash
source venv/bin/activate
```

3.2 Windows:

```bash
venv\Scripts\activate.bat
```

4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

5. Crear un archivo `.env` con la siguiente información:

```bash
EMAIL= # Correo electrónico de la cuenta de ChatGPT
PASSWORD= # Contraseña de la cuenta de ChatGPT
```

# 4. Ejecución

Para ejecutar el script, debemos ejecutar el siguiente comando:

```bash
python main.py
```

# 5. Resultados

La información de libros también quedará almacenada en la base de datos.

El script nos generará un archivo `libros.txt` con el siguiente formato:

# 6. Notas importantes

- Antes de ejecutar el script hay que tener en cuenta el nombre de la base de datos SQLite.

- La extracción de títulos de libros es semiautomática, es decir, el navegador mostrará un captcha que hay que resolver manualmente.
