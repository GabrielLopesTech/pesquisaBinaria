def pesquisa_binaria(lista, valor):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2  
        chute = lista[meio]

        if chute == valor:
            return meio  
        if chute > valor:
            fim = meio - 1  
        else:
            inicio = meio + 1  

    return -1  # Retorna -1 se não encontrou

numeros = [1, 3, 5, 7, 9, 11, 13, 15]

print(pesquisa_binaria(numeros, 7))   # Saída: 3 (índice do número 7)
print(pesquisa_binaria(numeros, 2))   # Saída: -1 (não existe na lista)

# Versão do livro "Entendendo Algoritmos"

# def pesquisa_binaria(lista, item):
#     baixo = 0
#     alto = len(lista) - 1

#     while baixo <= alto:
#         meio = (baixo + alto) // 2
#         chute = lista[meio]

#         if chute == item:
#             return meio
#         if chute > item:
#             alto = meio - 1
#         else:
#             baixo = meio + 1

#     return None

# numeros = [1, 3, 5, 7, 9, 11, 13, 15]

# print(pesquisa_binaria(numeros, 7))   # Saída: 3 (índice do número 7)
# print(pesquisa_binaria(numeros, 2))   # Saída: -1 (não existe na lista)

# ordenacaoPorSelecao

def encontra_menor_indice(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

def ordenacao_por_selecao(arr):
    novo_arr = []
    for i in range(len(arr)):
        menor = encontra_menor_indice(arr)
        novo_arr.append(arr.pop(menor))
    return novo_arr

# Exemplo
print(ordenacao_por_selecao([5, 3, 6, 2, 10]))  
# saída: [2, 3, 5, 6, 10]


# Encontrar o maior número em uma lista

def maior_numero(lista):
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num
    return maior

# Exemplo
print(maior_numero([3, 7, 2, 9, 5]))  # saída: 9




