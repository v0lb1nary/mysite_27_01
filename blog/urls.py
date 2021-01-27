from django.urls import path
from . import views

app_name = 'blog'

rlpatterns =[
    path('', views.lista_postagem, name='lista_postagem'),
    path('<int:ano>/<int:mes>/<int:dia>/<slug:rotulo>/', views.detalhe_postagem, name='detalhe_postagem'),
    path('<int:post_id>/compartilhar/', views.compartilhar_postagens, name='compartilhar_postagens'),
]
