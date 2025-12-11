# operacoes/estrela.py

from automato import AFN

def estrela_afn(nfa, gerador_estados):
    """
    Cria um novo AFN que representa o Fecho de Kleene (estrela) de um AFN.
    """
    novo_inicial = gerador_estados.novo_estado()
    novo_final = gerador_estados.novo_estado()
    novos_estados = nfa.estados.union({novo_inicial, novo_final})
    
    novas_transicoes = nfa.transicoes.copy()
    novas_transicoes[(novo_inicial, '&')] = {nfa.estado_inicial, novo_final}
    novas_transicoes[(nfa.estado_final, '&')] = {nfa.estado_inicial, novo_final}

    return AFN(novos_estados, nfa.alfabeto, novas_transicoes, novo_inicial, estado_final=novo_final)
