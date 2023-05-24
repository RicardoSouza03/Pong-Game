import pygame
from screen import window_dict, load_window
from ball import Ball
from bars import Bar
from level_control import increase_game_speed
from button import Button

class Game():
    def __init__(self) -> None:
        self.running = True
        self.speed_time_increase = 1800
        self.paused = False
        self.current_time = 0
        self.paused_time = 0
        self.screen = load_window()
        self.font = pygame.font.SysFont('arialblack', 40)
        self.clock = pygame.time.Clock()
        self.create_images()

    def draw_text(self, text, text_color, pos_x, pos_y):
        img = self.font.render(text, True, text_color)
        self.screen.blit(img, (pos_x, pos_y))

    def pause_game(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_ESCAPE] and self.paused == False:
            self.paused = True
            self.paused_time = self.current_time

    def create_images(self):
        self.unpause_img = pygame.image.load('images/button_resume.png').convert_alpha()
        self.quit_img = pygame.image.load('images/button_quit.png').convert_alpha()

    def run_game(self):
        self.ball = Ball()
        self.bar_left = Bar('left')
        self.bar_right = Bar('right')
        self.unpause_btn = Button(300, 150, self.unpause_img)
        self.quit_btn = Button(330, 250, self.quit_img)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            if self.paused == False:
                self.screen.fill("black")
                self.ball.draw_bounce_ball(self.screen, self.bar_left.draw(self.screen), self.bar_right.draw(self.screen))
                self.bar_left.draw(self.screen)
                self.bar_right.draw(self.screen)
                self.current_time += 1
                self.pause_game()

                if self.current_time == self.speed_time_increase:
                    increase_game_speed([self.bar_left, self.bar_right, self.ball])
                    self.speed_time_increase += 1800
                    pygame.display.set_caption(f'{window_dict["caption"]} - Level {window_dict["level_indicator"]}')

                if window_dict['level_indicator'] == 10:
                    self.draw_text(self.screen, 'You won!', self.font, 'green', 300, 200)

            elif self.paused == True:
                if self.unpause_btn.draw(self.screen):
                    self.current_time = self.paused_time
                    self.paused = False
                if self.quit_btn.draw(self.screen):
                    self.running = False

            pygame.display.flip()
            pygame.display.update()

            self.clock.tick(60)

if __name__ == "__main__":
    Game().run_game()