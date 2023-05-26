import pygame
from screen import window_dict

class Bar():
    def __init__(self, side) -> None:
        self.side = side
        self.speed = 6
        self.top = 200
        self.width = 10
        self.heigth = 80
        self.bar_obj()

    def bar_obj(self):
        if self.side == 'left':
            self.left = 5
            self.rect = pygame.Rect(self.left, self.top, self.width, self.heigth)
        else:
            self.left = window_dict['width'] - 15
            self.rect = pygame.Rect(self.left, self.top, self.width, self.heigth)

    def draw(self, screen):
        key = pygame.key.get_pressed()

        if self.side == "left":
            if key[pygame.K_w] and self.rect.y>0:
                self.rect.y -= self.speed
            if key[pygame.K_s] and self.rect.y<screen.get_height()-80:
                self.rect.y += self.speed
        else:
            if key[pygame.K_UP] and self.rect.y>0:
                self.rect.y -= self.speed
            if key[pygame.K_DOWN] and self.rect.y<screen.get_height()-80:
                self.rect.y += self.speed

        return pygame.draw.rect(screen, "white", self.rect, 20)
    
    def increase_speed(self):
        self.speed += 1
