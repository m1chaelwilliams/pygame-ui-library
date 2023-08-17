import pygame
from pyuilite.config import *
from pyuilite.uielement import UIElement

class Label(UIElement):
    def __init__(self, 
                 text: str = "", 
                 position: tuple[int, int] = (0,0),
                 position_centered: tuple[int, int] = None,
                 font: str = FONT,
                 fontsize: int = 20, 
                 font_color: pygame.Color = pygame.Color("#ebdbb2"),
                 bg_color: pygame.Color = pygame.Color("#282828"),
                 padding: int = 10,
                 border_radius: int = 0) -> None:
        super().__init__()
        self.value = str(text)
        self.font = font
        self.fontsize = fontsize
        self.font_color = font_color
        self.bg_color = bg_color
        self.padding = padding
        self.border_radius = border_radius

        # generate button
        self.font = pygame.font.Font(self.font, self.fontsize)

        self.text_surface = self.font.render(self.value,
                                             True,
                                             self.font_color)
        self.position = position
        if position_centered:
            self.position = (position_centered[0] - (self.text_surface.get_width()//2),
                             position_centered[1] - (self.text_surface.get_height()//2))

        self.rect = self.text_surface.get_rect(topleft = (self.position[0], self.position[1]))
        self.rect = self.rect.inflate(padding*2, padding*2)

        # states
        self.hovered: bool = False
        self.active_color = self.bg_color
    def update(self, target_pos: tuple[int, int], events: list[pygame.event.Event] = []):
        pass
    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, self.active_color, self.rect, border_radius=self.border_radius)
        surface.blit(self.text_surface, (self.rect.x + self.padding, self.rect.y + self.padding))

class IconLabel(UIElement):
    def __init__(self, 
                 icon: str = None,
                 size: tuple[int, int] = (10, 10), 
                 position: tuple[int, int] = (0,0),
                 position_centered: tuple[int, int] = None,
                 font: str = FONT,
                 fontsize: int = 20, 
                 font_color: pygame.Color = pygame.Color("#ebdbb2"),
                 bg_color: pygame.Color = pygame.Color("#282828"),
                 padding: int = 10,
                 border_radius: int = 0,
                 background: bool = True,
                 on_click = None) -> None:
        super().__init__()
        self.font = font
        self.fontsize = fontsize
        self.font_color = font_color
        self.bg_color = bg_color
        self.padding = padding
        self.border_radius = border_radius
        self.on_click = on_click
        self.background = background

        # generate button
        self.font = pygame.font.Font(self.font, self.fontsize)

        if icon:
            self.surface = pygame.image.load(icon).convert_alpha()
            self.surface = pygame.transform.scale(self.surface, size)
        self.position = position
        if position_centered:
            self.position = (position_centered[0] - (self.surface.get_width()//2),
                             position_centered[1] - (self.surface.get_height()//2))

        self.rect = self.surface.get_rect(topleft = (self.position[0], self.position[1]))
        self.rect = self.rect.inflate(padding*2, padding*2)

        # states
        self.hovered: bool = False
        self.active_color = self.bg_color
    def update(self, target_pos: tuple[int, int], events: list[pygame.event.Event] = []):
        pass
    def draw(self, surface: pygame.Surface):
        if self.background:
            pygame.draw.rect(surface, self.active_color, self.rect, border_radius=self.border_radius)
        surface.blit(self.surface, (self.rect.x + self.padding, self.rect.y + self.padding))