import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from game.scripting.control_growing import ControlGrowing
from game.services.keyboard_service import KeyboardService

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
            self._handle_game_over(cast)
            # self._handle_snake_collision(cast)


    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments or with each other.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snake = cast.get_first_actor("snakes")
        snake2 = cast.get_first_actor('snake2')
        head = snake.get_segments()[0]
        head2 = snake2.get_segments()[0]
        segments = snake.get_segments()[1:]
        segments2 = snake2.get_segments()[1:]
        
        for segment in segments:
            if head.get_position().equals(segment.get_position()):
                self._is_game_over = True
            for segment_second in segments2:
                if head2.get_position().equals(segment_second.get_position()):
                    self._is_game_over = True
                if head2.get_position().equals(segment.get_position()):
                    self._is_game_over = True
                if head.get_position().equals(segment_second.get_position()):
                    self._is_game_over = True
                

    # def _handle_snake_collision(self,cast):
    #         '''Sets the game over flag if the snakes collides with each other.
            
    #         Args:
    #             cast(Cast): The cast of Actors in the game.
    #         '''

    #         snake = cast.get_first_actor('snakes')
    #         snake2 = cast.get_first_actor('snake2')
    #         head = snake.get_segments()[0]
    #         head2 = snake2.get_segments()[0]
    #         segments = snake.get_segments()[1:]
    #         segments2 = snake2.get_segments()[1:]

    #         #First snake
    #         for segment in segments:
    #             segment_snake = segment
    #             return segment_snake
            
    #         #Second snake
    #         for segments2 in segments:
    #             segment_snake2 = segments2
    #             return segment_snake2
            
    #         if head.get_position().equals(segment_snake2.get_position()):
    #             self._is_game_over = True
    #         elif head2.get_position().equals(segment_snake.get_position()):
    #             self._is_game_over = True
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            snake = cast.get_first_actor("snakes")
            snake2 = cast.get_first_actor("snake2")
            segments = snake.get_segments()
            segments2 = snake2.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments:
                segment.set_color(constants.WHITE)
            for segment in segments2:
                segment.set_color(constants.WHITE)
