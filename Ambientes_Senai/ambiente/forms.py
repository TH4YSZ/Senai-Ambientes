from django import forms

TIPO_USUARIOS = (
    ("COORDENADOR", "Coordenador"),
    ("PROFESSOR", "Professor"),
)


class FormLogin(forms.Form):
    username = forms.CharField(
        label="Usuário",
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': 'Nome de Usuário', 'class': 'form-control'})
    )
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha', 'class': 'form-control'})
    )


class FormCadastro(forms.Form):
    nome = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': 'Nome', 'class': 'form-control'}))

    sobrenome = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': 'Sobrenome', 'class': 'form-control'}))

    username = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': 'Nome de Usuário', 'class': 'form-control'}))

    senha = forms.CharField(
        max_length=20,
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha', 'class': 'form-control'}))
    cargo = forms.ChoiceField(label="Cargo", choices=TIPO_USUARIOS, initial='PROFESSOR')


class FormReserva(forms.Form):
    data = forms.DateField(label='Data', widget=forms.DateInput(attrs={'type': 'date'}))
    horario = forms.TimeField(label='Horário', widget=forms.TimeInput(attrs={'type': 'time'}))
