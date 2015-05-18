from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.template import RequestContext
from django_ajax.decorators import ajax
from jobs.forms import NovaTarefaForm
from jobs.models import Tarefa


@ajax
@login_required
def nova_tarefa(request):
    if request.method == 'POST':
        form = NovaTarefaForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            descricao = form.cleaned_data['descricao']
            Tarefa.objects.create(titulo=titulo, descricao=descricao)
            return redirect('/')
    else:
        form = NovaTarefaForm()

    template = loader.get_template('modals/nova_tarefa.html')
    context = RequestContext(request, {
        'form': form
    })
    return HttpResponse(template.render(context))
