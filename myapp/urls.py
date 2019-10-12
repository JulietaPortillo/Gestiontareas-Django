from django.urls import path
from myapp.views import index

urlpatterns = [
    path("", index),
    # Aqui puedes agregar mas rutas por ejem. path("about/", aboutview)
]
