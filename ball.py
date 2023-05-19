import pygame

ball_dict = {
    "ball_x_speed": 5,
    "ball_y_speed": 3,
    "collision_tolerance": 10,
    "ball_radius": 50,
    "left": 250,
    "top": 250,
    "width": 25,
    "heigth": 25,
}

def bouncing_ball(screen, ball, bar_left, bar_right):
    ball.y += ball_dict["ball_y_speed"]
    ball.x += ball_dict["ball_x_speed"]
    collision_tolerance = ball_dict["collision_tolerance"]

    if ball.right > screen.get_width() + 20 or ball.left <= -20:
        screen.quit()
    if ball.bottom >= screen.get_height() or ball.top <= 0:
        ball_dict["ball_y_speed"] = -ball_dict["ball_y_speed"]

    if ball.colliderect(bar_left):
        if (
            abs(bar_left.top - ball.bottom) < collision_tolerance
            or abs(bar_left.bottom - ball.top) < collision_tolerance
            ) and ball_dict["ball_y_speed"] > 0:
            ball_dict["ball_y_speed"] = -ball_dict["ball_y_speed"]
        if (
            abs(bar_left.right - ball.left) < collision_tolerance
            or abs(bar_left.left - ball.right) < collision_tolerance
            ) and ball_dict["ball_x_speed"] < 0:
            ball_dict["ball_x_speed"] = -ball_dict["ball_x_speed"]
        
    if ball.colliderect(bar_right):
        if (
            abs(bar_right.top - ball.bottom) < collision_tolerance
            or abs(bar_right.bottom - ball.top) < collision_tolerance
            ) and ball_dict["ball_y_speed"] < 0:
            ball_dict["ball_y_speed"] = -ball_dict["ball_y_speed"]
        if (
            abs(bar_right.right - ball.left) < collision_tolerance
            or abs(bar_right.left - ball.right) < collision_tolerance
            ) and ball_dict["ball_x_speed"] > 0:
            ball_dict["ball_x_speed"] = -ball_dict["ball_x_speed"]

    pygame.draw.rect(screen, "white", ball, border_radius=ball_dict["ball_radius"])