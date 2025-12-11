# Loop principal
while True:
    print("\n----- LFA - Linguagens Formais e Autômatos -----")
    print("Escolha qual operação você deseja fazer:")
    
    escolha = input("1- Soma de autômatos\n"
                    "2- Produto de autômatos\n"
                    "3- Complemento de autômato\n"
                    "4- Interseção de autômatos\n"
                    "5- União de autômatos\n"
                    "0- Sair\n"
                    "Sua escolha: ")

    match escolha:
        case '1':
            print("Encerrando o programa. Até logo!")
            #soma_automatos()
        case '2':
            print("Encerrando o programa. Até logo!")
            #produto_automatos()
        case '3':
            print("Encerrando o programa. Até logo!")
            #complemento_automato()
        case '4':
            print("Encerrando o programa. Até logo!")
            #intersecao_automatos()
        case '5':
            print("Encerrando o programa. Até logo!")
            #uniao_automatos()
        case '0':
            print("Encerrando o programa. Até logo!")
            break
        case _:  # O '_' é o caso padrão, para qualquer outra entrada
            print("\n[ERRO] Opção inválida. Por favor, escolha um número do menu.")
    
    if escolha == '0':
        break