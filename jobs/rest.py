from rest_framework import viewsets, permissions
from jobs.models import Tarefa, Grupo, Alarme
from jobs.serializers import TarefaSerializer, GrupoSerializer, AlarmeSerializer


class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    # permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        return Tarefa.objects.filter()


class GrupoViewSet(viewsets.ModelViewSet):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer
    # permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        return Grupo.objects.filter()


class AlarmeViewSet(viewsets.ModelViewSet):
    queryset = Alarme.objects.all()
    serializer_class = AlarmeSerializer
    # permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        return Alarme.objects.filter()
