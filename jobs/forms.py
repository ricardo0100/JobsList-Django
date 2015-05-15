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
