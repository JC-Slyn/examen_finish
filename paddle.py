import pygame
from settings import *

class Paddle:

    def __init__(self, x, y):

        self.rect = pygame.Rect(
            x,
            y,
            PADDLE_WIDTH,
            PADDLE_HEIGHT
        )

    def move(self, up=True):

        if up:
            self.rect.y -= PADDLE_SPEED

        else:
            self.rect.y += PADDLE_SPEED

        # Limitar dentro de pantalla
        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def draw(self, screen):

        # Sombra
        shadow_rect = self.rect.copy()

        shadow_rect.x += 4
        shadow_rect.y += 4

        pygame.draw.rect(
            screen,
            (60, 60, 60),
            shadow_rect,
            border_radius=6
        )

        # Paddle principal
        pygame.draw.rect(
            screen,
            WHITE,
            self.rect,
            border_radius=6
        )

        # Borde brillante
        pygame.draw.rect(
            screen,
            (180, 180, 180),
            self.rect,
            3,
            border_radius=6
        )