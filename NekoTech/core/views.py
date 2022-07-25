from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from core.forms import UserRegisterForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def store(request):
    return render(request, "core/store.html")

def salachat(request):
    return render(request, "core/salachat.html")

def aboutme(request):
    return render(request, "core/aboutme.html")

def login (request):
    if request.method == "POST":
        form = AuthenticationForm(request,data = request.POST)
        if form.is_valid():
            usuario = form.cleanned_data.get ('username')
            contra = form.cleanned_data.get ('password')

            user = authenticate(username=usuario, password=contra)
            if user is not None:
                login(request, user)
                return render (request,"core/login.html", {"mensaje": f"Bienvenido! {usuario}"} )
            
            else:
                return render (request,"core/login.html", {"mensaje": f"Error, datos incorrectos"} )
        
        else:
                return render (request,"core/login.html", {"mensaje": f"Error, formulario erroneo"} )

    form= AuthenticationForm()

    return render(request,"core/login.html", {'form':form} )

def register(request):

    if request.method =="POST":
        #form = UserCreationForm (request.POST)
        form = UserRegisterForm (request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            return render(request,"core/register.html",{"mensaje":"Usuario Creado :)"})
    else:       
        #form = UserCreationForm ()
        form = UserRegisterForm()
    return render(request,"core/register.html",{"form":form})