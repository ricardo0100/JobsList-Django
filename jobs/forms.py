from datetimewidget.widgets import DateTimeWidget
from django import forms
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

    nome = forms.CharField(label='Nome', error_messages={'required': 'Informe seu nome'})
    email = forms.EmailField(label='E-mail', error_messages={'required': 'Informe seu e-mail'})
    senha = forms.CharField(widget=forms.PasswordInput, error_messages={'required': 'Informe sua senha'})
    confirmacao_senha = forms.CharField(label='Confirmação da senha', widget=forms.PasswordInput,
                                        error_messages={'required': 'Informe sua senha novamente'})


class NovaTarefaForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(NovaTarefaForm, self).__init__(*args, **kwargs)
        self.error_class = CustomFormErrorList

    titulo = forms.CharField(label='Título', error_messages={'required': 'Dê um nome para a tarefa'})
    descricao = forms.CharField(label='Descrição', widget=forms.Textarea, required=False)
    vencimento = forms.DateTimeField(label='Vencimento',
                                     widget=DateTimeWidget(usel10n=True, bootstrap_version=3),
                                     required=False)


class NovoAlarmeForm(forms.Form):
    horario = forms.DateTimeField(label='Horário',
                                  widget=DateTimeWidget(usel10n=True, bootstrap_version=3))
