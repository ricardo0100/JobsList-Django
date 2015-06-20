from rest_framework import serializers
from jobs.models import Tarefa, Alarme, Grupo


class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = ('created', 'modified', 'usuario', 'titulo', 'descricao', 'vencimento', 'concluida', 'grupo', )


class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = ('created', 'modified', 'usuario', 'nome', )

class AlarmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alarme
        fields = ('created', 'modified', 'usuario', 'tipo', 'tarefa', 'horario', 'ativo')
