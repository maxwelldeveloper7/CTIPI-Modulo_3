import pygame
import sys
import random

# Inicializa o Pygame
pygame.init()

# Inicializa o mixer de som
pygame.mixer.init()

# Configurações da janela
largura_tela, altura_tela = 800, 600
screen = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Sons e Efeitos Visuais")

# Carrega a imagem da nave, do inimigo, do projétil e da explosão
nave = pygame.image.load('nave.png')
inimigo = pygame.image.load('inimigo.png')
projetil = pygame.image.load('projetil.png')
explosao = pygame.image.load('explosao.png')

# Carrega o som do disparo e a música de fundo
som_disparo = pygame.mixer.Sound('disparo.wav')
pygame.mixer.music.load('musica_fundo.mp3')
pygame.mixer.music.play(-1)  # Música em loop

# Posição inicial da nave
x, y = largura_tela // 2, altura_tela - 100
velocidade = 5

# Lista para armazenar os inimigos e projéteis
inimigos = []
projeteis = []

# Cria 5 inimigos em posições aleatórias
for i in range(5):
    x_inimigo = random.randint(0, largura_tela - inimigo.get_width())
    y_inimigo = random.randint(-100, -40)
    inimigos.append([x_inimigo, y_inimigo])

# Velocidade dos inimigos
velocidade_inimigos = 5

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                projeteis.append([x + nave.get_width() // 2, y])
                som_disparo.play()  # Reproduz o som de disparo

    # Detecta as teclas pressionadas
    keys = pygame.key.get_pressed()

    # Move a nave para a esquerda ou direita, limitando os movimentos
    if keys[pygame.K_LEFT] and x > 0:
        x -= velocidade
    if keys[pygame.K_RIGHT] and x < largura_tela - nave.get_width():
        x += velocidade

    # Preenche o fundo com preto
    screen.fill((0, 0, 0))

    # Atualiza a posição dos projéteis e remove os que saem da tela
    for p in projeteis:
        p[1] -= 10  # Move o projétil para cima
        if p[1] < 0:
            projeteis.remove(p)

    # Movimenta e desenha os inimigos
    for inimigo_pos in inimigos:
        inimigo_pos[1] += velocidade_inimigos  # Move o inimigo para baixo

        # Se o inimigo sair da tela, reposiciona-o no topo
        if inimigo_pos[1] > altura_tela:
            inimigo_pos[0] = random.randint(0, largura_tela - inimigo.get_width())
            inimigo_pos[1] = random.randint(-100, -40)

        # Verifica colisões entre projéteis e inimigos
        for p in projeteis:
            if colisao(p[0], p[1], projetil.get_width(), projetil.get_height(), inimigo_pos[0], inimigo_pos[1], inimigo.get_width(), inimigo.get_height()):
                projeteis.remove(p)
                inimigos.remove(inimigo_pos)
                pontuacao += 10
                # Desenha a explosão
                screen.blit(explosao, (inimigo_pos[0], inimigo_pos[1]))

        # Desenha o inimigo na tela
        screen.blit(inimigo, inimigo_pos)

    # Desenha a nave na nova posição
    screen.blit(nave, (x, y))

    # Desenha cada projétil na tela
    for p in projeteis:
        screen.blit(projetil, p)

    # Atualiza a tela
    pygame.display.flip()

# Encerra o Pygame
pygame.quit()
sys.exit()