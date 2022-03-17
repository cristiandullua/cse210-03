import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.scripting.control_growing import ControlGrowing
from game.shared.point import Point


class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast, script)

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments or with each other.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snakes = cast.get_actors("snakes")
        scores = cast.get_actors("scores")

        snake_1 = snakes[0]
        snake_2 = snakes[1]

        head_1 = snake_1.get_segments()[0]
        head_2 = snake_2.get_segments()[0]
        segments_1 = snake_1.get_segments()[1:]
        segments_2 = snake_2.get_segments()[1:]

        segments = segments_1 + segments_2
    
        for segment in segments:
            if head_1.get_position().equals(segment.get_position()) or head_1.get_position().equals(head_2.get_position()):
                scores[1].add_points(1)
                self._is_game_over = True
            elif head_2.get_position().equals(segment.get_position()) or head_2.get_position().equals(head_1.get_position()):
                scores[0].add_points(1)
                self._is_game_over = True
        
    def _handle_game_over(self, cast, script):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snakes = cast.get_actors("snakes")
        scores = cast.get_actors("scores")

        if self._is_game_over:
            for snake in snakes:
                segments = snake.get_segments()

                x = int(constants.MAX_X / 2)
                y = int(constants.MAX_Y / 2)
                position = Point(x, y)

                message = Actor()
            # set winner message
                winner_message = scores[0].get_name() if scores[0].get_points() > 0 else scores[1].get_name()

                message.set_text("Game Over! " + winner_message + " won")
                message.set_position(position)
                cast.add_actor("messages", message)

                for segment in segments:
                    segment.set_color(constants.WHITE)

            script.get_all_actions().pop("update")