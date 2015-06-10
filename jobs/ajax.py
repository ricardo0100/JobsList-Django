import json
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.template import RequestContext
from django_ajax.decorators import ajax
from jobs.forms import NovaTarefaForm, NovoAlarmeForm
from jobs.models import Tarefa, Alarme
from django.utils import timezone


@ajax
@login_required(login_url='/login')
def lista_de_tarefas(request, tipo_lista):
    if tipo_lista == 'todas':
        filtro = Q()
    elif tipo_lista == 'nao_vencidas':
        filtro = Q(Q(concluida=False) | Q(vencimento__lt=timezone.now(), concluida=False))
    elif tipo_lista == 'hoje':
        import datetime
        hoje = datetime.date.today()
        filtro = Q(vencimento__year=hoje.year, vencimento__month=hoje.month, vencimento__day=hoje.day)
    elif tipo_lista == 'concluidas':
        import datetime
        filtro = Q(concluida=True)

    user = request.user

    tarefas = Tarefa.objects.filter(filtro, usuario=user).order_by('titulo')

    template = loader.get_template('listagem_tarefas.html')
    context = RequestContext(request, {
        'tarefas': tarefas
    })
    return HttpResponse(template.render(context))


@ajax
@login_required(login_url='/login')
def nova_tarefa(request, id_tarefa=None):
    tarefa = None
    form = NovaTarefaForm()

    if id_tarefa:
        tarefa = Tarefa.objects.get(id=id_tarefa, usuario=request.user)

        if not request.method == 'POST':
            form = NovaTarefaForm(initial={
                'titulo': tarefa.titulo,
                'descricao': tarefa.descricao,
                'vencimento': tarefa.vencimento,
            })

    if request.method == 'POST':
        form = NovaTarefaForm(request.POST)

        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            descricao = form.cleaned_data['descricao']
            vencimento = form.cleaned_data['vencimento']

            if not tarefa:
                tarefa = Tarefa()
                tarefa.usuario = request.user

            tarefa.titulo = titulo
            tarefa.descricao = descricao
            tarefa.vencimento = vencimento

            tarefa.save()
            return redirect('/')

    template = loader.get_template('modals/edicao_tarefa.html')
    context = RequestContext(request, {
        'form': form,
        'tarefa': tarefa,
    })
    return HttpResponse(template.render(context))


@ajax
@login_required(login_url='/login')
def excluir_tarefa(request):
    if request.method == 'POST':
        id_tarefa = request.POST['id_tarefa']
        tarefa = Tarefa.objects.get(id=id_tarefa, usuario=request.user)
        tarefa.delete()
        return redirect('/')
    else:
        id_tarefa = request.GET['id_tarefa']
        tarefa = Tarefa.objects.get(id=id_tarefa, usuario=request.user)
        template = loader.get_template('modals/excluir_tarefa.html')
        context = RequestContext(request, {
            'tarefa': tarefa
        })
        return HttpResponse(template.render(context))


@ajax
@login_required(login_url='/login')
def marcar_tarefa_como_concluida(request):
    tarefa_id = request.GET['tarefa_id']
    concluida = False if request.GET['concluida'] == 'false' else True

    user = request.user
    tarefa = Tarefa.objects.get(id=tarefa_id, usuario=user)
    tarefa.concluida = concluida
    tarefa.save()

    return HttpResponse(status=200)

@ajax
@login_required(login_url='/login')
def lista_alarmes(request, id_tarefa):
    tarefa = Tarefa.objects.get(id=id_tarefa, usuario=request.user)
    alarmes = Alarme.objects.filter(tarefa=tarefa).order_by('-horario')
    form = NovoAlarmeForm()

    template = loader.get_template('modals/alarmes.html')
    context = RequestContext(request, {
        'alarmes': alarmes,
        'tarefa': tarefa,
        'form_novo_alarme': form
    })
    return HttpResponse(template.render(context))

@ajax
@login_required(login_url='/login')
def salvar_novo_alarme(request, id_tarefa):
    tarefa = Tarefa.objects.get(id=id_tarefa, usuario=request.user)
    form = NovoAlarmeForm(request.POST)

    if form.is_valid():
        horario = form.cleaned_data['horario']
        # TODO: Criar alarme de outra forma mais bonita
        alarme = Alarme()
        alarme.tarefa = tarefa
        alarme.usuario = request.user
        alarme.horario = horario
        alarme.ativo = True
        alarme.save()
        return redirect('/')
    else:
        return HttpResponse(json.dumps(form.errors['horario'][0]))
