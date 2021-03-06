from django.conf.urls import url, include
from rest_framework import routers

from . import views
from . import rest
from jobs import ajax

router = routers.DefaultRouter()
router.register(r'tarefas', rest.TarefaViewSet)
router.register(r'grupos', rest.GrupoViewSet)
router.register(r'alarmes', rest.AlarmeViewSet)

urlpatterns = [
    url(r'^api-rest/', include(router.urls)),
    url(r'^$', views.home, name='home'),
    url(r'^cadastro/', views.cadastro, name='cadastro'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),

    url(r'^lista/$', views.lista, name='lista'),

    url(r'^ajax/lista-de-todas-as-tarefas/', ajax.lista_de_tarefas, {'tipo_lista': 'todas'}, name='lista_de_todas_as_tarefas'),
    url(r'^ajax/lista-nao-vencidas/', ajax.lista_de_tarefas, {'tipo_lista': 'nao_vencidas'}, name='lista_nao_vencidas'),
    url(r'^ajax/lista-hoje/', ajax.lista_de_tarefas, {'tipo_lista': 'hoje'}, name='lista_hoje'),
    url(r'^ajax/lista-concluidas/', ajax.lista_de_tarefas, {'tipo_lista': 'concluidas'}, name='lista_concluidas'),

    url(r'^ajax/cadastro-tarefa/', ajax.nova_tarefa, name='cadastro_de_tarefa'),
    url(r'^ajax/editar-tarefa/(?P<id_tarefa>[0-9]+)/$', ajax.nova_tarefa, name='edicao_de_tarefa'),
    url(r'^ajax/confirmacao-exclusao-tarefa/', ajax.excluir_tarefa, name='confirmacao_exclusao_tarefa'),
    url(r'^ajax/excluir-tarefa/', ajax.excluir_tarefa, name='excluir_tarefa'),
    url(r'^ajax/marcar-tarefa-concluida/', ajax.marcar_tarefa_como_concluida, name='marcar_tarefa_concluida'),

    url(r'^ajax/lista-alarmes/(?P<id_tarefa>[0-9]+)/$', ajax.lista_alarmes, name='lista_alarmes'),
    url(r'^ajax/salvar-novo-alarme/(?P<id_tarefa>[0-9]+)/$', ajax.salvar_novo_alarme, name='salvar_novo_alarme'),
    url(r'^ajax/excluir-alarme/(?P<id_alarme>[0-9]+)/$', ajax.excluir_alarme, name='excluir_alarme'),


    url(r'^ajax/lista-grupos/$', ajax.lista_grupos, name='lista_grupos'),
    url(r'^ajax/novo-grupo/$', ajax.novo_grupo, name='cadastro_de_grupo'),
    url(r'^ajax/editar-grupo/(?P<id_grupo>[0-9]+)/$', ajax.novo_grupo, name='edicao_de_grupo'),
    url(r'^ajax/exclusao-grupo/', ajax.excluir_grupo, name='exclusao_grupo'),
]
