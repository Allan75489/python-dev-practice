def bubble_sort(lista):
    n = len(lista)
    
    # Loop para passar por todos os elementos da lista
    for i in range(n):
        # Variável para rastrear se houve troca nesta passagem
        houve_troca = False
        
        # Os últimos 'i' elementos já estão no lugar certo, não precisamos checar
        for j in range(0, n - i - 1):
            
            # Compara elementos vizinhos
            if lista[j] > lista[j + 1]:
                # Troca os elementos de posição
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                houve_troca = True
                
        # Se nenhuma troca aconteceu, a lista já está ordenada
        if not houve_troca:
            break
            
    return lista

# Exemplo de uso:
numeros = [64, 34, 25, 12, 22, 11, 90]
lista_ordenada = bubble_sort(numeros)
print("Lista ordenada:", lista_ordenada)
