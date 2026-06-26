import pygame
import random
from settings import *

#definiendo clases
class Ball:

    def __init__(self):
        self.reset()

    def reset(self):

        # Posición inicial
        self.x = WIDTH // 2
        self.y = HEIGHT // 2

        # Dirección aleatoria
        self.dx = BALL_SPEED * random.choice((1, -1))
        self.dy = BALL_SPEED * random.choice((1, -1))

    def move(self):

        self.x += self.dx
        self.y += self.dy

        # Rebote arriba
        if self.y - BALL_RADIUS <= 0:
            self.dy *= -1

        # Rebote abajo
        if self.y + BALL_RADIUS >= HEIGHT:
            self.dy *= -1

    def draw(self, screen):

        pygame.draw.circle(
            screen,
            WHITE,
            (self.x, self.y),
            BALL_RADIUS
        )

    def collide(self, paddle):

        paddle_rect = paddle.rect

        # Colisión izquierda
        if paddle_rect.collidepoint(
            self.x - BALL_RADIUS,
            self.y
        ):

            # Rebote y aumento velocidad
            self.dx *= -1.05

        # Colisión derecha
        if paddle_rect.collidepoint(
            self.x + BALL_RADIUS,
            self.y
        ):

            # Rebote y aumento velocidad
            self.dx *= -1.05