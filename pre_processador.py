def expandir_classes(regex):
    saida = ""
    i = 0
    tamanho = len(regex)

    while i < tamanho:
        char = regex[i]

        if char == '[':
            i += 1
            conteudo_interno = ""
            
            while i < tamanho and regex[i] != ']':
                conteudo_interno += regex[i]
                i += 1
            
            lista_caracteres = []
            j = 0
            while j < len(conteudo_interno):
                if j + 2 < len(conteudo_interno) and conteudo_interno[j+1] == '-':
                    inicio = conteudo_interno[j]
                    fim = conteudo_interno[j+2]
                    
                    cod_inicio = ord(inicio)
                    cod_fim = ord(fim)
                    
                    if cod_inicio <= cod_fim:
                        for codigo in range(cod_inicio, cod_fim + 1):
                            lista_caracteres.append(chr(codigo))
                    
                    j += 3
                else:
                    lista_caracteres.append(conteudo_interno[j])
                    j += 1
            
            if lista_caracteres:
                bloco_expandido = "(" + "|".join(lista_caracteres) + ")"
                saida += bloco_expandido
            
        else:
            saida += char
        
        i += 1 #

    return saida