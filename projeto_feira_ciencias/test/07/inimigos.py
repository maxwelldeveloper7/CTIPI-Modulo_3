import pygame
import sys
import random

# Inicializa o Pygame
pygame.init()

# Configurações da janela
largura_tela, altura_tela = 800, 600
screen = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Inimigos")

# Carrega a imagem da nave e do inimigo
nave = pygame.image.load('nave.png')
inimigo = pygame.image.load('inimigo.png')

# Posição inicial da nave
x, y = largura_tela // 2, altura_tela - 100
velocidade = 1

# Lista para armazenar os inimigos
inimigos = []

# Cria 5 inimigos em posições aleatórias
for i in range(5):
    x_inimigo = random.randint(0, largura_tela - inimigo.get_width())
    y_inimigo = random.randint(-100, -40)
    inimigos.append([x_inimigo, y_inimigo])

# Velocidade dos inimigos
velocidade_inimigos = 1

# Função para verificar colisão
def colisao(x1, y1, largura1, altura1, x2, y2, largura2, altura2):
    if (x1 < x2 + largura2 and
        x1 + largura1 > x2 and
        y1 < y2 + altura2 and
        y1 + altura1 > y2):
        return True
    return False

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Detecta as teclas pressionadas
    keys = pygame.key.get_pressed()

    # Move a nave para a esquerda ou direita, limitando os movimentos
    if keys[pygame.K_LEFT] and x > 0:
        x -= velocidade
    if keys[pygame.K_RIGHT] and x < largura_tela - nave.get_width():
        x += velocidade

    # Preenche o fundo com preto
    screen.fill((0, 0, 0))

    # Movimenta e desenha os inimigos
    for inimigo_pos in inimigos:
        inimigo_pos[1] += velocidade_inimigos  # Move o inimigo para baixo

        # Se o inimigo sair da tela, reposiciona-o no topo
        if inimigo_pos[1] > altura_tela:
            inimigo_pos[0] = random.randint(0, largura_tela - inimigo.get_width())
            inimigo_pos[1] = random.randint(-100, -40)

        # Verifica colisão com a nave
        if colisao(x, y, nave.get_width(), nave.get_height(), inimigo_pos[0], inimigo_pos[1], inimigo.get_width(), inimigo.get_height()):
            running = False  # Se houver colisão, encerra o jogo

        # Desenha o inimigo na tela
        screen.blit(inimigo, inimigo_pos)

    # Desenha a nave na nova posição
    screen.blit(nave, (x, y))

    # Atualiza a tela
    pygame.display.flip()

# Encerra o Pygame
pygame.quit()
sys.exit()
