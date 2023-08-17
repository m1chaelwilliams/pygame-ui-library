import pygame
from pyuilite.uielement import UIElement
from pyuilite.constants import *

class Container(UIElement):
    def __init__(self, 
                 position: tuple,
                 position_centered: tuple = None,
                 bg_color: pygame.Color = pygame.Color("#fb4934"),
                 children: list[UIElement] = [], 
                 direction: str = COLUMN,
                 padding: int = 10,
                 gap: int = 10,
                 centered: bool = True,
                 border_radius: int = 0,
                 background: bool = True,
                 abs_width: int = None,
                 abs_height: int = None) -> None:
        super().__init__()
        
        self.children: list[UIElement] = children
        self.padding = padding
        self.gap = gap
        self.centered = centered
        self.direction = direction
        width = padding*2
        height = padding *2
        self.bg_color = bg_color
        self.border_radius = border_radius
        self.background = background

        if direction == "column":
            width += self.get_max_width()
            for child in self.children:
                child.rect.y = height + position[1] - padding
                child.rect.x = position[0] + padding
                if self.centered:
                    child.rect.centerx = position[0] + (width / 2)
                height += child.rect.height + self.gap
            height -= self.gap
                
        elif direction == "row":
            height += self.get_max_height()
            for child in self.children:
                child.rect.y = position[1] + padding
                child.rect.x = width + position[0] - padding
                if self.centered:
                    child.rect.centery = position[1] + (height / 2)
                width += child.rect.width + self.gap
            width -= self.gap

        if abs_width:
            width = abs_width
        if abs_height:
            height = abs_height

        self.position = position
        if position_centered:
            self.position = (position_centered[0] - (width//2),
                             position_centered[1] - (height//2))
        self.rect = pygame.Rect(self.position[0], self.position[1], width, height)
    def get_max_width(self) -> int:
        m = 0
        for child in self.children:
            if child.rect.width > m:
                m = child.rect.width
        return m
    def get_max_height(self) -> int:
        m = 0
        for child in self.children:
            if child.rect.height > m:
                m = child.rect.height
        return m
    def update(self, target_pos: tuple[int, int], events: list[pygame.event.Event]):
        if self.rect.topleft != self.position:
            
            if self.centered:
                if self.direction == "column":
                    for child in self.children:
                        child.rect.centerx = self.rect.x + (self.rect.width/2)
                        child.rect.y += (self.rect.y - self.position[1])
                elif self.direction == "row":
                    for child in self.children:
                        child.rect.x += (self.rect.x - self.position[0])
                        child.rect.centery = self.rect.y + (self.rect.height/2)
            else:
                for child in self.children:
                    child.rect.x += (self.rect.x - self.position[0])
                    child.rect.y += (self.rect.y - self.position[1])

            self.position = self.rect.topleft

        self.update_children(target_pos, events)
    def draw(self, surface):
        if self.background:
            pygame.draw.rect(surface, self.bg_color, self.rect, border_radius=self.border_radius)
        self.draw_children(surface)
    def draw_children(self, surface: pygame.Surface):
        for child in self.children:
            child.draw(surface)
    def update_children(self, target_pos: tuple[int, int], events: list[pygame.event.Event]):
        for child in self.children:
            child.update(target_pos, events)