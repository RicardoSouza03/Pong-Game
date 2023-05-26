from screen import window_dict

def increase_game_speed(objects):
    for object in objects:
        object.increase_speed()
    window_dict["level_indicator"] += 1