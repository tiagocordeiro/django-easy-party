# django-easy-party

[![Updates](https://pyup.io/repos/github/tiagocordeiro/django-easy-party/shield.svg)](https://pyup.io/repos/github/tiagocordeiro/django-easy-party/)
[![Python 3](https://pyup.io/repos/github/tiagocordeiro/django-easy-party/python-3-shield.svg)](https://pyup.io/repos/github/tiagocordeiro/django-easy-party/)
[![Python 3.8.2](https://img.shields.io/badge/python-3.8.2-blue.svg)](https://www.python.org/downloads/release/python-382/)
[![Django 3.0.4](https://img.shields.io/badge/django-3.0.4-blue.svg)](https://www.djangoproject.com/download/)
![Python application](https://github.com/tiagocordeiro/django-easy-party/workflows/Python%20application/badge.svg)
[![codecov](https://codecov.io/gh/tiagocordeiro/django-easy-party/branch/master/graph/badge.svg)](https://codecov.io/gh/tiagocordeiro/django-easy-party)
[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/tiagocordeiro/django-easy-party/blob/master/LICENSE)

### Como rodar o projeto
* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git https://github.com/tiagocordeiro/django-easy-party.git
cd django-easy-party
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```

### Configurar administrador
Para cria um usuário administrador
```
python manage.py createsuperuser --username dev --email dev@foo.bar
```

### Rodar em ambiente de desenvolvimento
Para rodar o projeto localmente
```
python manage.py runserver
```

### Testes, contribuição e dependências de desenvolvimento
Para instalar as dependências de desenvolvimento
```
pip install -r requirements-dev.txt
```

Para rodar os testes
```
python manage.py test -v 2
```

Para rodar os testes com relatório de cobertura.
```
coverage run manage.py test -v 2
coverage html
```

Verificando o `Code style`
```
pycodestyle .
flake8 .
```