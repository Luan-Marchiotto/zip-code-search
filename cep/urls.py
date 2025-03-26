from django.urls import path
from . import views

urlpatterns = [
    path('', views.busca_cep, name='cep'),
]
