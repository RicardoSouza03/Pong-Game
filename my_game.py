import pygame
from screen import window_dict, load_window
from ball import bouncing_ball, create_ball_obj
from bars import bar, create_bar_obj
from level_control import increase_game_speed
from button import Button

game_dict = {
    "running": True,
    "speed_time_increase": 30000,
    "paused": False,
}

def draw_text(screen, text, font, text_color, pos_x, pos_y):
    img = font.render(text, True, text_color)
    screen.blit(img, (pos_x, pos_y))

def main():
    screen = load_window()
    font = pygame.font.SysFont('arialblack', 40)
    clock = pygame.time.Clock()
    
    unpause_img = pygame.image.load('images/button_resume.png').convert_alpha()
    quit_img = pygame.image.load('images/button_quit.png').convert_alpha()
    unpause_btn = Button(300, 150, unpause_img)
    quit_btn = Button(330, 250, quit_img)

    ball = create_ball_obj()
    bar_rect_left = create_bar_obj('left')
    bar_rect_right = create_bar_obj('rigth')

    while game_dict["running"]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_dict['running'] = False

        screen.fill("black")
        bouncing_ball(screen, ball, bar_rect_left, bar_rect_right)
        bar(screen, bar_rect_left, side="left")
        bar(screen, bar_rect_right, side="rigth")

        current_time = pygame.time.get_ticks()
        if current_time >= game_dict["speed_time_increase"]:
            increase_game_speed()
            game_dict['speed_time_increase'] += 30000
            pygame.display.set_caption(f'{window_dict["caption"]} - Level {window_dict["level_indicator"]}')

        if window_dict['level_indicator'] == 10:
            draw_text(screen, 'You won!', font, 'green', 300, 200)

        pygame.display.flip()
        pygame.display.update()

        clock.tick(60)

if __name__ == "__main__":
    main()