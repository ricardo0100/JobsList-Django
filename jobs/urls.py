from django.conf.urls import url

from . import views
from jobs import ajax

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^cadastro/', views.cadastro, name='cadastro'),
    url(r'^ajax/cadastro-jobs/', ajax.nova_tarefa, name='cadastro_jobs'),
]
