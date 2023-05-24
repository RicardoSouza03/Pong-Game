import pygame

window_dict = {
    "width": 800,
    "heigth": 500,
    "icon": "images/icon.png",
    "caption": "pong game",
    "level_indicator": 0
}

def load_window():
    pygame.init()
    pygame.display.set_caption(f'{window_dict["caption"]} - Level {window_dict["level_indicator"]}')
    icon = pygame.image.load(window_dict["icon"])
    pygame.display.set_icon(icon)
    screen = pygame.display.set_mode((window_dict["width"], window_dict["heigth"]))

    return screen