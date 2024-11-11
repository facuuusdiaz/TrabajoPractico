# capa de servicio/lógica de negocio

from ..persistence import repositories
from django.contrib.auth import get_user
from ..transport.transport import getAllImages as get_data_from_api
from ..utilities.translator import fromRequestIntoCard

################################################################################################
def getAllImages(input=None):
    json_collection = get_data_from_api(input)  # Llama a la función de transport.py
    images = []  # Inicializa la lista de imágenes (Cards)

    # Recorre la colección de datos JSON crudos y crea objetos Card
    for item in json_collection:
        try:
            # Verifica si la clave 'image' está presente
            if 'image' in item:
                # Convierte el item en un objeto Card y agrégalo a la lista
                images.append(fromRequestIntoCard(item))
            else:
                print("[services.py]: Se encontró un objeto sin clave 'image', omitiendo...")

        except KeyError:
            # Manejo de errores en caso de claves faltantes
            print("[services.py]: Error al procesar un objeto, omitiendo...")
            pass  # Continua con el siguiente elemento

    # Aplica el filtro si se proporciona input
    if input:
        images = [image for image in images if input.lower() in image.name.lower()]

################################################################################################
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