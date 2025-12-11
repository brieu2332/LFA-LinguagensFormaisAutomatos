class AFN:
  
    def __init__(self, estados, alfabeto, transicoes, estado_inicial, estados_finais):
        self.estados = set(estados)
        self.alfabeto = set(alfabeto)
        self.transicoes = transicoes  
        self.estado_inicial = estado_inicial
        self.estados_finais = set(estados_finais)

    def _calcular_fecho_epsilon(self, estados_a_verificar):
        pilha = list(estados_a_verificar)
        fecho = set(estados_a_verificar)

        while pilha:
            estado = pilha.pop()
            destinos_epsilon = self.transicoes.get((estado, '&'), set())
            
            for destino in destinos_epsilon:
                if destino not in fecho:
                    fecho.add(destino)
                    pilha.append(destino)
        return fecho

    def simular(self, cadeia):
        estados_atuais = self._calcular_fecho_epsilon({self.estado_inicial})
        
        print(f"\n--- Processando a cadeia: '{cadeia}' ---")
        print(f"Estados iniciais (com fecho-ε): {estados_atuais}")

        for simbolo in cadeia:
            if simbolo not in self.alfabeto:
                print(f"ERRO: Símbolo '{simbolo}' não pertence ao alfabeto {self.alfabeto}.")
                return False

            proximos_estados_sem_fecho = set()
            for estado in estados_atuais:
                destinos = self.transicoes.get((estado, simbolo), set())
                proximos_estados_sem_fecho.update(destinos)
            
            estados_atuais = self._calcular_fecho_epsilon(proximos_estados_sem_fecho)
            
            print(f"Lendo '{simbolo}': Possíveis estados atuais: {estados_atuais}")
        
        print(f"Fim da cadeia. Conjunto de estados finais possíveis: {estados_atuais}")
        
        if not estados_atuais.isdisjoint(self.estados_finais):
            print(f"Pelo menos um estado final ({estados_atuais.intersection(self.estados_finais)}) foi alcançado.")
            return True
        else:
            print(f"Nenhum estado final foi alcançado.")
            return False

def obter_definicao_afn_interativo():
    
    print("--- Definição do Autômato Finito Não Determinístico ---")
    
    estados = {e.strip() for e in input("1. Estados (separados por vírgula): ").split(',')}
    print(f"   Estados definidos: {estados}")

    alfabeto = {s.strip() for s in input("2. Alfabeto (separados por vírgula): ").split(',')}
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
    print("\n5. Defina as transições. Use '&' para transição vazia (épsilon).")
    print("   Formato: 'estado_origem, simbolo -> estado1_destino, estado2_destino, ...'")
    print("   Digite 'fim' quando tiver terminado.")
    
    while True:
        entrada = input("   > ").strip()
        if entrada.lower() == 'fim':
            break
        
        try:
            parte_esquerda, parte_direita = [p.strip() for p in entrada.split('->')]
            estado_origem, simbolo = [p.strip() for p in parte_esquerda.split(',')]
            estados_destino = {e.strip() for e in parte_direita.split(',')}

            if estado_origem not in estados or not estados_destino.issubset(estados) or \
               (simbolo != '&' and simbolo not in alfabeto):
                print("   ERRO: Estado ou símbolo inválido na transição.")
                continue
            
            chave = (estado_origem, simbolo)
            if chave not in transicoes:
                transicoes[chave] = set()
            transicoes[chave].update(estados_destino)
            print(f"      -> Transição adicionada: δ({estado_origem}, {simbolo}) = {transicoes[chave]}")

        except ValueError:
            print("   ERRO: Formato inválido.")

    print("\n--- Definição do Autômato Concluída! ---")
    return estados, alfabeto, transicoes, estado_inicial, estados_finais


if __name__ == "__main__":
    q, sigma, delta, q0, f = obter_definicao_afn_interativo()
    meu_automato = AFN(q, sigma, delta, q0, f)

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