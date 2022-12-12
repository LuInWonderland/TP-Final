from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from AppUsuarios import forms, models

# Create your views here.
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasena = form.cleaned_data.get('password')
            user=authenticate(username = usuario, password = contrasena)
            if user is not None:
                login(request, user)
                return render(request, "inicio.html", {"mensaje":f"Bienvenido {usuario}", "avatar_url": get_avatar_url(request)})
            else:
                return render(request, "inicio.html", {"mensaje":f"No se pudo iniciar sesión, datos incorrectos"})
        else:
            return render(request, "inicio.html", {"mensaje":form.errors})
    form = AuthenticationForm()
    return render(request, "login.html", {'form':form})

def register(request):
    mensaje = ''
    if request.method == "POST":
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            form.save()
            return render(request, "inicio.html", {"mensaje":f"Usuario creado satisfactoriamente"})
        mensaje = "Los datos ingresados no cumplen con los requisitos."
    form = forms.UserRegisterForm()
    return render(request, "registro.html", {'form':form, 'mensaje':mensaje})

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = forms.UserEditForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario.email = info['email']
            usuario.first_name = info['first_name']
            usuario.last_name = info['last_name']
            usuario.password1 = info['password1']
            usuario.password2 = info['password2']
            usuario.save()
            return render(request, "inicio.html", {'avatar_url': get_avatar_url(request)})
        else:
            
            return render(request, "inicio.html", {"mensaje":f"Error al editar usuario: "+str(form.errors)})
    else:
        form = forms.UserEditForm(initial ={ 'username': usuario.username, 'email': usuario.email, 'first_name': usuario.first_name, 'last_name': usuario.last_name})
        return render(request, "editarPerfil.html", {'form':form, 'usuario':usuario, 'avatar_url': get_avatar_url(request)})

@login_required
def get_avatar_url(request):
    try:
        return models.Avatar.objects.filter(user=request.user.id)[0].imagen.url
    except:
        return "/media/avatares/no-profile-pic.webp"

@login_required
def inicio(request):
    return render(request, "inicio.html", {'avatar_url': get_avatar_url(request)})

@login_required
def sobreMi(request):
    return render(request, "sobreMi.html", {'avatar_url': get_avatar_url(request)})

