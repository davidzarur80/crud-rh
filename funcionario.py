from datetime import datetime
from dateutil.relativedelta import relativedelta

class Funcionario:
    contador_chapa = 100112700

    def __init__(self, nome, filial, departamento, cargo, salario, data_admissao):
        self.chapa = Funcionario.contador_chapa
        Funcionario.contador_chapa += 1

        self.nome = nome
        self.filial = filial
        self.departamento = departamento
        self.cargo = cargo
        self.salario = salario
        self.data_admissao = data_admissao

    def calcular_tempo_casa(self):
        hoje = datetime.now().date()
        diferenca = relativedelta(hoje, self.data_admissao)
        return (diferenca.years, diferenca.months, diferenca.days)

    def exibir_dados(self):
        anos, meses, dias = self.calcular_tempo_casa()
        salario_formatado = (f"R$ {self.salario:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

        return f"""
Chapa...........: {self.chapa:010d}
Nome............: {self.nome}
Filial..........: {self.filial}
Departamento....: {self.departamento}
Cargo...........: {self.cargo}
Salário.........: {salario_formatado}
Data Admissão...: {self.data_admissao.strftime('%d/%m/%Y')}
Tempo de Casa...: {anos} ano(s), {meses} mês(es) e {dias} dia(s)
"""

    def to_dict(self):
        return {
            "chapa": self.chapa,
            "nome": self.nome,
            "filial": self.filial,
            "departamento": self.departamento,
            "cargo": self.cargo,
            "salario": self.salario,
            "data_admissao": self.data_admissao.strftime("%d/%m/%Y")
        }

    @classmethod
    def from_dict(cls, dados):
        funcionario = cls(
            dados["nome"],
            dados["filial"],
            dados["departamento"],
            dados["cargo"],
            float(dados["salario"]),
            datetime.strptime(dados["data_admissao"], "%d/%m/%Y").date()
        )

        funcionario.chapa = int(dados["chapa"])
        return funcionario