from rest_framework import serializers
from jobs.models import Tarefa, Alarme

class TarefaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tarefa
        fields = ('titulo', )
