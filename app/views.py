# capa de vista/presentación

from django.shortcuts import redirect, render
from .layers.services import services
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from layers.transport.transport import getAllImages
from layers.utilities.translator import fromRequestIntoCard


def index_page(request):
    return render(request, 'index.html')

# esta función obtiene 2 listados que corresponden a las imágenes de la API y los favoritos del usuario, y los usa para dibujar el correspondiente template.
# si el opcional de favoritos no está desarrollado, devuelve un listado vacío.

def home(request):
    # Obtener personajes de la API
    images_data = getAllImages()
    images = [fromRequestIntoCard(image_data) for image_data in images_data]

    # Obtener personajes de la base de datos (ejemplo)
    # repo_data = Character.objects.all()  # Consulta a la base de datos (reemplaza con tu lógica)
    # db_characters = [fromRepositoryIntoCard(repo_dict) for repo_dict in repo_data]
    db_characters = []  # Inicializa como lista vacía si no tienes la lógica de la BD

    # Mantener la lista de favoritos vacía por ahora
    favourite_list = []

    if request.method == 'POST':  # Si se recibe un formulario
        if 'add_character' in request.POST:  # Si el formulario es para agregar un personaje
            card = fromTemplateIntoCard(request)  # Convertir datos del formulario en Card
            # ... (guardar card en la base de datos - agrega tu lógica aquí)
        # ... (manejar otros formularios si es necesario)

    return render(request, 'home.html', {
        'images': images,
        'db_characters': db_characters,
        'favourite_list': favourite_list
    })

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