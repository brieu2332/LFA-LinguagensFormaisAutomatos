
from collections import deque
from automato import AFD, AFN

def afn_para_afd(afn):
   
    mapeamento_estados_afd = {}
    lista_trabalho = deque()
    
    novas_transicoes = {}
    novos_estados_finais = set()
    
    estado_inicial_afd_conjunto = afn._calcular_fecho_epsilon({afn.estado_inicial})
    estado_inicial_afd_conjunto = frozenset(estado_inicial_afd_conjunto) #

    contador_estados = 0
    nome_estado_inicial_afd = f"S{contador_estados}"
    contador_estados += 1
    
    mapeamento_estados_afd[estado_inicial_afd_conjunto] = nome_estado_inicial_afd
    lista_trabalho.append(estado_inicial_afd_conjunto)
    
    while lista_trabalho:
        conjunto_atual_afn = lista_trabalho.popleft()
        nome_estado_atual_afd = mapeamento_estados_afd[conjunto_atual_afn]
        
        for simbolo in afn.alfabeto:
            
            proximos_estados_afn = set()
            for estado_afn in conjunto_atual_afn:
                destinos = afn.transicoes.get((estado_afn, simbolo), set())
                proximos_estados_afn.update(destinos)
            
            fecho_destino = afn._calcular_fecho_epsilon(proximos_estados_afn)
            fecho_destino = frozenset(fecho_destino)

            if not fecho_destino: 
                continue

            if fecho_destino not in mapeamento_estados_afd:
                novo_nome_estado_afd = f"S{contador_estados}"
                contador_estados += 1
                mapeamento_estados_afd[fecho_destino] = novo_nome_estado_afd
                lista_trabalho.append(fecho_destino) 
            
            nome_estado_destino_afd = mapeamento_estados_afd[fecho_destino]
            novas_transicoes[(nome_estado_atual_afd, simbolo)] = nome_estado_destino_afd

    for conjunto_afn, nome_afd in mapeamento_estados_afd.items():
        if not conjunto_afn.isdisjoint(afn.estados_finais):
            novos_estados_finais.add(nome_afd)
            
    novos_estados_afd = set(mapeamento_estados_afd.values())
    
    return AFD(
        estados=novos_estados_afd,
        alfabeto=afn.alfabeto,
        transicoes=novas_transicoes,
        estado_inicial=nome_estado_inicial_afd,
        estados_finais=novos_estados_finais
    )