from django.conf.urls import url

from . import views
from django.views.generic import TemplateView
from jobs import ajax

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^lista/$', views.lista, name='lista'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^cadastro/', views.cadastro, name='cadastro'),
    url(r'^ajax/lista-de-todas-as-tarefas/', ajax.lista_de_tarefas, {'tipo_lista': 'todas'}, name='lista_de_todas_as_tarefas'),
    url(r'^ajax/lista-nao-vencidas/', ajax.lista_de_tarefas, {'tipo_lista': 'nao_vencidas'}, name='lista_nao_vencidas'),
    url(r'^ajax/lista-hoje/', ajax.lista_de_tarefas, {'tipo_lista': 'hoje'}, name='lista_hoje'),
    url(r'^ajax/cadastro-tarefa/', ajax.nova_tarefa, name='cadastro_de_tarefa'),
    url(r'^ajax/editar-tarefa/(?P<id_tarefa>[0-9]+)/$', ajax.nova_tarefa, name='edicao_de_tarefa'),
    url(r'^ajax/confirmacao-exclusao-tarefa/', ajax.excluir_tarefa, name='confirmacao_exclusao_tarefa'),
    url(r'^ajax/excluir-tarefa/', ajax.excluir_tarefa, name='excluir_tarefa'),
    url(r'^ajax/marcar-tarefa-concluida/', ajax.marcar_tarefa_como_concluida, name='marcar_tarefa_concluida'),
]
