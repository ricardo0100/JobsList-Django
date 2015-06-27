from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from jobs.models import Tarefa, Grupo, Alarme
from jobs.serializers import TarefaSerializer, GrupoSerializer, AlarmeSerializer


class TarefaViewSet(viewsets.ModelViewSet):

    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    # permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        user = User.objects.get(email='murielkong@gmail.com')
        return Tarefa.objects.filter(usuario=user)


class GrupoViewSet(viewsets.ModelViewSet):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer
    # permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        user = User.objects.get(email='murielkong@gmail.com')
        return Grupo.objects.filter(usuario=user)


class AlarmeViewSet(viewsets.ModelViewSet):
    queryset = Alarme.objects.all()
    serializer_class = AlarmeSerializer
    # permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        user = User.objects.get(email='murielkong@gmail.com')
        return Alarme.objects.filter(usuario=user)
