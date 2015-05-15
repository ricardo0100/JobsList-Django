from django import forms


class LoginForm(forms.Form):

    email = forms.EmailField(label='E-mail', error_messages={'required': 'Informe seu e-mail'})
    senha = forms.CharField(widget=forms.PasswordInput, error_messages={'required': 'Informe sua senha'})


class CadastroUsuarioForm(forms.Form):
    nome = forms.CharField(label='Nome', error_messages={'required': 'Informe seu nome'})
    email = forms.EmailField(label='E-mail', error_messages={'required': 'Informe seu e-mail'})
    senha = forms.CharField(widget=forms.PasswordInput, error_messages={'required': 'Informe sua senha'})
    confirmacao_senha = forms.CharField(label='Confirmação da senha', widget=forms.PasswordInput,
                                        error_messages={'required': 'Informe sua senha novamente'})
