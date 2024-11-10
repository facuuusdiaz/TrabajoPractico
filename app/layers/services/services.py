# capa de servicio/lógica de negocio

from ..persistence import repositories
from ..utilities import translator
from django.contrib.auth import get_user
from . import transport  # Importa el módulo transport
from .models import Card  # Importa el modelo Card (si lo tienes)

def getAllImages(input=None):
    # Obtiene un listado de datos "crudos" desde la API, usando a transport.py.
    json_collection = transport.get_data(input)  # Pasa input a transport.get_data

    # Recorre cada dato crudo de la colección anterior, lo convierte en una Card y lo agrega a images.
    images = []
    for item in json_collection:
        # Crea una instancia de Card con los datos del item
        card = Card(
            name=item['name'],
            image=item['image'],
            status=item['status'],
            # ... otros campos de la Card ...
        )
        images.append(card)  # Agrega la Card a la lista

    return images

# añadir favoritos (usado desde el template 'home.html')
def saveFavourite(request):
    fav = '' # transformamos un request del template en una Card.
    fav.user = '' # le asignamos el usuario correspondiente.

    return repositories.saveFavourite(fav) # lo guardamos en la base.

# usados desde el template 'favourites.html'
def getAllFavourites(request):
    if not request.user.is_authenticated:
        return []
    else:
        user = get_user(request)

        favourite_list = [] # buscamos desde el repositories.py TODOS los favoritos del usuario (variable 'user').
        mapped_favourites = []

        for favourite in favourite_list:
            card = '' # transformamos cada favorito en una Card, y lo almacenamos en card.
            mapped_favourites.append(card)

        return mapped_favourites

def deleteFavourite(request):
    favId = request.POST.get('id')
    return repositories.deleteFavourite(favId) # borramos un favorito por su ID.