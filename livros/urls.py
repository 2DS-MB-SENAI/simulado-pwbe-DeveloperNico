from django.urls import path
from . import views

urlpatterns = [
    path('livros/', views.listar_livros, name='listar_livros'),
    path('novo/', views.crud_create, name='crud_create'),
    path('atualizar/<int:pk>', views.crud_update, name='crud_update'),
    path('deletar/<int:pk>', views.crud_delete, name='crud_delete')
]