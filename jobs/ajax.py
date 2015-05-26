from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.template import RequestContext
from django_ajax.decorators import ajax
from jobs.forms import NovaTarefaForm
from jobs.models import Tarefa


@ajax
@login_required(login_url='/login')
def nova_tarefa(request, id_tarefa=None):
    tarefa = None
    if id_tarefa:
        tarefa = Tarefa.objects.get(id=id_tarefa)
        if not request.method == 'POST':
            form = NovaTarefaForm(initial={
                'titulo': tarefa.titulo,
                'descricao': tarefa.descricao,
            })
    else:
        form = NovaTarefaForm()

    if request.method == 'POST':
        form = NovaTarefaForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            descricao = form.cleaned_data['descricao']
            if not tarefa:
                tarefa = Tarefa()
                tarefa.usuario = request.user
            tarefa.titulo = titulo
            tarefa.descricao = descricao
            tarefa.save()
            return redirect('/')

    template = loader.get_template('modals/nova_tarefa.html')
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
        tarefa = Tarefa.objects.get(id=id_tarefa)
        tarefa.delete()
        return redirect('/')
    else:
        id_tarefa = request.GET['id_tarefa']
        tarefa = Tarefa.objects.get(id=id_tarefa)
        template = loader.get_template('modals/excluir_tarefa.html')
        context = RequestContext(request, {
            'tarefa': tarefa
        })
        return HttpResponse(template.render(context))
