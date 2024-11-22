from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import RegistroUsuarioForm, InmuebleForm, EditarPerfilForm
from django.contrib.auth import login
from .models import Perfil, Inmueble, Region
from django.contrib import messages


# Create your views here.

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            Perfil.objects.create(
                usuario=user,
                nombres=form.cleaned_data['nombres'],
                apellidos=form.cleaned_data['apellidos'],
                rut=form.cleaned_data['rut'],
                direccion=form.cleaned_data['direccion'],
                telefono=form.cleaned_data['telefono'],
                correo_electronico=form.cleaned_data['correo_electronico'],
                tipo_usuario=form.cleaned_data['tipo_usuario']
            )
            login(request, user)
            messages.success(request, 'Cuenta creada exitosamente. ¡Bienvenido!')
            return redirect('home')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registro.html', {'form': form})

def home(request):
    tipo_inmueble = request.GET.get('tipo_inmueble', None)  
    ordenar_por_fecha = request.GET.get('ordenar_por_fecha', 'desc')  
    inmuebles = Inmueble.objects.all()
    
    if tipo_inmueble:
        inmuebles = inmuebles.filter(tipo_inmueble=tipo_inmueble)
    
    if ordenar_por_fecha == 'asc':
        inmuebles = inmuebles.order_by('fecha_creacion')  # Orden ascendente (más antiguos primero)
    else:
        inmuebles = inmuebles.order_by('-fecha_creacion')  # Orden descendente (más nuevos primero)
    
    regiones = Region.objects.all()
    return render(request, 'home.html', {
        'inmuebles': inmuebles,
        'regiones': regiones,
        'tipo_inmueble': tipo_inmueble,
        'ordenar_por_fecha': ordenar_por_fecha
    })

def crear_inmueble(request):
    if request.method == 'POST':
        form = InmuebleForm(request.POST, request.FILES)
        if form.is_valid():
            inmueble = form.save(commit=False)
            inmueble.arrendador = request.user.perfil  # Asignar al arrendador
            inmueble.save()
            return redirect('home')  # Redirige al 'home' después de crear el inmueble
    else:
        form = InmuebleForm()
    
    return render(request, 'crear_inmueble.html', {'form': form})

def editar_inmueble(request, id):
    inmueble = get_object_or_404(Inmueble, id=id)
    if request.method == 'POST':
        form = InmuebleForm(request.POST, instance=inmueble)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = InmuebleForm(instance=inmueble)
    return render(request, 'editar_inmueble.html', {'form': form, 'inmueble': inmueble})

def eliminar_inmueble(request, id):
    inmueble = get_object_or_404(Inmueble, id=id)
    if request.method == 'POST':
        inmueble.delete()
        return redirect('home')  
    return render(request, 'eliminar_inmueble.html', {'inmueble': inmueble})

def ver_mas_inmueble(request, id):
    inmueble = get_object_or_404(Inmueble, id=id)
    return render(request, 'ver_mas_inmueble.html', {'inmueble': inmueble})

@login_required
def editar_perfil(request):
    perfil = get_object_or_404(Perfil, usuario=request.user)
    
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('home')  # Cambia esto según tu URL
    else:
        form = EditarPerfilForm(instance=perfil)
    
    return render(request, 'editar_perfil.html', {'form': form})