# ======================
# Importações
# ======================
import pygame  # Biblioteca para criar jogos 2D em Python
import random  # Biblioteca para gerar números/frases aleatórias
import sys     # Biblioteca para encerrar o programa corretamente

# ======================
# Inicialização
# ======================
pygame.init()  # Inicializa todos os módulos do Pygame (tela, som, teclado, etc.)

# ======================
# Configurações da tela
# ======================
LARGURA, ALTURA = 800, 500  # Define largura e altura da janela
TELA = pygame.display.set_mode((LARGURA, ALTURA))  # Cria a janela do jogo
pygame.display.set_caption("Desafio das Siglas")  # Define título da janela

# ======================
# Cores
# ======================
BRANCO = (255, 255, 255)         # Cor de fundo da tela
PRETO = (0, 0, 0)                 # Cor padrão de texto
AZUL = (50, 100, 200)             # Azul usado em títulos e sigla parcial
VERDE = (50, 200, 100)            # Verde usado para acertos
VERMELHO = (200, 50, 50)          # Vermelho usado para erros

# ======================
# Fonte
# ======================
FONTE = pygame.font.SysFont(None, 36)  # Fonte padrão com tamanho 36 px

# ======================
# Palavras ignoradas e frases
# ======================
palavras_ignoradas = ["de", "da", "do", "dos", "das", "e", "em", "para", "com"]  # Palavras que não entram na sigla
frases = [
    "Instituto Federal de Tecnologia",  # Lista de frases possíveis no jogo
    "Universidade de Coimbra",
    "Centro de Estudos Avançados",
    "Faculdade de Ciencias e Tecnologia",
    "Instituto Superior Técnico",
    "Escola Nacional de Música"
]

# ======================
# Variáveis do jogo
# ======================
frases_disponiveis = frases.copy()  # Copia todas as frases para uso sem repetir
frase_atual = ""                     # Frase da rodada atual
sigla_correta = ""                   # Sigla correta da rodada atual
resposta = ""                        # Resposta digitada pelo jogador
mensagem = ""                        # Mensagem de feedback (Correto/Errado)
cor_mensagem = PRETO                 # Cor do feedback, muda dependendo da resposta
acertos = 0                           # Contador de acertos do jogador
jogo_acabou = False                   # Flag indicando se acabou o jogo

# ======================
# Funções auxiliares
# ======================

def preparar_frase(frase):
    """Remove palavras irrelevantes da frase e retorna lista de palavras importantes."""
    palavras = frase.lower().split()  # Divide a frase em palavras minúsculas # chamada em linha 84
    return [p for p in palavras if p not in palavras_ignoradas]  # Filtra palavras importantes

def gerar_sigla(palavras):
    """Gera a sigla a partir da primeira letra de cada palavra."""
    return "".join(p[0].upper() for p in palavras)  # Junta primeiras letras em maiúsculas # chamada em linha 85

def desenhar_texto(texto, x, y, cor=PRETO):
    """Desenha texto na tela na posição (x, y) com a cor desejada."""
    img = FONTE.render(texto, True, cor)  # Cria uma superfície com o texto renderizado
    TELA.blit(img, (x, y))                # Desenha a superfície na tela # usada em várias linhas do loop principal, ex: 147, 150, 170

def nova_rodada():
    """Inicia uma nova rodada escolhendo uma frase aleatória."""
    global frase_atual, sigla_correta, resposta, mensagem, cor_mensagem, frases_disponiveis, jogo_acabou

    if not frases_disponiveis:  # Se não houver mais frases disponíveis
        jogo_acabou = True       # Marca o jogo como acabado
        return                   # Sai da função

    frase_atual = random.choice(frases_disponiveis)  # Escolhe uma frase aleatória
    frases_disponiveis.remove(frase_atual)           # Remove para não repetir
    sigla_correta = gerar_sigla(preparar_frase(frase_atual))  # Gera a sigla correta
    resposta = ""          # Limpa a resposta digitada
    mensagem = ""          # Limpa o feedback
    cor_mensagem = PRETO   # Reseta cor da mensagem # chamada na linha 130 ao clicar "Próxima"

def reiniciar_jogo():
    """Reinicia o jogo do zero, recarregando frases e resetando acertos."""
    global frases_disponiveis, acertos, jogo_acabou, frase_atual, sigla_correta, resposta, mensagem, cor_mensagem
    frases_disponiveis = frases.copy()  # Recarrega todas as frases
    acertos = 0                          # Reseta contador de acertos
    jogo_acabou = False                   # Reseta flag de fim de jogo
    resposta = ""                        # Limpa resposta
    mensagem = ""                        # Limpa mensagem
    cor_mensagem = PRETO                 # Reseta cor do feedback
    nova_rodada()                        # Chama nova rodada # linha 136 ao iniciar jogo

# ======================
# Estados do jogo
# ======================
menu = True     # Controla se estamos no menu inicial
jogando = False # Controla se estamos na tela de jogo

# ======================
# Loop principal
# ======================
while True:
    TELA.fill(BRANCO)  # Limpa a tela com branco a cada frame

    # ======================
    # Eventos
    # ======================
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Se o usuário fechar a janela
            pygame.quit()               # Encerra Pygame
            sys.exit()                  # Sai do programa

        # ======================
        # Digitação do jogador
        # ======================
        if evento.type == pygame.KEYDOWN and jogando and not jogo_acabou:
            if evento.key == pygame.K_BACKSPACE:  # Apagar última letra
                resposta = resposta[:-1]
            elif evento.key == pygame.K_RETURN:   # Validar resposta
                if resposta.upper() == sigla_correta:  # Se correta
                    mensagem = f"CORRETO! A sigla é {sigla_correta}"
                    cor_mensagem = VERDE             # Feedback verde
                    acertos += 1                     # Incrementa acertos
                else:
                    mensagem = f"ERRADO! A sigla correta é {sigla_correta}"
                    cor_mensagem = VERMELHO          # Feedback vermelho
            else:
                resposta += evento.unicode  # Adiciona letra digitada à resposta

        # ======================
        # Clique do mouse
        # ======================
        if evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos
            if menu and 300 < x < 500 and 200 < y < 260:  # Botão JOGAR
                menu = False
                jogando = True
                reiniciar_jogo()  # Reinicia jogo do zero # linha 136
            if jogando and 600 < x < 750 and 20 < y < 60 and not jogo_acabou:  # Botão Próxima rodada
                nova_rodada()  # Escolhe nova frase # linha 130
            if jogo_acabou and 300 < x < 500 and 300 < y < 360:  # Botão Reiniciar
                reiniciar_jogo()  # Reinicia jogo do zero # linha 136

    # ======================
    # Menu principal
    # ======================
    if menu:
        desenhar_texto("DESAFIO DAS SIGLAS", 250, 120, AZUL)  # Título do menu
        pygame.draw.rect(TELA, VERDE, (300, 200, 200, 60))   # Botão JOGAR
        desenhar_texto("JOGAR", 360, 215, PRETO)             # Texto do botão

    # ======================
    # Tela do jogo
    # ======================
    if jogando:
        if jogo_acabou:
            desenhar_texto(f"Fim do jogo!", 320, 150, VERMELHO)  # Mensagem final
            desenhar_texto(f"Você acertou {acertos} de {len(frases)}", 230, 200, VERMELHO)  # Resultado
            pygame.draw.rect(TELA, VERDE, (300, 300, 200, 60))  # Botão Reiniciar
            desenhar_texto("REINICIAR", 320, 315, PRETO)        # Texto do botão
        else:
            pygame.draw.rect(TELA, AZUL, (600, 20, 150, 40))    # Botão Próxima rodada
            desenhar_texto("PRÓXIMA", 620, 30, BRANCO)         # Texto do botão

            desenhar_texto("Frase:", 50, 50)                   # Label "Frase"
            desenhar_texto(frase_atual, 50, 90, AZUL)         # Mostra a frase atual

            desenhar_texto("Escreve a sigla:", 50, 160)       # Label "Escreve a sigla"
            pygame.draw.rect(TELA, PRETO, (50, 200, 300, 40), 2)  # Caixa de entrada
            desenhar_texto(resposta, 60, 210)                 # Mostra o que o jogador digitou

            desenhar_texto(mensagem, 50, 270, cor_mensagem)  # Feedback dinâmico (verde/vermelho) # linha 101

            sigla_parcial = resposta.upper()                  # Mostra sigla parcial
            desenhar_texto(f"Sigla parcial: {sigla_parcial}", 50, 330, AZUL)  # Cor diferenciada

            desenhar_texto(f"Acertos: {acertos}", 600, 450, AZUL)  # Contador de acertos

    pygame.display.update()  # Atualiza tela com todas alterações feitas no frame

