from datetimewidget.widgets import DateTimeWidget
from django import forms
from jobs.models import Grupo
from jobs.template_snippets import CustomFormErrorList


class LoginForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.error_class = CustomFormErrorList

    email = forms.EmailField(label='E-mail', error_messages={'required': 'Informe seu e-mail'})
    senha = forms.CharField(widget=forms.PasswordInput, error_messages={'required': 'Informe sua senha'})


class CadastroUsuarioForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(CadastroUsuarioForm, self).__init__(*args, **kwargs)
        self.error_class = CustomFormErrorList

    nome = forms.CharField(label='Nome', error_messages={'required': 'Informe seu nome'}, max_length=30)
    email = forms.EmailField(label='E-mail', error_messages={'required': 'Informe seu e-mail'})
    senha = forms.CharField(widget=forms.PasswordInput, error_messages={'required': 'Informe sua senha'})
    confirmacao_senha = forms.CharField(label='Confirmação da senha', widget=forms.PasswordInput,
                                        error_messages={'required': 'Informe sua senha novamente'})


class NovaTarefaForm(forms.Form):
    titulo = forms.CharField(label='Título', error_messages={'required': 'Dê um nome para a tarefa'}, max_length=80)
    descricao = forms.CharField(label='Descrição', widget=forms.Textarea, required=False)
    vencimento = forms.DateTimeField(label='Vencimento',
                                     widget=DateTimeWidget(usel10n=True, bootstrap_version=3),
                                     required=False)

    def __init__(self, user, grupo_inicial=0, *args, **kwargs):
        super(NovaTarefaForm, self).__init__(*args, **kwargs)

        self.error_class = CustomFormErrorList

        self.fields['grupo'] = forms.ChoiceField(
            choices=[(0, '')] + [(o.id, str(o)) for o in Grupo.objects.filter(usuario=user)],
            initial=grupo_inicial
        )


class NovoAlarmeForm(forms.Form):
    horario = forms.DateTimeField(label='Horário',
                                  widget=DateTimeWidget(usel10n=True, bootstrap_version=3))


class NovoGrupoForm(forms.Form):
    nome = forms.CharField(label='Nome', error_messages={'required': 'Informe o nome do grupo'}, max_length=40)

    def __init__(self,  *args, **kwargs):
        super(NovoGrupoForm, self).__init__(*args, **kwargs)

        self.error_class = CustomFormErrorList
