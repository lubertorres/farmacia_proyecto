from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name = 'admin-index' ),
    path('Detalleproducto/', producto, name = 'Producto' ),
    path('AboutUs/', aboutU, name = 'quienesSomos' ),
]
