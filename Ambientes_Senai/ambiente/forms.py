from django import forms

TIPO_USUARIOS = (
    ("COORDENADOR", "Coordenador"),
    ("PROFESSOR", "Professor"),
)

class FormReserva(forms.Form):
    data = forms.DateField(label='Data', widget=forms.DateInput(attrs={'type': 'date'}))

class FormCadastro(forms.Form):
    nome = forms.CharField(max_length=20)
    sobrenome = forms.CharField(max_length=20)
    username = forms.CharField(max_length=20)
    senha = forms.CharField(max_length=20)
    cargo = forms.CharField(
        max_length=15,
        initial='PROFESSOR',
        widget=forms.HiddenInput()
    )

class FormLogin(forms.Form):
    user = forms.CharField(label="Usuário", max_length=20)
    password = forms.CharField(label="Senha", widget=forms.PasswordInputtrs)