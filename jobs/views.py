from django.http import HttpResponse
from django.template import RequestContext, loader
from jobs.forms import LoginForm


def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, {

    })
    return HttpResponse(template.render(context))


def login(request):
    form = LoginForm()
    template = loader.get_template('login.html')
    context = RequestContext(request, {
        "form": form
    })
    return HttpResponse(template.render(context))
