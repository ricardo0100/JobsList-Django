import datetime
import json
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.template import RequestContext
from django_ajax.decorators import ajax
from jobs.forms import NovaTarefaForm, NovoAlarmeForm, NovoGrupoForm
from jobs.models import Tarefa, Alarme, Grupo
from django.utils import timezone


@ajax
@login_required(login_url='/login')
def lista_de_tarefas(request, tipo_lista):
    user = request.user

    filtro = Q()
    if tipo_lista == 'nao_vencidas':
        filtro = Q(Q(concluida=False) | Q(vencimento__lt=timezone.now(), concluida=False))
    elif tipo_lista == 'hoje':
        import datetime
        hoje = datetime.date.today()
        filtro = Q(vencimento__year=hoje.year, vencimento__month=hoje.month, vencimento__day=hoje.day)
    elif tipo_lista == 'concluidas':
        import datetime
        filtro = Q(concluida=True)

    grupos_ids = [int(grupo_id) for grupo_id in request.GET.getlist('grupos_ids[]')]

    if grupos_ids:
        grupos = Grupo.objects.filter(id__in=grupos_ids, usuario=user)
        filtro &= Q(grupo__in=grupos)

        if 0 in grupos_ids:
            filtro |= Q(grupo=None)

    order_by = 'vencimento'
    ordenacao = request.GET.get('ordenacao', '')

    if ordenacao == 'criacao':
        order_by = 'created'

    if ordenacao == 'titulo':
        order_by = 'titulo'

    tarefas = Tarefa.objects.filter(filtro, usuario=user).order_by(order_by)

    template = loader.get_template('listagem_tarefas.html')
    context = RequestContext(request, {
        'tarefas': tarefas
    })
    return HttpResponse(template.render(context))


@ajax
@login_required(login_url='/login')
def nova_tarefa(request, id_tarefa=None):
    user = request.user

    tarefa = None
    form = NovaTarefaForm(user)

    if id_tarefa:
        tarefa = Tarefa.objects.get(id=id_tarefa, usuario=user)

        if not request.method == 'POST':
            form = NovaTarefaForm(user, tarefa.grupo_id, initial={
                'titulo': tarefa.titulo,
                'descricao': tarefa.descricao,
                'vencimento': tarefa.vencimento
            })

    if request.method == 'POST':
        grupo_id = tarefa.grupo_id if tarefa else None
        form = NovaTarefaForm(user, grupo_id, request.POST)

        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            descricao = form.cleaned_data['descricao']
            vencimento = form.cleaned_data['vencimento']
            grupo_id = int(form.cleaned_data['grupo'])

            if grupo_id == 0:
                grupo = None
            else:
                grupo = Grupo.objects.get(id=grupo_id, usuario=user)

            if not tarefa:
                tarefa = Tarefa()
                tarefa.usuario = user

            tarefa.titulo = titulo
            tarefa.descricao = descricao
            tarefa.vencimento = vencimento
            tarefa.grupo = grupo

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
    usuario = request.user

    form = NovoAlarmeForm(request.POST)

    if form.is_valid():
        horario = form.cleaned_data['horario']
        # TODO: Criar alarme de outra forma mais bonita
        alarme = Alarme()
        alarme.tarefa = tarefa
        alarme.usuario = usuario
        alarme.horario = horario
        alarme.ativo = True
        alarme.save()

        destinatario = usuario.email
        assunto = 'Alarme para a tarefa {0}'.format(tarefa.titulo)
        mensagem = assunto

        countdown = horario - timezone.now()

        from tasks import enviar_alarme_por_email
        enviar_alarme_por_email.apply_async((destinatario, assunto, mensagem, ), countdown=countdown.seconds)

        return redirect('/')
    else:
        return HttpResponse(json.dumps(form.errors['horario'][0]))

@ajax
@login_required(login_url='/login')
def excluir_alarme(request, id_alarme):
    user = request.user
    alarme = Alarme.objects.get(id=id_alarme, usuario=user)
    alarme.delete()
    return redirect('/')


@ajax
@login_required(login_url='/login')
def lista_grupos(request):
    user = request.user
    grupos = Grupo.objects.filter(usuario=user)

    template = loader.get_template('lista_grupos.html')
    context = RequestContext(request, {
        'grupos': grupos
    })
    return HttpResponse(template.render(context))

@ajax
@login_required(login_url='/login')
def novo_grupo(request, id_grupo=None):
    user = request.user
    grupo = None
    form = NovoGrupoForm()

    if id_grupo:
        grupo = Grupo.objects.get(id=id_grupo, usuario=user)

        if not request.method == 'POST':
            form = NovoGrupoForm(initial={
                'nome': grupo.nome
            })

    if request.method == 'POST':
        form = NovoGrupoForm(request.POST)

        if form.is_valid():
            nome = form.cleaned_data['nome']
            if not grupo:
                grupo = Grupo()
                grupo.usuario = user

            grupo.nome = nome
            grupo.save()
            return redirect('/')

    template = loader.get_template('modals/edicao_grupo.html')
    context = RequestContext(request, {
        'form': form,
        'grupo': grupo,
    })
    return HttpResponse(template.render(context))

@ajax
@login_required(login_url='/login')
def excluir_grupo(request):
    if request.method == 'POST':
        id_grupo = request.POST['id_grupo']
        grupo = Grupo.objects.get(id=id_grupo, usuario=request.user)
        grupo.delete()
        return redirect('/')
    else:
        id_grupo = request.GET['id_grupo']
        grupo = Grupo.objects.get(id=id_grupo, usuario=request.user)
        template = loader.get_template('modals/excluir_grupo.html')
        context = RequestContext(request, {
            'grupo': grupo
        })
        return HttpResponse(template.render(context))
