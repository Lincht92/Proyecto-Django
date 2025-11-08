from django.shortcuts import render, get_object_or_404, redirect
from .models import Evento
from .forms import EventoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def index(request):
    eventos = Evento.objects.order_by('fecha')
    return render(request, 'eventos_app/index.html', {'eventos': eventos})

def detalle_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    return render(request, 'eventos_app/detalle.html', {'evento': evento})

@login_required
def crear_evento(request):
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

@login_required
def editar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if evento.creado_por != request.user and not request.user.is_staff:
        messages.error(request, 'No tienes permiso para editar este evento.')
        return redirect('eventos_app:detalle', pk=pk)

    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Evento actualizado.')
            return redirect('eventos_app:detalle', pk=pk)
    else:
        form = EventoForm(instance=evento)
    return render(request, 'eventos_app/evento_form.html', {'form': form})

@login_required
def borrar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if evento.creado_por != request.user and not request.user.is_staff:
        messages.error(request, 'No tienes permiso para borrar este evento.')
        return redirect('eventos_app:detalle', pk=pk)
    if request.method == 'POST':
        evento.delete()
        messages.success(request, 'Evento eliminado.')
        return redirect('eventos_app:index')
    return render(request, 'eventos_app/confirmar_borrar.html', {'evento': evento})

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registro exitoso. Ya estás logueado.')
            return redirect('eventos_app:index')
    else:
        form = UserCreationForm()
    return render(request, 'eventos_app/registro.html', {'form': form})
