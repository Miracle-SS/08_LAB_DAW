# Laboratorio 08 - Destinos Turísticos con Django

## Descripción

Aplicación web desarrollada con Django para la gestión de destinos turísticos. El sistema permite registrar, visualizar, modificar y eliminar destinos turísticos mediante una interfaz web conectada a una base de datos SQLite.

## Objetivos

- Implementar una aplicación web utilizando Django.
- Utilizar modelos para almacenar información en una base de datos.
- Mostrar datos dinámicamente mediante plantillas Django.
- Aplicar los tags `for` e `if`.
- Implementar operaciones CRUD (Crear, Leer, Actualizar y Eliminar).

## Tecnologías Utilizadas

- Python 3
- Django
- SQLite
- HTML5
- CSS3
- Git
- GitHub

## Modelo Implementado

La tabla **DestinosTuristicos** contiene los siguientes campos:

| Campo | Tipo |
|---------|---------|
| nombreCiudad | CharField |
| descripcionCiudad | TextField |
| imagenCiudad | ImageField |
| precioTour | IntegerField |
| ofertaTour | BooleanField |

## Funcionalidades

- Listar destinos turísticos.
- Agregar nuevos destinos.
- Modificar destinos existentes.
- Eliminar destinos.
- Mostrar ofertas especiales mediante etiquetas `if`.
- Mostrar registros dinámicamente mediante etiquetas `for`.
- Gestión de imágenes para cada destino.

## Estructura del Proyecto

```text
mi_proyecto/
│
├── manage.py
├── media/
├── mi_proyecto/
│
└── travello/
    ├── migrations/
    ├── static/
    │   └── css/
    │       └── estilo.css
    │
    ├── templates/
    │   └── travello/
    │       ├── base.html
    │       ├── destinos.html
    │       ├── crear_destino.html
    │       ├── modificar_destino.html
    │       └── confirmar_eliminar.html
    │
    ├── forms.py
    ├── models.py
    ├── urls.py
    └── views.py
```

## Instalación y Ejecución

### 1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

### 2. Ingresar al proyecto

```bash
cd mi_proyecto
```

### 3. Instalar dependencias

```bash
pip install django pillow
```

### 4. Aplicar migraciones

```bash
python manage.py migrate
```

### 5. Ejecutar el servidor

```bash
python manage.py runserver
```

### 6. Abrir en el navegador

```text
http://127.0.0.1:8000/
```

## Video Explicativo

Enlace al video:
https://youtu.be/uvZn0J7W_vI

## Autor

Choquecota Pandia, Mario Miguel

Curso: Desarrollo de Aplicaciones Web

Docente: Mgter. Carlo Corrales Delgado

Universidad: Universidad Nacional de San Agustín de Arequipa
