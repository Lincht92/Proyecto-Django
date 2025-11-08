# Proyecto Django

Este proyecto fue desarrollado como parte del curso de Python + Django.
Estudiante: Jose Antonio Betancourt Moreira

##Descripción
Aplicación web desarrollada con el framework **Django**, que permite:
> Registrar usuarios, iniciar sesion, y crear publicaciones de eventos culturales, asi como editar o borrar dichos eventos.

##Tecnologías utilizadas
- Python 3.13
- Django 5.2.8
- HTML, CSS, Bootstrap  
- SQLite

##Indicaciones del proyecto

- Usted forma parte de un equipo de desarrollo encargado de crear un portal web para la gestión y publicación de eventos locales, utilizando el framework Django.

- El objetivo principal del proyecto es permitir que los usuarios puedan registrarse, iniciar sesión y crear publicaciones de eventos, mientras los visitantes pueden ver los eventos disponibles en una interfaz dinámica y ordenada.

- El resultado esperado es un sitio funcional y navegable con las siguientes secciones:
- Página de inicio que muestra la lista de eventos.
- Página de detalle de cada evento.
- Páginas para crear y editar eventos (solo para usuarios autenticados).
- Páginas de registro, login y logout.

- Puntos importantes:
1. Cree una aplicación llamada eventos_app
2. Diseñe un modelo Evento con los siguientes campos:
    a. titulo (CharField),
    b. descripcion (TextField),
    c. fecha (DateField),
    d. ubicacion (CharField),
    e. creado_por (ForeignKey al modelo User).
3. Use el ORM de Django para insertar, actualizar, consultar y eliminar registros desde la consola interactiva
4. Diseñe plantillas HTML para renderizar los datos de los eventos
5. Cree formularios HTML para añadir y editar eventos, manejando correctamente los métodos GET y POST.
6. Configure el sistema de usuarios de Django para permitir registro, inicio y cierre de sesión.

##Instalación y configuración
Sigua estos pasos para ejecutar el proyecto en su computadora:

1. Clonar el repositorio desde GitHub.
    (O descargar el ZIP y extraerlo)

2. Abrir la carpeta del proyecto en VS Code.

3. Crear un entorno virtual (venv):
    En la terminal de VS Code escriba: python -m venv venv

4. Activar el entorno virtual:
    En la terminal de VS Code escriba: venv\Scripts\activate
    En macOS o Linux: source venv/bin/activate

5. Instalar las dependencias del proyecto:
    pip install -r requirements.txt

6. Aplicar migraciones a la base de datos:
    python manage.py migrate

7. Ejecutar el servidor de desarrollo:
    python manage.py runserver

8. Abrir en el navegador: http://127.0.0.1:8000/

