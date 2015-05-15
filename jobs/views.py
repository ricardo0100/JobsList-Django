import django
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import RequestContext, loader
from jobs.forms import LoginForm, CadastroUsuarioForm


@login_required(login_url='/login')
def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, {

    })
    return HttpResponse(template.render(context))


def login(request, mostrar_mensagem_logout=False):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                user = User.objects.filter(email=email)
                username = user[0].username
                password = form.cleaned_data['senha']

                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        django.contrib.auth.login(request, user)
                        return redirect("/")
                    else:
                        form.add_error(None, 'Usuário inativo')
                else:
                    form.add_error(None, 'Senha incorreta')
            else:
                form.add_error(None, 'Usuário não existe')
    else:
        form = LoginForm()

    template = loader.get_template('autenticacao/login.html')
    context = RequestContext(request, {
        'form': form,
        'mostrar_mensagem_logout': mostrar_mensagem_logout
    })
    return HttpResponse(template.render(context))


def logout(request):
    django.contrib.auth.logout(request)
    return login(request, mostrar_mensagem_logout=True)


def cadastro(request):
    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']

            confirmacao_senha = form.cleaned_data['confirmacao_senha']

            user = User.objects.create_user(nome, email, senha)
            user.save()

            return login(request)

    else:
        form = CadastroUsuarioForm()

    template = loader.get_template('autenticacao/cadastro.html')
    context = RequestContext(request, {
        'form': form
    })
    return HttpResponse(template.render(context))
