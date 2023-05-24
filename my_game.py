import pygame
from screen import window_dict, load_window
from ball import Ball
from bars import Bar
from level_control import increase_game_speed
from button import Button
import sched, time

game_dict = {
    "running": True,
    "speed_time_increase": 1800,
    "paused": False,
    "current_time": 0,
    "game_paused": 0,
}

def draw_text(screen, text, font, text_color, pos_x, pos_y):
    img = font.render(text, True, text_color)
    screen.blit(img, (pos_x, pos_y))

def pause_game():
    key = pygame.key.get_pressed()

    if key[pygame.K_ESCAPE] and game_dict['paused'] == False:
        game_dict['paused'] = True
        game_dict['game_paused'] = game_dict['current_time']
        print(game_dict['game_paused'])

def main():
    screen = load_window()
    font = pygame.font.SysFont('arialblack', 40)
    clock = pygame.time.Clock()
    
    unpause_img = pygame.image.load('images/button_resume.png').convert_alpha()
    quit_img = pygame.image.load('images/button_quit.png').convert_alpha()
    unpause_btn = Button(300, 150, unpause_img)
    quit_btn = Button(330, 250, quit_img)

    ball = Ball()
    bar_left = Bar('left')
    bar_right = Bar('rigth')

    while game_dict["running"]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_dict['running'] = False

        if game_dict['paused'] == False:
            screen.fill("black")
            ball.draw_bounce_ball(screen, bar_left.draw(screen), bar_right.draw(screen))
            bar_left.draw(screen)
            bar_right.draw(screen)
            game_dict['current_time'] += 1
            pause_game()

            if game_dict['current_time'] == game_dict["speed_time_increase"]:
                increase_game_speed([bar_left, bar_right, ball])
                game_dict['speed_time_increase'] += 1800
                pygame.display.set_caption(f'{window_dict["caption"]} - Level {window_dict["level_indicator"]}')

            if window_dict['level_indicator'] == 10:
                draw_text(screen, 'You won!', font, 'green', 300, 200)

        elif game_dict['paused'] == True:
            if unpause_btn.draw(screen):
                game_dict['current_time'] = game_dict['game_paused']
                game_dict['paused'] = False
            if quit_btn.draw(screen):
                game_dict['running'] = False

        pygame.display.flip()
        pygame.display.update()

        clock.tick(60)

if __name__ == "__main__":
    main()