from django import forms


class LoginForm(forms.Form):

    email = forms.EmailField(label='E-mail', error_messages={'required': 'Informe seu e-mail'})
    senha = forms.CharField(widget=forms.PasswordInput, error_messages={'required': 'Informe sua senha'})
    sempre_logado = forms.BooleanField(label='Manter logado', required=False)
