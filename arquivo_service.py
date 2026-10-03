from datetime import date, datetime
import json
from pathlib import Path

CAMINHO_JSON = Path(__file__).resolve().parent.parent / "funcionarios.json"

def _funcionario_para_dict(funcionario):
    data_admissao = funcionario.data_admissao

    if isinstance(data_admissao, (date, datetime)):
        data_admissao = data_admissao.isoformat()

    return {
        "chapa": funcionario.chapa,
        "nome": funcionario.nome,
        "filial": funcionario.filial,
        "departamento": funcionario.departamento,
        "cargo": funcionario.cargo,
        "salario": funcionario.salario,
        "data_admissao": data_admissao,
    }

def salvar_funcionarios(funcionarios):
        dados = [
        _funcionario_para_dict(funcionario)
        for funcionario in funcionarios
    ]

        with CAMINHO_JSON.open("w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4,)

def _converter_data(valor):
    if isinstance(valor, date):
        return valor

    if not valor:
        return None

    try:
        return date.fromisoformat(valor)
    except ValueError:
        return datetime.strptime(valor, "%d/%m/%Y").date()

def carregar_funcionarios(Funcionario):
    if not CAMINHO_JSON.exists():
        return []

    try:
        with CAMINHO_JSON.open("r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    except json.JSONDecodeError:
        print("Aviso: o arquivo funcionarios.json está inválido ou vazio.")
        return []

    funcionarios = []

    for item in dados:
        try:
            funcionario = Funcionario(
                item["nome"],
                item["filial"],
                item["departamento"],
                item["cargo"],
                float(item["salario"]),
                _converter_data(item["data_admissao"]),
            )

            funcionario.chapa = int(item["chapa"])
            funcionarios.append(funcionario)

        except (KeyError, TypeError, ValueError) as erro:
            print(f"Aviso: funcionário ignorado por dados inválidos: {erro}")

    return funcionarios