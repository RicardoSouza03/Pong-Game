import pygame
from screen import window_dict, load_window
from ball import bouncing_ball, create_ball_obj
from bars import bar, create_bar_obj
from level_control import increase_game_speed

game_dict = {
    "running": True,
    "speed_time_increase": 30000
}

def main():
    screen = load_window()
    clock = pygame.time.Clock()
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

        pygame.display.flip()

        clock.tick(60)

if __name__ == "__main__":
    main()