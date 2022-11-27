import os
import random

from game.casting.actor import Actor
from game.casting.object import Object
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_OBJECTS = 40


def main():
    
    cast = Cast()
    
    banner = Actor()
    banner.set_text("Score: ")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    

    x = int(MAX_X / 2)
    position = Point(x, MAX_Y - 20)

    player = Actor()
    player.set_text("#")
    player.set_font_size(FONT_SIZE)
    player.set_color(WHITE)
    player.set_position(position)
    cast.add_actor("players", player)

    for n in range(DEFAULT_OBJECTS):
        text = random.choice(['*', 'o'])
        x = random.randint(1, COLS - 1)
        y = random.randint(-10, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        if text == "*":
            color = Color(0, 225, 225)
        elif text == "o":
            color = Color(111, 64, 60)

        object = Object()
        object.set_text(text)
        object.set_font_size(FONT_SIZE)
        object.set_color(color)
        object.set_position(position)
        object.set_velocity(Point(0, 1))
        cast.add_actor("objects", object)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()