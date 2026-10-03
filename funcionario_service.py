from datetime import datetime
from utils.helpers import normalizar_texto

SALARIO_MINIMO = 1621.00

def _ler_salario(mensagem="Salário: R$ "):
    while True:
        entrada = input(mensagem).strip()

        try:
            if "," in entrada:
                entrada = entrada.replace(".", "").replace(",", ".")
            elif entrada.count(".") > 1:
                entrada = entrada.replace(".", "")

            salario = float(entrada)

            if salario < SALARIO_MINIMO:
                print(f"O salário não pode ser menor que R$ {SALARIO_MINIMO:.2f}.")
                continue

            return round(salario, 2)

        except ValueError:
            print("Salário inválido. Digite um valor numérico.")

def _ler_data(mensagem):
    while True:
        entrada = input(mensagem).strip()

        try:
            return datetime.strptime(entrada, "%d/%m/%Y").date()
        except ValueError:
            print("Data inválida. Use o formato dd/mm/aaaa.")

def cadastrar(funcionarios, funcionario_cls):
    nome = input("\nNome: ").strip().upper()
    filial = input("Filial (Cidade/UF): ").strip().upper()
    departamento = input("Departamento: ").strip().upper()
    cargo = input("Cargo: ").strip().upper()
    salario = _ler_salario()
    data_admissao = _ler_data("Data de admissão (dd/mm/aaaa): ")

    funcionario = funcionario_cls(nome, filial, departamento, cargo, salario, data_admissao)
    funcionarios.append(funcionario)
    return funcionario

def buscar_por_chapa(funcionarios, chapa):
    for funcionario in funcionarios:
        if funcionario.chapa == chapa:
            return funcionario

    return None

def buscar_por_nome(funcionarios, nome):
    nome_normalizado = normalizar_texto(nome)

    return [
        funcionario
        for funcionario in funcionarios
        if nome_normalizado in normalizar_texto(funcionario.nome)
    ]

def buscar_por_filial(funcionarios, filial):
    filial_normalizada = normalizar_texto(filial)

    return [
        funcionario
        for funcionario in funcionarios
        if filial_normalizada in normalizar_texto(funcionario.filial)
    ]

def buscar_por_departamento(funcionarios, departamento):
    departamento_normalizado = normalizar_texto(departamento)

    return [
        funcionario
        for funcionario in funcionarios
        if departamento_normalizado
        in normalizar_texto(funcionario.departamento)
    ]

def editar(funcionarios, chapa):
    funcionario = buscar_por_chapa(funcionarios, chapa)

    if funcionario is None:
        return None

    print("\nDeixe vazio para manter o valor atual.\n")

    nome = input(f"Nome [{funcionario.nome}]: ").strip().upper()
    filial = input(f"Filial [{funcionario.filial}]: ").strip().upper()
    departamento = input(f"Departamento [{funcionario.departamento}]: ").strip().upper()
    cargo = input(f"Cargo [{funcionario.cargo}]: ").strip().upper()

    while True:
        entrada_salario = input(f"Salário [{funcionario.salario:.2f}]: ").strip()
        
        if not entrada_salario:
            break

        try:
            if "," in entrada_salario:
                entrada_salario = (entrada_salario.replace(".", "").replace(",", "."))
            elif entrada_salario.count(".") > 1:
                entrada_salario = entrada_salario.replace(".", "")

            novo_salario = round(float(entrada_salario), 2)

            if novo_salario < SALARIO_MINIMO:
                print(f"O salário não pode ser menor que R$ {SALARIO_MINIMO:.2f}.")
                continue
            
            if novo_salario < funcionario.salario:
                print(f"O salário não pode ser menor que R$ {funcionario.salario:.2f}.")
                continue

            funcionario.salario = novo_salario
            break

        except ValueError:
            print("Salário inválido. Digite um valor numérico.")

    data_atual = funcionario.data_admissao.strftime("%d/%m/%Y")
    entrada_data = input(f"Data de admissão [{data_atual}]: ").strip()

    if nome:
        funcionario.nome = nome

    if filial:
        funcionario.filial = filial

    if departamento:
        funcionario.departamento = departamento

    if cargo:
        funcionario.cargo = cargo

    if entrada_data:
        try:
            funcionario.data_admissao = datetime.strptime(entrada_data, "%d/%m/%Y",).date()
        except ValueError:
            print("Data inválida. A data de admissão anterior foi mantida.")

    return funcionario

def excluir(funcionarios, chapa):
    funcionario = buscar_por_chapa(funcionarios, chapa)

    if funcionario is None:
        return None

    funcionarios.remove(funcionario)
    return funcionario