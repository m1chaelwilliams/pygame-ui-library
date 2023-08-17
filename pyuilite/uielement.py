import pygame

class UIElement:
    def __init__(self) -> None:
        self.rect: pygame.Rect = None
    def update(self, *args, **kwargs):
        pass
    def draw(self, *args, **kwargs):
        pass