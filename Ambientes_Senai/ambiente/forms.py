from django import forms

TIPO_USUARIOS = (
    ("COORDENADOR", "Coordenador"),
    ("PROFESSOR", "Professor"),
)

class FormLogin(forms.Form):
    username = forms.CharField(max_length=20,
        widget=forms.TextInput(attrs={'placeholder':'Nome de usuário', 'class': 'form-control'}))
    password = forms.CharField(max_length=20,
        widget=forms.PasswordInput(attrs={'placeholder':'Senha', 'class':'form-control'})
        )

class FormCadastro(forms.Form):
    nome = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': 'Nome', 'class': 'form-control'})
    )
    sobrenome = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': 'Sobrenome', 'class': 'form-control'})
    )
    username = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': 'Nome de usuário', 'class': 'form-control'})
    )
    senha = forms.CharField(
        max_length=20,
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha', 'class': 'form-control'})
    )


class FormReserva(forms.Form):
    data = forms.DateField(label='Data', widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    horario = forms.TimeField(label='Horario_Inicial', widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}))
    hora_final = forms.TimeField(label='Horario_Final', widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}))

class FormAmbiente(forms.Form):
    titulo = forms.CharField(max_length=50)
    descricao = forms.CharField(max_length=300)
    sala = forms.CharField(max_length=50)

class FormPesquisa(forms.Form):
    pesquisa = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Pesquisar', 'class': 'form-control'})) #Campo de pesquisa para buscar ambientes