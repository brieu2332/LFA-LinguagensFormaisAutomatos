# main.py

from construtor_thompson import regex_para_afn
from conversor_afn_afd import afn_para_afd 

if __name__ == "__main__":
    
    print("--- Conversor de Expressão Regular para Autômato ---")
    
    try:
        # Pede a entrada do usuário
        expressao = input("Digite uma Expressão Regular (ex: (a|b)*a): ")
        
        # --- FASE 1: ER -> AFN ---
        print("\n1. Convertendo Expressão Regular para AFN (Construção de Thompson)...")
        afn_gerado = regex_para_afn(expressao)
        
        print("\n--- AFN Resultante ---")
        print(afn_gerado)
        
        # --- FASE 2: AFN -> AFD ---
        print("\n\n2. Convertendo AFN para AFD (Construção de Subconjuntos)...")
        afd_final = afn_para_afd(afn_gerado)
        
        print("\n--- AFD Final Gerado ---")
        print(afd_final)
        
        print("\n\n--- O pipeline completo foi executado com sucesso! ---")
        # A partir daqui, você poderia usar o 'afd_final' no seu simulador.
        
    except (ValueError, IndexError) as e:
        print(f"\nERRO: A expressão regular parece ser inválida. ({e})")
    except KeyboardInterrupt:
        print("\nOperação cancelada pelo usuário.")