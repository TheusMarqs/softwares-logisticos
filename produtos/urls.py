from django.urls import path
from .views import ProdutoCreate, ProdutoUpdate, ProdutoDelete

urlpatterns = [
    path('tabela_produtos', ProdutoCreate.as_view(), name='tabela_produtos'),
    path('update_produto/<int:pk>', ProdutoUpdate.as_view(), name='update_produto'),
    path('delete_produto/<int:pk>', ProdutoDelete.as_view(), name='delete_produto'),
]