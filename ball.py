import pygame

class Ball():
    def __init__(self) -> None:
        self.x_speed = 5
        self.y_speed = 3
        self.collision_tolerance = 10
        self.radius = 50
        self.left = 250
        self.top = 250
        self.width = 25
        self.heigth = 25
        self.ball_obj()

    def ball_obj(self):
        self.ball = pygame.Rect(self.left, self.top, self.width, self.heigth)

    def ball_collidion(self, bars):
        if self.ball.colliderect(bars[0]):
            if (
                abs(bars[0].top - self.ball.bottom) < self.collision_tolerance
                or abs(bars[0].bottom - self.ball.top) < self.collision_tolerance
                ) and self.y_speed > 0:
                self.y_speed = -self.y_speed
            if (
                abs(bars[0].right - self.ball.left) < self.collision_tolerance
                or abs(bars[0].left - self.ball.right) < self.collision_tolerance
                ) and self.x_speed < 0:
                self.x_speed = -self.x_speed
        
        if self.ball.colliderect(bars[1]):
            if (
                abs(bars[1].top - self.ball.bottom) < self.collision_tolerance
                or abs(bars[1].bottom - self.ball.top) < self.collision_tolerance
                ) and self.y_speed < 0:
                self.y_speed = -self.y_speed
            if (
                abs(bars[1].right - self.ball.left) < self.collision_tolerance
                or abs(bars[1].left - self.ball.right) < self.collision_tolerance
                ) and self.x_speed > 0:
                self.x_speed = -self.x_speed

    def draw_bounce_ball(self, screen, bar_left, bar_right):
        self.ball.x += self.x_speed
        self.ball.y += self.y_speed

        if self.ball.right > screen.get_width() + 20 or self.ball.left <= -20:
            screen.quit()
        if self.ball.bottom >= screen.get_height() or self.ball.top <= 0:
            self.y_speed = -self.y_speed

        self.ball_collidion([bar_left, bar_right])

        return pygame.draw.rect(screen, "white", self.ball, border_radius=self.radius)
    
    def increase_speed(self):
        if self.x_speed < 0:
            self.x_speed += -1
        else:
            self.x_speed += 1
        if self.y_speed < 0:
            self.y_speed += -1
        else:
            self.y_speed += 1