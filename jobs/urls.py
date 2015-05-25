from django.conf.urls import url

from . import views
from jobs import ajax

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^cadastro/', views.cadastro, name='cadastro'),
    url(r'^ajax/cadastro-tarefa/', ajax.nova_tarefa, name='cadastro_jobs'),
    url(r'^ajax/confirmacao-exclusao-tarefa/', ajax.excluir_tarefa, name='confirmacao_exclusao_tarefa'),
    url(r'^ajax/excluir-tarefa/', ajax.excluir_tarefa, name='excluir_tarefa'),
]
