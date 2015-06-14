# JobsList-Django

Trabalho final da Disciplina de OTES-02 (Programação Web)
Ricardo Gehrke Filho
UDESC CCT

##Estrutura de dados (Models)##

**Tarefa**

- titulo
- descricao
- vencimento
- concluida

**Alarme**

- tipo
- tarefa - FK(Tarefa)
- horario
- ativo


##Principais tecnologias##

**Django 1.8.1**
Framework web em python

**Bootstrap 3.3.4**
Framework front-end (CSS e JS)


---


##Instalação do Ambiente de Desenvolvimento no Mac OSX##

**Pré requisitos**

-Xcode


**HomeBrew**

```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

**Python**
```
brew install python
brew install python3
```

**Virtual Env**

```
pip install virtualenv
pip install virtualenvwrapper
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv otes02 --python=/usr/local/bin/python3
```

**PostgreSQL**

```
PYTHON=/usr/local/bin/python brew install postgresql
initdb -A trust /usr/local/var/postgres
initdb /usr/local/var/postgres -E utf8
```

Trocar a versão do PostgreSQL para a instalada
```
mkdir -p ~/Library/LaunchAgents
cp /usr/local/Cellar/postgresql/9.1.4/homebrew.mxcl.postgresql.plist ~/Library/LaunchAgents/
launchctl load -w ~/Library/LaunchAgents/homebrew.mxcl.postgresql.plist

```

Criar database
```
createdb otes02
```

**Requirements**
```
pip install -r requirements.txt
```

Configurar a variável de ambiente DATABASE_URL=postgres://user:password@localhost:5432/otes02

```
python manage.py syncdb
```
