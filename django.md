### Criar um Ambiente Virtual Python

Para criar um ambiente virtual Python, siga estes passos:

1. Abra o terminal no Visual Studio Code. Use o atalho `Ctrl` + `no Windows ou `Cmd` +` no macOS.
2. Navegue até a pasta raiz do seu projeto, onde deseja criar o ambiente virtual.
3. Execute o seguinte comando para criar um ambiente virtual Python com `virtualenv`:
    
    No Windows:
    
    `python -m venv nome_do_ambiente`
    

## Ativar um Ambiente Virtual Python com PowerShell no Visual Studio Code

Para ativar um ambiente virtual Python usando o PowerShell no Visual Studio Code, siga os seguintes passos:

1. Abra o terminal no Visual Studio Code. Você pode usar o atalho `Ctrl` + `no Windows ou `Cmd` +` no macOS.
2. Navegue até a pasta raiz do seu ambiente virtual ou forneça o caminho completo para a pasta do ambiente virtual.
3. Use o comando `.\nome_do_ambiente\Scripts\Activate.ps1` para ativar o ambiente virtual. Certifique-se de substituir `nome_do_ambiente` pelo nome real do ambiente virtual.

Com sua `venv` já ativada você pode instalar o Django utilizando o `pip`, como mostra o comando a seguir:

```python
pip install django
```

Você pode verificar se o Django foi instalado corretamente executando o seguinte comando:

```python
python -m django --version
```

Agora que a instalação foi concluída, você pode criar um novo projeto Django. Ainda no terminal e com a `venv` ativada, execute o seguinte comando:

```python
 django-admin startproject 'nome_do_projeto'
```

Após isso, navegue para o diretório onde está o arquivo `manage.py` do seu projeto, e execute o seguinte comando:

```python
 cd 'diretorio com o arquivo manage,py'
 python manage.py runserver
```

Para configurar o banco de dados, é necessário criar as migrações e aplicá-las para que as tabelas e esquemas do banco de dados sejam criados ou atualizados de acordo. Para isso, você pode utilizar os seguintes comandos em seu terminal:

```python
 python manage.py migrate
```

Crie um Super usuario para fazer a autenticação do djangle, com o seguinte comando:

```python
 python .\manage.py createsuperuser

 # User: 'admin', Password:'123'
```

Para criar um app novo para o projeto, use o comando:

```python
 python .\manage.py startapp
 ```
