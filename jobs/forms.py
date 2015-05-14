from django import forms


class LoginForm(forms.Form):

    email = forms.EmailField(label='E-mail')
    senha = forms.CharField(widget=forms.PasswordInput)
    sempre_logado = forms.BooleanField(label='Manter logado')
