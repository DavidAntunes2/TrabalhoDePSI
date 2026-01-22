# Cria uma lista vazia para guardar as notas
notas = []

# Ciclo infinito para permitir inserir quantas notas quiser
while True:
    # Pede ao utilizador que insira uma nota ou a palavra 'fim'
    entrada = input("Insira uma ou mais notas (ou digite 'fim' para terminar e saber a nota mais alta, a mais baixa e a média.): ")

    # Verifica se o utilizador escreveu 'fim'
    if entrada.lower() == "fim":
        break  # Sai do ciclo

    # Converte a entrada para número decimal
    nota = float(entrada)

    # Adiciona a nota à lista
    notas.append(nota)

# Verifica se pelo menos uma nota foi inserida
if len(notas) > 0:
    # Calcula a nota mais alta
    nota_mais_alta = max(notas)

    # Calcula a nota mais baixa
    nota_mais_baixa = min(notas)

    # Calcula a média das notas
    media = sum(notas) / len(notas)

    # Mostra os resultados no ecrã
    print("Nota mais alta:", nota_mais_alta)
    print("Nota mais baixa:", nota_mais_baixa)
    print("Média:", media)
else:
    # Mensagem caso nenhuma nota tenha sido inserida
    print("Não foram inseridas notas.")


