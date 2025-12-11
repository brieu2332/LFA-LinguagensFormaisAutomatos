# operacoes/concatenacao.py

from automato import AFN

def concatenacao_afns(nfa1, nfa2):
    novos_estados = nfa1.estados.union(nfa2.estados)
    novo_alfabeto = nfa1.alfabeto.union(nfa2.alfabeto)
    
    novas_transicoes = nfa1.transicoes.copy()
    novas_transicoes.update(nfa2.transicoes)
    
    novas_transicoes[(nfa1.estado_final, '&')] = {nfa2.estado_inicial}

    return AFN(novos_estados, novo_alfabeto, novas_transicoes, nfa1.estado_inicial, estado_final=nfa2.estado_final)
