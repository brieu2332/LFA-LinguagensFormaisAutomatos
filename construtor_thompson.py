from automato import AFN
from gerador_estados import GeradorDeEstados
from operacoes.uniao import uniao_afns
from operacoes.concatenacao import concatenacao_afns
from operacoes.estrela import estrela_afn
from pre_processador import expandir_classes

def _adicionar_concatenacao_explicita(regex):
    saida = ''
    for i in range(len(regex)):
        saida += regex[i]
        if i + 1 < len(regex):
            char_atual = regex[i]
            proximo_char = regex[i+1]
            
            if (char_atual.isalnum() or char_atual == '.' or char_atual == ')' or char_atual == '*') and \
               (proximo_char.isalnum() or proximo_char == '.' or proximo_char == '('):
                saida += '~'
    return saida

def _infixa_para_posfixa(regex_com_concat):
    precedencia = {'|': 1, '~': 2, '*': 3}
    posfixa = []
    pilha_operadores = []
    
    for char in regex_com_concat:
        if char.isalnum() or char == '&' or char == '.':
            posfixa.append(char)
        elif char == '(':
            pilha_operadores.append(char)
        elif char == ')':
            while pilha_operadores and pilha_operadores[-1] != '(':
                posfixa.append(pilha_operadores.pop())
            pilha_operadores.pop() 
        elif char in precedencia: 
            while (pilha_operadores and pilha_operadores[-1] != '(' and
                   precedencia.get(pilha_operadores[-1], 0) >= precedencia.get(char, 0)):
                posfixa.append(pilha_operadores.pop())
            pilha_operadores.append(char)

    while pilha_operadores:
        posfixa.append(pilha_operadores.pop())
        
    return "".join(posfixa)

def regex_para_afn(regex):
    regex_expandida = expandir_classes(regex)

    regex_com_concat = _adicionar_concatenacao_explicita(regex_expandida)

    posfixa = _infixa_para_posfixa(regex_com_concat)

    if not posfixa:
        raise ValueError("A expressão não pôde ser processada (posfixa vazia).")

    pilha_afns = []
    gerador = GeradorDeEstados()

    for char in posfixa:
        if char.isalnum() or char == '&' or char == '.':
            q_inicial = gerador.novo_estado()
            q_final = gerador.novo_estado()
         
            nfa = AFN(
                estados={q_inicial, q_final},
                alfabeto={char} if char != '&' else set(),
                transicoes={(q_inicial, char): {q_final}},
                estado_inicial=q_inicial,
                estado_final=q_final
            )
            pilha_afns.append(nfa)
        
        elif char == '|':
            nfa2 = pilha_afns.pop()
            nfa1 = pilha_afns.pop()
            resultado = uniao_afns(nfa1, nfa2, gerador)
            pilha_afns.append(resultado)
        
        elif char == '~':
            nfa2 = pilha_afns.pop()
            nfa1 = pilha_afns.pop()
            resultado = concatenacao_afns(nfa1, nfa2)
            pilha_afns.append(resultado)

        elif char == '*':
            nfa = pilha_afns.pop()
            resultado = estrela_afn(nfa, gerador)
            pilha_afns.append(resultado)
    
    if len(pilha_afns) != 1:
        raise ValueError(f"Pilha final mal formada. Sobraram {len(pilha_afns)} itens.")
        
    return pilha_afns.pop()