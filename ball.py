import pygame

class Ball:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (255, 0, 0)
        self.vel_x = 7
        self.vel_y = 7
    
    #Dibujar pelota en la pantalla
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    #Movimientos de la pelota
    def movement(self, screen):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        if self.rect.top <= 0 or self.rect.bottom >= screen.get_height():
            self.vel_y *= -1
        
    #Logica para resetear la pelota cuando hay un punto
    def reset(self, screen):
        self.rect.center = (screen.get_width() // 2, screen.get_height() // 2)
        self.vel_x *= -1
        self.vel_y *= -1