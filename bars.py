import pygame
from screen import window_dict

bar_dict = {
    "rect_speed": 8,
    "l_left": 5,
    "r_left": window_dict["width"] - 15,
    "top": 200,
    "width": 10,
    "heigth": 80,
}

def bar(screen, bar_rect, side="right"):
    rect_speed = bar_dict["rect_speed"]
    key = pygame.key.get_pressed()

    if side == "left":
        if key[pygame.K_w] and bar_rect.y>0:
            bar_rect.y -= rect_speed
        if key[pygame.K_s] and bar_rect.y<screen.get_height()-80:
            bar_rect.y += rect_speed
    else:
        if key[pygame.K_UP] and bar_rect.y>0:
            bar_rect.y -= rect_speed
        if key[pygame.K_DOWN] and bar_rect.y<screen.get_height()-80:
            bar_rect.y += rect_speed

    pygame.draw.rect(screen, "white", bar_rect, 20)