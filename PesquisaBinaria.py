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
