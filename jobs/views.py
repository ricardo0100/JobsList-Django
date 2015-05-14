from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import RequestContext, loader
from jobs.forms import LoginForm
from jobs.template_snippets import CustomFormErrorList


@login_required(login_url='/login')
def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, {

    })
    return HttpResponse(template.render(context))


def login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST, error_class=CustomFormErrorList)
        if form.is_valid():
            username = User.objects.filter(email=form.cleaned_data['email'])
            password = form
    else:
        form = LoginForm(error_class=CustomFormErrorList)

    template = loader.get_template('login.html')
    context = RequestContext(request, {
        "form": form
    })
    return HttpResponse(template.render(context))
