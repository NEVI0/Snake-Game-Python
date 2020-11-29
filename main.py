# Imports
import pygame, sys

from fruit import Fruit
from snake import Snake

from pygame.locals import *

# Configurações do PyGame
pygame.init()
pygame.display.set_caption('Snack Game') # Titulo do Jogo
pygame.display.set_icon(pygame.image.load('assets/game_logo.png')) # Icone do Jogo

# Musica do Jogo
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.load('assets/soundtrack.mp3')
pygame.mixer.music.play(-1)

# Constantes
WINDOW_SIZE: tuple = (1000, 550) # Tamanho da Tela
GAME_SCREEN: pygame.Surface = pygame.display.set_mode(WINDOW_SIZE, 0, 32) # Tela de Jogo
TIMER = pygame.time.Clock() # Temporizador

# Objetos
fruit_obj: Fruit = Fruit()
snake_obj: Snake = Snake()

# Variavel de pontos, fim de jogo e a fonte dos textos
points: int = 0
is_dead: bool = False
font = pygame.font.SysFont('Trebuchet MS', 24, True, True)

# Funçao que reestarta o jogo
def restart():
    global points, is_dead, snake_obj, fruit_obj

    points = 0
    is_dead = False
    snake_obj = Snake()
    fruit_obj = Fruit()

# Tela de fim de jogo
def end_game_screen():

    GAME_SCREEN.fill((255, 255, 255))  # Deixa a tela branca
    end_message = font.render(f'Fim de Jogo! Você conseguiu {points} pontos, recione R para reiniciar!', True, (0, 0, 0))  # Mensagem de game over
    end_message_rect = end_message.get_rect()
    end_message_rect.center = (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2) # Centraliza a mensagem no meio da tela

    # Eventos do Jogo
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            sys.exit()

        if e.type == KEYDOWN:
            if e.key == K_r:
                restart() # Restarta o jogo

    GAME_SCREEN.blit(end_message, end_message_rect) # Renderiza a mensagem de fim de jogo na tela
    pygame.display.update()

# Game Loop
while True:

    points_text = font.render(f'Pontos: {points}', True, (0, 0, 0)) # Cria a mensagem os os pontos
    points_text_rect = points_text.get_rect()
    points_text_rect.center = (WINDOW_SIZE[0] // 2, 25) # Centraliza a mensagem no meio da tela

    GAME_SCREEN.fill((255, 255, 255))  # Background Color Branco
    snake_rect = pygame.draw.rect(GAME_SCREEN, (0, 0, 255), snake_obj.location) # Desenha a cobra na tela

    GAME_SCREEN.blit(fruit_obj.image, fruit_obj.location)  # Renderiza a imagem da fruta na tela
    GAME_SCREEN.blit(points_text, points_text_rect)  # Renderiza o texto com os pontos na tela

    # Eventos do Jogo
    for e in pygame.event.get():
        # Evento de fechar
        if e.type == QUIT:
            pygame.quit()
            sys.exit()

        # Eventos do teclado
        if e.type == KEYDOWN:
            if e.key == K_RIGHT:
                snake_obj.move_right() # Move a cobra para a direita
            if e.key == K_LEFT:
                snake_obj.move_left() # Move a cobra para a esquerda
            if e.key == K_UP:
                snake_obj.move_up() # Move a cobra para cima
            if e.key == K_DOWN:
                snake_obj.move_down() # Move a cobra para baixo

    snake_obj.update_location()  # Atualiza a localização da cobra

    # Verifica se a cobra colidiu com a fruta
    if snake_rect.colliderect(fruit_obj.rect):
        points += 1 # Incrementa os pontos
        snake_obj.update_length() # Aumenta o tamanho da cobra
        fruit_obj.collision() # Renderiza a frunta em outra posição

    snake_obj.update_body_head() # Atualiza a cabeça e o corpo da cobra

    # Verifica se a cobra colidiu em si mesma
    if snake_obj.collision():
        is_dead = True
        while is_dead:
            end_game_screen()

    snake_obj.update(WINDOW_SIZE, GAME_SCREEN) # Atualiza o objeto da cobra e o seu tamanho

    pygame.display.update() # Atualiza a tela
    TIMER.tick(60) # Roda o jogo em 60 FPS
