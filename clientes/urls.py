from django.urls import path
from .views import ClienteCreate, ClienteUpdate, ClienteDelete

urlpatterns = [
    path('cadastrar_cliente', ClienteCreate.as_view(), name="cadastrar_cliente"),
    path('update_cliente/<int:pk>', ClienteUpdate.as_view(), name="update_cliente"),
    path('delete_cliente/<int:pk>', ClienteDelete.as_view(), name="delete_cliente"),
]