import constants
from game.scripting.action import Action
from game.shared.point import Point

RIGHT = Point(constants.CELL_SIZE, 0)
LEFT = Point(-constants.CELL_SIZE, 0)
UP = Point(0, -constants.CELL_SIZE)
DOWN = Point(0, constants.CELL_SIZE)

class ControlActorsAction(Action):
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
        self._direction_1 = Point(0, -constants.CELL_SIZE)
        self._direction_2 = Point(0, -constants.CELL_SIZE)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
    # Controls for 1st snake         
        snake_1 = cast.get_actors("snakes")[0]
        
        # Avoid snake trailing back on itself
        if self._keyboard_service.is_key_down('a') and snake_1.get_head().get_velocity() != RIGHT:
            self._direction_1 = LEFT
        
        if self._keyboard_service.is_key_down('d') and snake_1.get_head().get_velocity() != LEFT:
            self._direction_1 = RIGHT
        
        if self._keyboard_service.is_key_down('w') and snake_1.get_head().get_velocity() != DOWN:
            self._direction_1 = UP
        
        if self._keyboard_service.is_key_down('s') and snake_1.get_head().get_velocity() != UP:
            self._direction_1 = DOWN

        snake_1.turn_head(self._direction_1)

    # Controls for 2nd snake
        snake_2 = cast.get_actors("snakes")[1]

        # Avoid snake trailing back on itself
        if self._keyboard_service.is_key_down('j') and snake_2.get_head().get_velocity() != RIGHT:
            self._direction_2 = LEFT        

        if self._keyboard_service.is_key_down('l') and snake_2.get_head().get_velocity() != LEFT:
            self._direction_2 = RIGHT
        
        if self._keyboard_service.is_key_down('i') and snake_2.get_head().get_velocity() != DOWN:
            self._direction_2 = UP
        
        if self._keyboard_service.is_key_down('k') and snake_2.get_head().get_velocity() != UP:
            self._direction_2 = DOWN
        
        snake_2.turn_head(self._direction_2)