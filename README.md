# 🏢 DZADATA

Sistema de cadastro e gerenciamento de funcionários desenvolvido em **Python**, utilizando **Programação Orientada a Objetos (POO)**, persistência de dados em **JSON** e organização do projeto em camadas.

> Projeto desenvolvido para prática de CRUD, Programação Orientada a Objetos, manipulação de arquivos JSON, modularização e organização de aplicações Python.

---

## 📖 Sobre o Projeto

O **DZADATA** é uma aplicação de terminal desenvolvida para simular um sistema de **Recursos Humanos**, permitindo o gerenciamento de funcionários.

O sistema realiza operações de **cadastro, consulta, atualização e exclusão de funcionários**, além de possuir persistência dos dados em arquivo JSON e geração automática de funcionários fictícios para testes e demonstração.

---

## ✨ Funcionalidades

* Cadastro de funcionários
* Listagem completa dos funcionários
* Consulta por chapa
* Consulta por nome
* Consulta por filial
* Consulta por departamento
* Edição de informações cadastrais
* Exclusão de funcionários
* Persistência de dados em JSON
* Geração automática de funcionários fictícios
* Geração de chapas únicas
* Cálculo do tempo de empresa
* Formatação monetária no padrão brasileiro
* Busca de funcionários sem diferenciação de acentos
* Validação de salário mínimo
* Validação da data de admissão

---

## 🚀 Tecnologias Utilizadas

* **Python 3.11+**
* **Rich** — interface e formatação no terminal
* **Faker** — geração de dados fictícios
* **JSON** — persistência dos dados
* **datetime** — manipulação de datas
* **python-dateutil** — cálculo de períodos e tempo de empresa
* **Programação Orientada a Objetos (POO)**

---

## 📦 Dependências

Instale as dependências com:

```bash
pip install rich faker python-dateutil
```

---

## 📂 Estrutura do Projeto

```text
DZADATA  /
│
├── models/
│   ├── __init__.py
│   └── funcionario.py
│
├── services/
│   ├── __init__.py
│   ├── arquivo_service.py
│   ├── automacao_service.py
│   └── funcionario_service.py
│
├── utils/
│   ├── __init__.py
│   └── helpers.py
│
├── views/
│   ├── __init__.py
│   └── menu.py
│
├── funcionarios.json
├── main.py
├── README.md
└── .gitignore
```

### Organização das camadas

| Diretório  | Responsabilidade                         |
| ---------- | ---------------------------------------- |
| `models`   | Representação das entidades do sistema   |
| `services` | Regras de negócio e operações do sistema |
| `views`    | Interface e interação com o usuário      |
| `utils`    | Funções auxiliares                       |
| `main.py`  | Ponto de entrada da aplicação            |

---

## ⚙️ Regras de Negócio

### 💰 Salário

* O salário mínimo permitido é de **R$ 1.621,00**.
* Não é permitido cadastrar funcionários com salário abaixo do mínimo.
* Durante a edição, não é permitido reduzir o salário atual do funcionário.

### 🆔 Chapa

* Cada funcionário possui uma chapa única.
* As chapas geradas automaticamente não podem se repetir.
* A chapa é gerenciada automaticamente pelo sistema.

### 📅 Data de Admissão

A data de admissão deve ser informada no formato:

```text
dd/mm/aaaa
```

Exemplo:

```text
15/08/2020
```

---

## 💾 Persistência dos Dados

Os funcionários são armazenados localmente no arquivo:

```text
funcionarios.json
```

Como o sistema permite o cadastro de vários funcionários, os registros são armazenados em uma lista de objetos JSON.

### Exemplo

```json
[
    {
        "chapa": 123456789,
        "nome": "JOÃO DA SILVA",
        "filial": "LONDRINA/PR",
        "departamento": "SUPERINTENDÊNCIA FINANCEIRA",
        "cargo": "ANALISTA DE SISTEMAS",
        "salario": 5500.00,
        "data_admissao": "2020-08-15"
    }
]
```

---

## 🚀 Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/davidzarur80/DZADATA.git
```

### 2. Entrar no diretório

```bash
cd DZADATA 
```

### 3. Criar ambiente virtual

#### Windows

```bash
python -m venv .venv
```

Ative o ambiente virtual:

```bash
.venv\Scripts\activate
```

#### Linux/macOS

```bash
python3 -m venv .venv
```

Ative o ambiente virtual:

```bash
source .venv/bin/activate
```

### 4. Instalar as dependências

```bash
pip install rich faker python-dateutil
```

---

## ▶️ Executando a Aplicação

Após instalar as dependências, execute:

```bash
python main.py
```

---

## 🖥️ Interface

A aplicação possui uma interface de terminal com as seguintes opções:

```text
============================================================

             Sistema de Cadastro de Funcionários

============================================================

[1] Cadastrar Funcionário
[2] Visualizar Funcionários
[3] Consultar Funcionário
[4] Editar Funcionário
[5] Excluir Funcionário
[6] Gerar Funcionários Aleatórios
[7] Sair
```

---

## 🔍 Exemplo de Cadastro

```text
Nome: JOÃO DA SILVA
Filial: LONDRINA/PR
Departamento: SUPERINTENDÊNCIA FINANCEIRA
Cargo: ANALISTA DE SISTEMAS
Salário: 5500
Data de admissão: 15/08/2020
```

Após o cadastro, o sistema gera automaticamente a chapa do funcionário e salva os dados no arquivo `funcionarios.json`.

---

## 🎲 Geração Automática de Funcionários

O sistema utiliza a biblioteca **Faker** para criar funcionários fictícios para testes e demonstração.

Os registros gerados possuem:

* Nome
* Filial
* Departamento
* Cargo
* Salário
* Data de admissão
* Chapa única

Por padrão, a opção de automação gera **30 funcionários**.

Essa funcionalidade facilita os testes das operações de consulta, edição, exclusão e listagem.

---

## 🏗️ Arquitetura

O projeto foi organizado em camadas para separar responsabilidades.

### Models

Responsável pela representação das entidades do sistema.

```text
Funcionario
```

O arquivo principal é:

```text
models/funcionario.py
```

---

### Services

Responsáveis pela lógica e pelas operações do sistema.

```text
services/
├── arquivo_service.py
├── automacao_service.py
└── funcionario_service.py
```

#### `arquivo_service.py`

Responsável pela leitura e gravação dos funcionários no arquivo JSON.

#### `automacao_service.py`

Responsável pela geração automática de funcionários fictícios utilizando o Faker.

#### `funcionario_service.py`

Responsável pelas operações relacionadas aos funcionários, como:

* Cadastro
* Consulta
* Edição
* Exclusão
* Listagem
* Validações

---

### Views

Responsável pela interação com o usuário.

```text
views/menu.py
```

Contém os menus e fluxos da aplicação no terminal.

---

### Utils

Contém funções auxiliares utilizadas em diferentes partes do sistema.

```text
utils/helpers.py
```

## 🎯 Objetivos de Aprendizagem

Este projeto foi desenvolvido para praticar:

* Programação Orientada a Objetos
* Classes e objetos
* Métodos e atributos
* Encapsulamento
* Manipulação de arquivos JSON
* Persistência de dados
* Modularização
* Separação de responsabilidades
* Tratamento de exceções
* Validação de dados
* Manipulação de datas
* Formatação de valores
* Bibliotecas externas
* Organização de projetos Python
* Arquitetura em camadas

---

## 👨‍💻 Autor

**David Zarur**

GitHub: https://github.com/davidzarur80

---

## 📄 Uso

Este projeto foi desenvolvido para fins **educacionais e de aprendizado**.

Sinta-se à vontade para utilizar o projeto como referência nos seus estudos de Python, POO, CRUD, persistência de dados e organização de aplicações.

---

## ⭐ Projeto

Se este projeto foi útil para seus estudos, considere deixar uma ⭐ no repositório.

**Desenvolvido com Python 🐍**
