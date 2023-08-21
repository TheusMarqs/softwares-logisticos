from django.urls import path
from .views import RegistrarCreate, RegistrosList, RegistroUpdate
from . import views

urlpatterns = [
    path('registrar/', RegistrarCreate.as_view(), name="registrar"),
    path('registros/', RegistrosList.as_view(), name="registros"),
    path('update_registro/<int:pk>', RegistroUpdate.as_view(), name="update_registro")
]
