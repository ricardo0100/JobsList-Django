from rest_framework import viewsets
from jobs.models import Tarefa
from jobs.serializers import TarefaSerializer


class TarefaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
