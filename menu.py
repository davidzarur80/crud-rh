from rich import print

def exibir_menu():
    largura = 60
    print("=" * largura)
    print(f"[bold green]{'Sistema de Cadastro de Funcionários'.center(largura)}[/bold green]")
    print("=" * largura)

    print("\n[1] Cadastrar Funcionário")
    print("[2] Visualizar Funcionários")
    print("[3] Consultar Funcionário")
    print("[4] Editar Funcionário")
    print("[5] Excluir Funcionário")
    print("[6] Gerar Funcionários Aleatórios")
    print("[7] Sair\n")
    
    return input("Escolha uma opção: ")