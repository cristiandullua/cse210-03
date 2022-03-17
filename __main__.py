import constants

from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.snake import Snake
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point
from game.scripting.control_growing import ControlGrowing

def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("snakes", Snake(constants.RED))
    cast.add_actor("snakes", Snake(constants.GREEN))
    cast.add_actor("scores", Score("Player 1"))
        # create 2nd Score and set it to the right position 
    score_2 = Score("Player 2")
    score_2.set_position(Point(constants.MAX_X - constants.CELL_SIZE * len(score_2.get_text()), 0))
    cast.add_actor("scores", score_2)
    
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("update", ControlGrowing())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()
