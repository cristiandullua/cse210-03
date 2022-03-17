import constants
from game.scripting.action import Action


class ControlGrowing(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._counter = 0

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        self._counter = self._counter + 1

        if self._counter == constants.FRAME_RATE * 5:
            self._counter = 0
            snakes = cast.get_actors("snakes")

            for snake in snakes:
                snake.grow_tail(1)