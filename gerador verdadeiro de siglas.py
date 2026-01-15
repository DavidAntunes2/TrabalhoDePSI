# ==============================
#        Mini projeto 1
# ==============================

# Lista de palavras que normalmente não entram em siglas
palavras_ignoradas = ["de", "da", "do", "dos", "das", "e", "em", "para", "com"]


# ------------------------------
# Função para limpar e preparar a frase
# ------------------------------
def preparar_frase(frase):
    frase = frase.strip().lower()  # Remove espaços e passa para minúsculas
    palavras = frase.split()  # Divide a frase em palavras

    # Remove palavras irrelevantes
    palavras_filtradas = []
    for palavra in palavras:
        if palavra not in palavras_ignoradas:
            palavras_filtradas.append(palavra)

    return palavras_filtradas


# ------------------------------
# Função para gerar a sigla simples
# ------------------------------
def gerar_sigla_simples(palavras):
    sigla = ""
    for palavra in palavras:
        sigla += palavra[0].upper()  # Primeira letra de cada palavra
    return sigla


# ------------------------------
# Função para gerar sigla com número
# ------------------------------
def gerar_sigla_com_numero(sigla):
    tamanho = len(sigla)
    return sigla + str(tamanho)


# ------------------------------
# Função para gerar sigla tipo password
# ------------------------------
def gerar_sigla_password(palavras):
    especiais = ["@", "#", "!", "$"]
    sigla = ""

    for i in range(len(palavras)):
        letra = palavras[i][0].upper()
        sigla += letra

        # Adiciona um carácter especial intercalado
        if i < len(especiais):
            sigla += especiais[i]

    return sigla


# ==============================
#       Programa principal
# ==============================
print("=========================")
print("=== GERADOR DE SIGLAS ===")
print("=========================")
frase_utilizador = input("Escreve uma frase: ")

# Verifica se o utilizador escreveu algo
if frase_utilizador == "":
    print("Erro: Não escreveste nenhuma frase.")
else:
    palavras_tratadas = preparar_frase(frase_utilizador)

    if len(palavras_tratadas) == 0:
        print("Erro: A frase só contém palavras ignoradas.")
    else:
        sigla_simples = gerar_sigla_simples(palavras_tratadas)
        sigla_numero = gerar_sigla_com_numero(sigla_simples)
        sigla_password = gerar_sigla_password(palavras_tratadas)

        print("\nResultados:")
        print("Sigla simples:", sigla_simples)
        print("Sigla com número:", sigla_numero)
        print("Sigla tipo password:", sigla_password)


