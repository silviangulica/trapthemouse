from enum import Enum


class GameModes(Enum):
    """
    Enumeration of game modes used in the game.
    """
    PLAYER_VS_PLAYER_LOCAL = 1
    PLAYER_VS_AI = 2
    PLAYER_VS_PLAYER_SERVER = 3
