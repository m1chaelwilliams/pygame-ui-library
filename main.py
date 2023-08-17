import pygame
import sys
from pyuilite import *
from pyuilite.constants import *

# this is the test file

SCRW = 1280
SCRH = 720
TILESIZE = 50
FPS = 60

pygame.init()
screen = pygame.display.set_mode((SCRW, SCRH))
clock = pygame.time.Clock()

def say_hello():
    print('hello world')
def say_my_name(name):
    print(f'hello, {name}')

toggle_background_button = TextButton(text="toggle_background")

sidebar = Container(position=(0,0),
                    children=[
                        IconLabel("tinyblock.png", size=(100, 100), background=None),
                        TextButton(text="Click me!", on_click=lambda: print('clicking me!')),
                        toggle_background_button,
                        TextButton(text="Random Text"),
                        Label(text="Label", fontsize=30),
                        TextButton(text="Random Text"),
                        TextButton(text="Random Text"),
                        TextButton(text="Random Text"),
                        TextButton(text="Random Text"),
                    ],
                    padding=0)

right_sidebar = Container(position=(0,0),
                    children=[
                        TextButton(text="Random Text"),
                        TextButton(text="Random Text"),
                        TextButton(text="Random Text"),
                        Label(text="Label", fontsize=30),
                        TextButton(text="Random Text"),
                        TextButton(text="Random Text"),
                        TextButton(text="Random Text"),
                        TextButton(text="Random Text"),
                    ],
                    padding=10,
                    bg_color=pygame.Color("green"),
                    )


view = Container(position=(0,0),
                 children=[
                     sidebar,
                     Container((0,0),
                               children=[
                                   Label(text="Label")
                               ],
                               bg_color=pygame.Color("lightblue"),
                               
                               abs_height=700,
                               border_radius=15,
                               centered=False),
                    right_sidebar
                 ],
                 direction=ROW,
                 centered=False,
                 abs_width=SCRW,
                 abs_height=SCRH)

def bg_toggle():
    if view.bg_color.r > 0:
        view.bg_color.r = 0
    else:
        view.bg_color.r = 255

toggle_background_button.on_click = bg_toggle

while True:
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # update logic
    # container.update_children(pygame.mouse.get_pos(), events=events)
    # button.update(pygame.mouse.get_pos(), events=events)
    view.update(pygame.mouse.get_pos(), events=events)

    # draw logic
    screen.fill('#282828')
    view.draw(screen)
    # container.draw_children(screen)
    # button.draw(screen)

    pygame.display.update()
    clock.tick(FPS)