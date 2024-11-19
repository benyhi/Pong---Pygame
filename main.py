import pygame
from player import Player
from ball import Ball

NEGRO = (0,0,0)
BLANCO = (255,255,255)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

#Inicializacion del juego
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("prueba juego")
reloj = pygame.time.Clock()
font = pygame.font.SysFont('Times New Roman', 30)

#Inicializacion del jugador
player_left = Player(0, screen.get_height()//2 - 100, 50, 200, VERDE)
player_right = Player(screen.get_width() - 50, screen.get_height()//2 - 100, 50, 200, AZUL)
ball = Ball(screen.get_width()//2, screen.get_height()//2, 20, 20)

#Inicializacion del bucle de juego
running = True
initial_score_right = 0
initial_score_left = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False

    #Relleno el fondo de color blanco
    screen.fill(BLANCO)

    #Detecto la tecla presionada
    key = pygame.key.get_pressed()

    #Inicializo el movimiento del jugador
    player_left.movement(key, pygame.K_w, pygame.K_s, screen.get_height())
    player_left.draw(screen)
    player_right.movement(key, pygame.K_UP,pygame.K_DOWN, screen.get_height())
    player_right.draw(screen)

    ball.draw(screen)
    ball.movement(screen)

    #Collision con los jugadores
    if ball.rect.colliderect(player_right.rect) or ball.rect.colliderect(player_left.rect):
        ball.vel_x *= -1

    if ball.rect.x < 0: 
        initial_score_right += 1
        ball.reset(screen)

    if ball.rect.x > screen.get_width():
        initial_score_left += 1
        ball.reset(screen)

    #Texto en pantalla
    point_left = font.render(f"Puntaje:{str(initial_score_left)}",True,NEGRO)
    point_right = font.render(f"Puntaje:{str(initial_score_right)}", True,NEGRO)
    screen.blit(point_left, (screen.get_width()// 4 , screen.get_height()-50))
    screen.blit(point_right, (screen.get_width()//4 * 3, screen.get_height()-50))


    pygame.display.flip()
    reloj.tick(60)

pygame.quit()