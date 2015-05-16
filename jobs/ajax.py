from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.template import RequestContext
from django_ajax.decorators import ajax
from jobs.forms import NovaTarefaForm


@ajax
@login_required
def nova_tarefa(request):
    if request.method == 'POST':
        form = NovaTarefaForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = NovaTarefaForm()

    template = loader.get_template('modals/nova_tarefa.html')
    context = RequestContext(request, {
        'form': form
    })
    return HttpResponse(template.render(context))
