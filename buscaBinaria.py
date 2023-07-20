def busca_binaria(valor, sequencia):
    inicio = 0
    fim = len(sequencia) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if valor == sequencia[meio]:
            return meio
        elif valor < sequencia[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1
    return None         
       