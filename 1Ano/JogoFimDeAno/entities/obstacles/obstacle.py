import pygame as pg
from ..player import Player
from scripts import INITIAL_ALPHA_TRACKER
from collections import deque

# Could add some JSON recognition for the levels

class Obstacle:
    """Obstacle Template Class for the others Obstacles."""
    def __init__(self, x: float, y: float, width: float, height: float, speed: float, spacing_mult: float, color: tuple[int, int, int]) -> None:
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._speed = speed
        self._color = color
        self._spacing_mult = spacing_mult
        self._position_tracker = deque()
        self._position_tracker_times = deque()
        self._position_tracker_lifetime = 0.2 # seconds
        self._initial_alpha_tracker = INITIAL_ALPHA_TRACKER
        self._base_width = self._width
        self._base_height = self._height
        self._ink_stain_surface = pg.Surface((self._base_width, self._base_height), pg.SRCALPHA)
        self._base_ink_stain_surface = pg.Surface((self._base_width, self._base_height), pg.SRCALPHA)
        self._base_ink_stain_surface.fill((0, 0, 0, 0))
        self._has_ink_stain = False
    
    def update(self, dt: float) -> None: pass
    
    def draw(self, screen: pg.Surface) -> None: pass
    
    def check_collision(self, player: Player) -> tuple[bool, list[int]]: pass

    def set_new_resolution(self, new_resolution: tuple[int, int], old_player_info: tuple[tuple[int, int], int], new_player_info: tuple[tuple[int, int], int], new_speed: float) -> None: pass

    def _update_tracker(self, dt: float) -> None: pass

    def _draw_tracker(self, screen: pg.Surface) -> None: pass

    def _draw_ink_stains(self, screen: pg.Surface) -> None: pass

    def _paint_new_stain(self, pos: tuple[float, float], size: float) -> None: pass

    def set_x(self, new_x: float) -> None: self._x = new_x

    def get_x(self) -> int: return self._x

    def set_y(self, new_y: float) -> None: self._y = new_y

    def get_y(self) -> int: return self._y

    def get_spacing_mult(self) -> float: return self._spacing_mult

    def set_color(self, color: tuple[int, int, int]) -> None: self._color = color
