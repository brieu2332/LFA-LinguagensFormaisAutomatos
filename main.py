import sys
import time
from meu_grep import executar_grep

def limpar_tela():
    print("\n" * 5)

def menu_principal():
    while True:
        limpar_tela()
        print("========================================")
        print("   SISTEMA DE AUTÔMATOS (Projeto LFA)")
        print("========================================")
        print("1. Iniciar Busca (Meu Grep)")
        print("0. Sair")
        print("========================================")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            executar_grep()
            input("\nPressione ENTER para voltar ao menu...")
            
        elif opcao == '0':
            print("\nEncerrando o sistema...")
            time.sleep(1)
            print("Até logo!")
            sys.exit()
            
        else:
            print("\nOpção inválida! Tente novamente.")
            time.sleep(1)

if __name__ == "__main__":
    try:
        menu_principal()
    except KeyboardInterrupt:
        print("\n\nExecução interrompida forçadamente.")