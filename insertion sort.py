def ordenacaoInsercao(vetor,tamanhoDoVetor):
    for indice in range(1, tamanhoDoVetor)
        atual = vetor[i]
        j = i-1
        while j >= 0 and atual < vetor[j]:
            vetor[1 + j] = vetor[j]
            j -= 1
        vetor[j + 1] = atual
            
