# MiniBlogCoder

## Instalación:

Primero se deberá proceder a clonar el repositorio:

```sh
$ git clone https://github.com/rafaelricardodarosa/MiniBlogCoder.git
$ cd MiniBlogCoder
```

Crear un nuevo entorno virtual para instalar luego las dependecias, y finalmente
activarlo (ej: `virtualenv2`):

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```
#### Para ver la lista de dependencias revisar el archivo requirements.txt.

Instalación de las dependencias:

```sh
(env)$ pip install -r requirements.txt
```

Notar `(env)` en frente. Esto indica que la sesión en la termina estará operando
en el entorno virtual configurado como `virtualenv2`.

Una vez que `pip` haya terminado de instalar todas las dependencias:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
Navegar hacia la URL `http://127.0.0.1:8000/` o `localhost:8000`.

## Descripción del proyecto:

MINIBLOGCODER es un Blog dedicado a usuarios con ganas de compartir contenido 
dentro de temáticas como: Comidas, Animales y Naturaleza, Musica, Videojuegos,
Películas y series.
¡Sean todos bienvenidos a compartir sus vivencias digitales más nítidas!

## Participantes:

* Rafael Da Rosa
* Pablo Franco
* Rafael Agüero

## Roles de desarrolladores:

* Rafael Da Rosa: Aporte al template base para realizar el blog. Creador de las 
páginas principales de "Contacto", "Sobre" y trabajos en panel de administrador. 
Trabajo sobre html e incoporación de estilos css.

* Pablo Franco: Trabajo sobre el panel de admin, modelo Post, y autenticación del 
usuario (Página de "Iniciar Sesión" y "Registrarse").
Edición de estilos y funcionalidades comunes. 

* Rafael Agüero: Creación de página "Blog" y Página "Añadir Post". Trabajo en estilos
en páginas varias y funcionalidades comunes. 