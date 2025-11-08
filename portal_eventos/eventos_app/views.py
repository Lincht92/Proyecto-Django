# -----------------------------------------------
# vistas.py — Módulo principal de vistas del sistema de eventos
# -----------------------------------------------
# En este archivo se definen las vistas que controlan el flujo de datos
# entre los modelos, los formularios y las plantillas HTML.
# Cada función representa una vista que responde a una URL específica.
# -----------------------------------------------

from django.shortcuts import render, get_object_or_404, redirect
from .models import Evento
from .forms import EventoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


# -------------------------------------------------------------
# Vista principal (Index)
# -------------------------------------------------------------
def index(request):
    """
    Muestra la página principal con el listado de eventos disponibles.
    Los eventos se ordenan por fecha de forma ascendente.

    Parámetros:
        request (HttpRequest): Solicitud del usuario.

    Retorna:
        HttpResponse: Página renderizada con la lista de eventos.
    """
    eventos = Evento.objects.order_by('fecha')
    return render(request, 'eventos_app/index.html', {'eventos': eventos})


# -------------------------------------------------------------
# Vista de detalle de un evento
# -------------------------------------------------------------
def detalle_evento(request, pk):
    """
    Muestra la información completa de un evento específico.

    Parámetros:
        request (HttpRequest): Solicitud del usuario.
        pk (int): Identificador primario del evento.

    Retorna:
        HttpResponse: Página renderizada con los detalles del evento.
    """
    evento = get_object_or_404(Evento, pk=pk)
    return render(request, 'eventos_app/detalle.html', {'evento': evento})


# -------------------------------------------------------------
# Crear nuevo evento (requiere inicio de sesión)
# -------------------------------------------------------------
@login_required
def crear_evento(request):
    """
    Permite al usuario autenticado crear un nuevo evento.

    Si la solicitud es POST, se procesan los datos del formulario.
    Si la información es válida, se guarda el evento asociado al usuario
    que lo creó y se muestra un mensaje de éxito.

    Parámetros:
        request (HttpRequest): Solicitud del usuario.

    Retorna:
        HttpResponse: Página del formulario o redirección al detalle del evento creado.
    """
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.creado_por = request.user
            evento.save()
            messages.success(request, 'Evento creado correctamente.')
            return redirect('eventos_app:detalle', pk=evento.pk)
    else:
        form = EventoForm()
    return render(request, 'eventos_app/evento_form.html', {'form': form})


# -------------------------------------------------------------
# Editar un evento existente (requiere inicio de sesión)
# -------------------------------------------------------------
@login_required
def editar_evento(request, pk):
    """
    Permite editar la información de un evento existente.

    Solo el usuario que creó el evento o un usuario con rol de personal (staff)
    puede realizar modificaciones. Si no cumple con los permisos,
    se muestra un mensaje de error.

    Parámetros:
        request (HttpRequest): Solicitud del usuario.
        pk (int): Identificador primario del evento a editar.

    Retorna:
        HttpResponse: Página del formulario o redirección al detalle actualizado.
    """
    evento = get_object_or_404(Evento, pk=pk)

    if evento.creado_por != request.user and not request.user.is_staff:
        messages.error(request, 'Usted no tiene permiso para editar este evento.')
        return redirect('eventos_app:detalle', pk=pk)

    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Evento actualizado correctamente.')
            return redirect('eventos_app:detalle', pk=pk)
    else:
        form = EventoForm(instance=evento)
    return render(request, 'eventos_app/evento_form.html', {'form': form})


# -------------------------------------------------------------
# Eliminar un evento (requiere inicio de sesión)
# -------------------------------------------------------------
@login_required
def borrar_evento(request, pk):
    """
    Permite eliminar un evento específico.

    Solo el creador del evento o un usuario con rol de personal (staff)
    puede realizar esta acción. Si la solicitud es POST, el evento se elimina.

    Parámetros:
        request (HttpRequest): Solicitud del usuario.
        pk (int): Identificador primario del evento.

    Retorna:
        HttpResponse: Redirección al listado principal o confirmación de eliminación.
    """
    evento = get_object_or_404(Evento, pk=pk)

    if evento.creado_por != request.user and not request.user.is_staff:
        messages.error(request, 'Usted no tiene permiso para borrar este evento.')
        return redirect('eventos_app:detalle', pk=pk)

    if request.method == 'POST':
        evento.delete()
        messages.success(request, 'Evento eliminado exitosamente.')
        return redirect('eventos_app:index')

    return render(request, 'eventos_app/confirmar_borrar.html', {'evento': evento})


# -------------------------------------------------------------
# Registro de usuarios
# -------------------------------------------------------------
def registro(request):
    """
    Permite registrar un nuevo usuario en el sistema.

    Si el formulario es válido, se crea la cuenta, se inicia sesión
    automáticamente y se muestra un mensaje de confirmación.

    Parámetros:
        request (HttpRequest): Solicitud del usuario.

    Retorna:
        HttpResponse: Página del formulario o redirección al inicio.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registro exitoso. Ha iniciado sesión correctamente.')
            return redirect('eventos_app:index')
    else:
        form = UserCreationForm()
    return render(request, 'eventos_app/registro.html', {'form': form})
