# capa de vista/presentación

from django.shortcuts import redirect, render
from .layers.services import services
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from . import services  # Importa el módulo services
#from .models import Favourite  # Importa el modelo Favourite (si lo tienes)

def index_page(request):
    return render(request, 'index.html')

# esta función obtiene 2 listados que corresponden a las imágenes de la API y los favoritos del usuario, y los usa para dibujar el correspondiente template.
# si el opcional de favoritos no está desarrollado, devuelve un listado vacío.

def home(request):
    images = services.getAllImages()  # Obtén las imágenes de la API
    favourite_list = []
    if request.user.is_authenticated:  # Si el usuario está autenticado
        #favourite_list = Favourite.objects.filter(user=request.user)  # Obtén los favoritos del usuario
        # (Si no tienes el modelo Favourite, puedes usar otra lógica para obtener los favoritos)
        # ... (lógica para obtener los favoritos del usuario, si está implementada)
        pass  # Reemplaza con tu lógica de favoritos
    return render(request, 'home.html', {'images': images, 'favourite_list': favourite_list})

def search(request):
    search_msg = request.POST.get('query', '')

    # si el texto ingresado no es vacío, trae las imágenes y favoritos desde services.py,
    # y luego renderiza el template (similar a home).
    if (search_msg != ''):
        pass
    else:
        return redirect('home')


# Estas funciones se usan cuando el usuario está logueado en la aplicación.
@login_required
def getAllFavouritesByUser(request):
    favourite_list = []
    return render(request, 'favourites.html', { 'favourite_list': favourite_list })

@login_required
def saveFavourite(request):
    pass

@login_required
def deleteFavourite(request):
    pass

@login_required
def exit(request):
    pass