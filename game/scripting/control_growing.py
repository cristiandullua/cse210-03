import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlGrowing(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        #self._direction = Point(constants.CELL_SIZE, 0)
        self._count = 1

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        
        # left
        if self._keyboard_service.is_key_down('a'):
            #self._direction = Point(-constants.CELL_SIZE, 0)
            self._count += 1

        
        # right
        if self._keyboard_service.is_key_down('d'):
            #self._direction = Point(constants.CELL_SIZE, 0)
            self._count += 1

        
        # up
        if self._keyboard_service.is_key_down('w'):
            #self._direction = Point(0, -constants.CELL_SIZE)
            self._count += 1

        
        # down
        if self._keyboard_service.is_key_down('s'):
            #self._direction = Point(0, constants.CELL_SIZE)
            self._count += 1

        
        snake = cast.get_first_actor("snakes")
        #snake.turn_head(self._direction)

        #my_list = [10, 25, 35, 50, 65, 80, 95, 105, 115, 125, 140, 155, 170]
        if  self._count == 12:
            score = cast.get_first_actor("scores")
            score.add_points(1)
            snake = snake.grow_tail(1)
            self._count = 0