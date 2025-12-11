class AFD:
    def __init__(self, estados, alfabeto, transicoes, estado_inicial, estados_finais):
        self.estados = set(estados)
        self.alfabeto = set(alfabeto)
        self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.estados_finais = set(estados_finais)

    def simular(self, cadeia):
        estado_atual = self.estado_inicial
        
        print(f"\n--- Processando a cadeia: '{cadeia}' ---")
        print(f"Estado inicial: {estado_atual}")

        for simbolo in cadeia:
            if simbolo not in self.alfabeto:
                print(f"ERRO: Símbolo '{simbolo}' não pertence ao alfabeto {self.alfabeto}.")
                return False

            chave_transicao = (estado_atual, simbolo)
            proximo_estado = self.transicoes.get(chave_transicao)

            if proximo_estado is None:
                print(f"ERRO: Transição não definida para o estado '{estado_atual}' com o símbolo '{simbolo}'.")
                return False

            print(f"Lendo '{simbolo}': Estado atual '{estado_atual}' ---> Próximo estado '{proximo_estado}'")
            estado_atual = proximo_estado
        
        print(f"Fim da cadeia. Estado final: '{estado_atual}'")
        
        if estado_atual in self.estados_finais:
            print(f"O estado '{estado_atual}' ESTÁ no conjunto de estados finais {self.estados_finais}.")
            return True
        else:
            print(f"O estado '{estado_atual}' NÃO ESTÁ no conjunto de estados finais {self.estados_finais}.")
            return False

def obter_definicao_afd_interativo():
   
    print("--- Definição do Autômato Finito Determinístico ---")
    
    entrada_estados = input("1. Digite os nomes dos estados, separados por vírgula (ex: q0,q1,q2): ")
    estados = {estado.strip() for estado in entrada_estados.split(',')}
    print(f"   Estados definidos: {estados}")

    entrada_alfabeto = input("2. Digite os símbolos do alfabeto, separados por vírgula (ex: 0,1): ")
    alfabeto = {simbolo.strip() for simbolo in entrada_alfabeto.split(',')}
    print(f"   Alfabeto definido: {alfabeto}")

    while True:
        estado_inicial = input("3. Digite o nome do estado inicial (deve ser um dos estados acima): ").strip()
        if estado_inicial in estados:
            print(f"   Estado inicial definido: {estado_inicial}")
            break
        else:
            print(f"   ERRO: '{estado_inicial}' não é um estado válido. Tente novamente.")

    while True:
        entrada_finais = input("4. Digite os nomes dos estados finais, separados por vírgula: ").strip()
        estados_finais = {estado.strip() for estado in entrada_finais.split(',')}
        if estados_finais.issubset(estados):
            print(f"   Estados finais definidos: {estados_finais}")
            break
        else:
            print(f"   ERRO: Um ou mais estados finais não estão no conjunto de estados. Tente novamente.")

    transicoes = {}
    print("\n5. Defina as transições. Digite no formato 'estado_atual, simbolo -> proximo_estado'")
    print("   Digite 'fim' quando tiver terminado.")
    
    while True:
        entrada_transicao = input("   > ").strip()
        if entrada_transicao.lower() == 'fim':
            break
        
        try:
            parte_esquerda, proximo_estado = [p.strip() for p in entrada_transicao.split('->')]
            estado_atual, simbolo = [p.strip() for p in parte_esquerda.split(',')]

            
            if estado_atual not in estados or proximo_estado not in estados or simbolo not in alfabeto:
                print("   ERRO: Estado ou símbolo inválido. Verifique se eles foram definidos corretamente.")
                continue
            
            transicoes[(estado_atual, simbolo)] = proximo_estado
            print(f"      -> Transição adicionada: δ({estado_atual}, {simbolo}) = {proximo_estado}")

        except ValueError:
            print("   ERRO: Formato inválido. Use 'estado, simbolo -> proximo_estado'.")

    print("\n--- Definição do Autômato Concluída! ---")
    return estados, alfabeto, transicoes, estado_inicial, estados_finais


if __name__ == "__main__":
    
    q, sigma, delta, q0, f = obter_definicao_afd_interativo()
    
    meu_automato = AFD(q, sigma, delta, q0, f)

    print("\n--- Simulação ---")
    while True:
        cadeia_teste = input("Digite uma cadeia para testar (ou 'sair' para terminar): ").strip()
        
        if cadeia_teste.lower() == 'sair':
            print("Encerrando o programa. Até logo!")
            break
        
        resultado = meu_automato.simular(cadeia_teste)
        if resultado:
            print(f"Resultado para '{cadeia_teste}': ACEITA\n")
        else:
            print(f"Resultado para '{cadeia_teste}': REJEITA\n")