from rich import print
from rich.box import DOUBLE
from rich.panel import Panel
from rich.traceback import install
from models.funcionario import Funcionario
from services.arquivo_service import (carregar_funcionarios, salvar_funcionarios,)
from services.automacao_service import gerar_funcionarios
from services.funcionario_service import (buscar_por_chapa, buscar_por_filial, buscar_por_nome, buscar_por_departamento, cadastrar, editar, excluir,)
from utils.helpers import limpar_tela
from views.menu import exibir_menu
install()

def pausar():
    input("\nPressione ENTER...")

def ler_chapa():
    while True:
        entrada = input("\nDigite a chapa: ").strip()

        try:
            return int(entrada)
        except ValueError:
            print("\n[red]Digite uma chapa numérica válida.[/red]")

def visualizar_funcionarios(funcionarios):
    if not funcionarios:
        print("\n[red]Nenhum funcionário cadastrado.[/red]")
    else:
        for funcionario in funcionarios:
            painel = Panel.fit(
                funcionario.exibir_dados(),
                title="📋 Dados do Funcionário",
                border_style="bright_blue",
                box=DOUBLE,
            )

            print()
            print(painel)

    pausar()

def consultar_funcionarios(funcionarios):
    print("\n[1] Consultar por Chapa")
    print("[2] Consultar por Nome")
    print("[3] Consultar por Filial")
    print("[4] Consultar por Departamento")

    tipo = input("\nEscolha uma opção: ").strip()
    resultados = []

    if tipo == "1":
        chapa = ler_chapa()
        funcionario = buscar_por_chapa(funcionarios, chapa)

        if funcionario:
            resultados.append(funcionario)

    elif tipo == "2":
        nome = input("\nDigite o nome: ")
        resultados = buscar_por_nome(funcionarios, nome)

    elif tipo == "3":
        filial = input("\nDigite a filial: ")
        resultados = buscar_por_filial(funcionarios, filial)

    elif tipo == "4":
        departamento = input("\nDigite o departamento: ")
        resultados = buscar_por_departamento(
            funcionarios,
            departamento
        )

    else:
        print("\n[red]Opção inválida.[/red]")
        pausar()
        return

    if resultados:
        for funcionario in resultados:
            painel = Panel.fit(
                funcionario.exibir_dados(),
                title="🔍 Funcionário Encontrado",
                border_style="green",
                box=DOUBLE,
            )

            print()
            print(painel)
    else:
        print("\n[red]Nenhum funcionário encontrado.[/red]")

    pausar()


def main():
    funcionarios = carregar_funcionarios(Funcionario)

    while True:
        limpar_tela()
        opcao = exibir_menu()

        if opcao == "1":
            funcionario = cadastrar(funcionarios, Funcionario)
            salvar_funcionarios(funcionarios)

            print("\n[green]✅ Funcionário cadastrado com sucesso![/green]")
            print(f"Chapa gerada: {funcionario.chapa:010d}")
            pausar()

        elif opcao == "2":
            visualizar_funcionarios(funcionarios)

        elif opcao == "3":
            consultar_funcionarios(funcionarios)

        elif opcao == "4":
            chapa = ler_chapa()
            funcionario = editar(funcionarios, chapa)

            if funcionario:
                salvar_funcionarios(funcionarios)
                print("\n[green]✅ Funcionário atualizado![/green]")
            else:
                print("\n[red]❌ Chapa não encontrada![/red]")

            pausar()

        elif opcao == "5":
            chapa = ler_chapa()
            funcionario = excluir(funcionarios, chapa)

            if funcionario:
                salvar_funcionarios(funcionarios)
                print(
                    f"\n[green]✅ Funcionário "
                    f"{funcionario.nome} excluído![/green]"
                )
            else:
                print("\n[red]❌ Chapa não encontrada![/red]")

            pausar()

        elif opcao == "6":
            novos = gerar_funcionarios(funcionarios, Funcionario)
            salvar_funcionarios(funcionarios)

            print(f"\n[green]✅ {len(novos)} funcionários gerados com sucesso![/green]")
            pausar()

        elif opcao == "7":
            print("\n[green]✅ Sistema encerrado![/green]")
            break
        
        else:
            print("\n[red]❌ Opção inválida![/red]")
            pausar()

if __name__ == "__main__":
    main()