class AFD:
    def __init__(self, estados, alfabeto, transicoes, estado_inicial, estados_finais):
        self.estados = set(estados)
        self.alfabeto = set(alfabeto)
        self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.estados_finais = set(estados_finais)

    def simular(self, cadeia):
        estado_atual = self.estado_inicial
        for simbolo in cadeia:
            if (estado_atual, simbolo) in self.transicoes:
                proximo_estado = self.transicoes.get((estado_atual, simbolo))
            elif (estado_atual, '.') in self.transicoes:
                proximo_estado = self.transicoes.get((estado_atual, '.'))
            else:
                proximo_estado = None 

            if proximo_estado is None: 
                
                proximo_estado = self.transicoes.get((estado_atual, '.'))
                if proximo_estado is None:
                    proximo_estado = self.transicoes.get((estado_atual, simbolo))
                    if proximo_estado is None:
                        
                         proximo_estado = self.transicoes.get((estado_atual, simbolo)) 
                         if proximo_estado is None:
                             proximo_estado = self.transicoes.get((estado_atual, '.')) 
                         
                         if proximo_estado is None:
                             return False 
            
            estado_atual = proximo_estado
        return estado_atual in self.estados_finais

    def __repr__(self):
        return (f"--- AFD ---\n"
                f"Q = {self.estados}\n"
                f"Σ = {self.alfabeto}\n"
                f"δ = {self.transicoes}\n"
                f"q₀ = {self.estado_inicial}\n"
                f"F = {self.estados_finais}\n"
                f"----------")

class AFD:
    def __init__(self, estados, alfabeto, transicoes, estado_inicial, estados_finais):
        self.estados = set(estados)
        self.alfabeto = set(alfabeto)
        self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.estados_finais = set(estados_finais)

    def simular(self, cadeia):
        estado_atual = self.estado_inicial
        for simbolo in cadeia:
             proximo_estado = self.transicoes.get((estado_atual, simbolo)) 
             if proximo_estado is None:
                 proximo_estado = self.transicoes.get((estado_atual, '.')) 
             
             if proximo_estado is None:
                 return False 
            
             estado_atual = proximo_estado
        return estado_atual in self.estados_finais

    def __repr__(self):
        return (f"--- AFD ---\n"
                f"Q = {self.estados}\n"
                f"Σ = {self.alfabeto}\n"
                f"δ = {self.transicoes}\n"
                f"q₀ = {self.estado_inicial}\n"
                f"F = {self.estados_finais}\n"
                f"----------")

class AFN:
  
    def __init__(self, estados, alfabeto, transicoes, estado_inicial, *, estado_final=None, estados_finais=None):
        self.estados = set(estados)
        self.alfabeto = set(alfabeto)
        self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.estado_final = estado_final 
        
        if estados_finais:
            self.estados_finais = set(estados_finais)
        elif estado_final:
            self.estados_finais = {estado_final} 
        else:
            self.estados_finais = set() 

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
        
        for simbolo in cadeia:
            proximos_estados_sem_fecho = set()
            for estado in estados_atuais:
                destinos = self.transicoes.get((estado, simbolo), set())
                proximos_estados_sem_fecho.update(destinos)
                destinos_wildcard = self.transicoes.get((estado, '.'), set())
                proximos_estados_sem_fecho.update(destinos_wildcard)
            
            estados_atuais = self._calcular_fecho_epsilon(proximos_estados_sem_fecho)
        
        return not estados_atuais.joint(self.estados_finais)

    def __repr__(self):
        return (f"--- AFN ---\n"
                f"Q = {self.estados}\n"
                f"Σ = {self.alfabeto}\n"
                f"δ = {self.transicoes}\n"
                f"q₀ = {self.estado_inicial}\n"
                f"F = {self.estados_finais}\n" 
                f"----------")