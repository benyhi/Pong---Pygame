import pygame

class Player:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x,y,width,height)
        self.color = color
        self.velocidad = 5

    #Dibujar jugador en la pantalla
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    #Movimiento del jugador
    def movement(self, key , key_up, key_down, screen_height):
        if key[key_up] and self.rect.y > 0: 
            self.rect.y -= self.velocidad
        
        if key[key_down] and self.rect.y + self.rect.height < screen_height:
            self.rect.y += self.velocidad
