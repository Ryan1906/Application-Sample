from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse
from Pedidos.models import Articulos, Clientes, Posts, hilo
from django.core.mail import send_mail
from django.conf import settings
from Pedidos.form import  ClienteForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone


# Create your views here.


def buscar_productos(request):
    return render(request, "ProductsSearch.html")

def buscar(request):

    if request.GET["prd"]:
        #mensaje="Articulo buscado: %r" %request.GET["prd"]
        producto=request.GET["prd"]
        if len(producto)>20:
            mensaje="Texto de busqueda demasiado largo"
        else:
            articulos=Articulos.objects.filter(nombre__icontains=producto)
            return render(request, "Results.html", {"articulos":articulos, "query":producto})
    else:
        mensaje="No has introducido nada"
    return HttpResponse(mensaje)

def contacto(request):

    if request.method=="POST":
        subject=request.POST["asunto"]
        message=request.POST["mensaje"]+" "+request.POST["email"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=['rjrshuertas@gmail.com']

        send_mail(subject, message, email_from, recipient_list)

        return render(request, "gracias.html")

    return render(request, "contact.html")



def home(request):
    posts = Posts.objects.all()
    context = {'posts': posts}
    return render(request, 'home.html', context)

def register(request):
    if request.method == 'POST':
        # Creamos un formulario basado en los datos enviados por el usuario.
        form = ClienteForm(request.POST)
        if form.is_valid():
            # Si el formulario es válido, creamos una instancia del modelo Cliente y guardamos los datos.
            user = form.save(commit=False)
            user.email = form.cleaned_data.get('email')
            user.save()
            return redirect(home)
    else:
        form = ClienteForm()

    return render(request, 'registration.html', {'form': form})

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        email = request.POST.get('correo')
        password = request.POST.get('contrasenia')

        print(email, password)
        # Buscamos un cliente con el correo y contraseña ingresados
        try:
            cliente = Clientes.objects.get(email=email, contraseña=password)
        except Clientes.DoesNotExist:
            cliente = None

        if cliente is not None:
            # Guardamos el id del cliente en la sesión
            request.session['cliente_id'] = cliente.id
            return redirect(home)
        else:
            mensaje_error = 'Correo o contraseña incorrectos.'
            return render(request, 'index.html', {'form': form, 'mensaje_error': mensaje_error})
 
    return render(request, 'index.html', {'form': form})

def foro(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        mensaje = request.POST['mensaje']
        autor_id = request.session['cliente_id']
        autor = Clientes.objects.get(id=autor_id).nombre
        

        hilo1 = hilo.objects.create(
            titulo=titulo,
            contenido=mensaje,
            autor=autor,
            fecha=timezone.now()
            
        )

        return redirect(foro)

    hilos = hilo.objects.all().order_by('-fecha')

    context = {
        'hilos': hilos,
    }

    return render(request, 'forum.html', context)
