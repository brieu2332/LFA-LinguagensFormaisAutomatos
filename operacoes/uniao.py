# operacoes/uniao.py

from automato import AFN

def uniao_afns(nfa1, nfa2, gerador_estados):
    
    novo_inicial = gerador_estados.novo_estado()
    novo_final = gerador_estados.novo_estado()

    novos_estados = nfa1.estados.union(nfa2.estados).union({novo_inicial, novo_final})
    novo_alfabeto = nfa1.alfabeto.union(nfa2.alfabeto)

    novas_transicoes = nfa1.transicoes.copy()
    novas_transicoes.update(nfa2.transicoes)
    
    novas_transicoes[(novo_inicial, '&')] = {nfa1.estado_inicial, nfa2.estado_inicial}
    novas_transicoes[(nfa1.estado_final, '&')] = {novo_final}
    novas_transicoes[(nfa2.estado_final, '&')] = {novo_final}

    return AFN(novos_estados, novo_alfabeto, novas_transicoes, novo_inicial, estado_final=novo_final)
