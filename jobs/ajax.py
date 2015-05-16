from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.template import RequestContext
from django_ajax.decorators import ajax

@ajax
@login_required
def cadastro_jobs(request):
    template = loader.get_template('modals/nova_tarefa.html')
    context = RequestContext(request, {
        # 'form': form
    })
    return HttpResponse(template.render(context))
