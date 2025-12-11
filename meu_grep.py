from automato import AFD
from construtor_thompson import regex_para_afn 
from AFD_para_AFN import afn_para_afd   

def criar_automato_grep(padrao):
    print(f"1. Compilando o padrão '{padrao}' para um autômato de busca...")
    
    regex_busca = f".*({padrao}).*" 
    
    afn_resultante = regex_para_afn(regex_busca)
    
    afd_final = afn_para_afd(afn_resultante)
    
    print("2. Autômato de busca criado com sucesso!")
    return afd_final

def mostrar_conteudo_arquivo(nome_arquivo):
    """
    Lê um arquivo de texto e imprime seu conteúdo completo no console.
    """
    print(f"\n--- Conteúdo do arquivo: '{nome_arquivo}' ---")
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            print(f.read())
        print("------------------------------------------")
    except FileNotFoundError:
        print(f"ERRO: O arquivo '{nome_arquivo}' não foi encontrado.")
        print("------------------------------------------")
    except Exception as e:
        print(f"ERRO ao ler o arquivo: {e}")
        print("------------------------------------------")


if __name__ == "__main__":
    
    padrão_usuario = input("Digite o padrão (Expressão Regular) a ser procurado: ")
    arquivo_alvo = input("Digite o nome do arquivo de texto para vasculhar: ")

    automato_de_busca = criar_automato_grep(padrão_usuario)

    print(f"\n--- Procurando por '{padrão_usuario}' em '{arquivo_alvo}' ---")
    
    try:
        with open(arquivo_alvo, 'r', encoding='utf-8') as f:
            ocorrencias_encontradas = 0
            for num_linha, linha in enumerate(f, 1):
                if automato_de_busca.simular(linha.strip()):
                    print(f"Linha {num_linha}: {linha.strip()}")
                    ocorrencias_encontradas += 1
            
            if ocorrencias_encontradas == 0:
                print("\nNenhuma ocorrência do padrão foi encontrada.")
    
    except FileNotFoundError:
        print(f"ERRO: O arquivo '{arquivo_alvo}' não foi encontrado.")