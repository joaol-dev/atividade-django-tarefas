# Primeira Interface Web do Sistema de Gestão de Tarefas

## Alunos
- João Lucas Binttencourt Rocha - 202422927
- João Pedro Oliveira - 202422911
- José Carlos Silva Pimentel - 202422916
- Adriel dos Santos Azevedo - 202422733

## Objetivo

Criar a primeira interface web do Sistema de Gestão de Tarefas utilizando o framework Django, aplicando conceitos de projeto, aplicação, rotas (URLs), views e templates.

## Funcionalidades

### Página inicial (`/`)
Exibe um título, um texto de boas-vindas e um link para a lista de tarefas.

### Lista de tarefas (`/tarefas/`)
Exibe as tarefas cadastradas (título, prioridade e situação) usando `{% for %}` para percorrer a lista e `{% if %}` para tratar o caso de lista vazia. No momento, os dados são temporários e ficam definidos diretamente na view.

## Conceitos utilizados
- Estrutura de projeto Django (`startproject` e `startapp`)
- `INSTALLED_APPS`
- Roteamento de URLs (`urls.py` da app + `include()` no projeto)
- Views baseadas em função
- Templates com herança de pasta (`tarefas/templates/tarefas/`)
- Tags de template `{% for %}`, `{% if %}` e `{% url %}`

## Estrutura da atividade

```text
gestao_tarefas_django/
├── manage.py
├── requirements.txt
├── gestao_tarefas/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── tarefas/
    ├── urls.py
    ├── views.py
    └── templates/
        └── tarefas/
            ├── inicio.html
            └── lista.html
```

## Execução

Crie e ative um ambiente virtual, depois instale as dependências:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Inicie o servidor:

```bash
python manage.py runserver
```

Acesse no navegador:
- `http://127.0.0.1:8000/` — página inicial
- `http://127.0.0.1:8000/tarefas/` — lista de tarefas

## Limitações

As tarefas exibidas são dados temporários definidos na view `lista_tarefas`. Não há banco de dados nem persistência entre execuções nesta etapa.

## Extensão opcional
Possíveis evoluções: adicionar uma terceira tarefa, criar uma página de detalhes por índice, aplicar CSS para diferenciar tarefas pendentes/concluídas, ou filtrar apenas as pendentes na view.
