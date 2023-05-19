from ball import ball_dict
from bars import bar_dict
from screen import window_dict

def increase_game_speed():
    if ball_dict["ball_x_speed"] < 0:
        ball_dict["ball_x_speed"] += -1
    else:
        ball_dict["ball_x_speed"] += 1
    if ball_dict["ball_y_speed"] < 0:
        ball_dict["ball_y_speed"] += -2
    else:
        ball_dict["ball_y_speed"] += 2
    bar_dict["rect_speed"] += 1.5
    window_dict["level_indicator"] += 1