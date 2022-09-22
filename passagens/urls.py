from django.urls import path
from . import views

app_name = 'passagens'

urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),
  path('exibir-dados/', views.ExibirDadosView.as_view(), name='exibir-dados/')
]
