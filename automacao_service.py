from datetime import date
import random
from faker import Faker

fake = Faker("pt_BR")
SALARIO_MINIMO = 1621.00

SUPERINTENDENCIA = [
"SUPERINTENDÊNCIA DE GESTÃO DE PESSOAS",
"SUPERINTENDÊNCIA GERAL",
"SUPERINTENDÊNCIA ADMINISTRATIVA",
"SUPERINTENDÊNCIA FINANCEIRA",
"SUPERINTENDÊNCIA CAPTAÇÃO DE RECURSOS",
"SUPERINTENDÊNCIA DE CAPTAÇÃO DE RECURSOS",
"SUPERINTENDÊNCIA DE ENGENHARIA DA COMUNICAÇÃO",
"SUPERINTENDÊNCIA SOCIAL",
"SUPERINTENDÊNCIA EDUCACIONAL",
"SUPERINTENDÊNCIA ASSESSORAMENTO",
"SUPERINTENDÊNCIA TECNOLOGIA DA INFORMAÇÃO",
"SUPERINTENDÊNCIA DE COMUNICAÇÃO",
"SUPERINTENDÊNCIA MARKETING E COMUNICAÇÃO"
]

def gerar_funcionario(funcionario_cls, chapas_usadas):
    while True:
        chapa = random.randint(100000000, 999999999)

        if chapa not in chapas_usadas:
            chapas_usadas.add(chapa)
            break

    nome = fake.name().upper()
    filial = f"{fake.city().upper()}/{fake.state_abbr().upper()}"
    departamento = random.choice(SUPERINTENDENCIA)
    cargo = fake.job().upper()
    salario = round(random.uniform(SALARIO_MINIMO, 20000.00), 2)
    data_admissao = fake.date_between(start_date="-20y", end_date="today",)
    funcionario = funcionario_cls(nome, filial, departamento, cargo, salario, data_admissao,)

    funcionario.chapa = chapa
    return funcionario

def gerar_funcionarios(funcionarios, funcionario_cls, quantidade=30):
    novos = []

    chapas_usadas = {funcionario.chapa for funcionario in funcionarios}

    for _ in range(quantidade):
        funcionario = gerar_funcionario(funcionario_cls, chapas_usadas,)
        funcionarios.append(funcionario)
        novos.append(funcionario)

    return novos