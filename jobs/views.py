import django
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
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
            user = User.objects.filter(email=form.cleaned_data['email'])
            if not user:
                raise Http404
            username = user[0].username
            password = form.cleaned_data['senha']

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    django.contrib.auth.login(request, user)
                    return redirect("/")
                else:
                    raise Http404
            else:
                raise Http404
    else:
        form = LoginForm(error_class=CustomFormErrorList)

    template = loader.get_template('login.html')
    context = RequestContext(request, {
        "form": form
    })
    return HttpResponse(template.render(context))


def logout(request):
    django.contrib.auth.logout(request)
    template = loader.get_template('logout.html')
    context = RequestContext(request, {

    })
    return HttpResponse(template.render(context))
