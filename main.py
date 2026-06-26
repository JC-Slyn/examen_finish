import pygame
from settings import *
from paddle import Paddle
from ball import Ball

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Mejorado")

font = pygame.font.SysFont(None, 50)
small_font = pygame.font.SysFont(None, 30)

# Jugadores
left_paddle = Paddle(30, HEIGHT // 2 - 50)
right_paddle = Paddle(WIDTH - 50, HEIGHT // 2 - 50)

# Pelota
ball = Ball()

# Puntajes
left_score = 0
right_score = 0

# Estados del juego
game_started = False
paused = False
winner = None

running = True

while running:

    # Eventos
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            # Iniciar juego
            if event.key == pygame.K_SPACE:
                game_started = True

            # Pausa
            if event.key == pygame.K_ESCAPE:
                paused = not paused

            # Reiniciar juego
            if event.key == pygame.K_r:

                left_score = 0
                right_score = 0

                winner = None
                game_started = False

                ball.reset()

    # Fondo
    screen.fill(BLACK)

    # Pantalla inicio
    if not game_started:

        title = font.render("PONG", True, WHITE)

        text = small_font.render(
            "Presiona ESPACIO para iniciar",
            True,
            WHITE
        )

        screen.blit(title, (WIDTH // 2 - 70, 150))
        screen.blit(text, (WIDTH // 2 - 170, 250))

        pygame.display.update()
        continue

    # Pantalla pausa
    if paused:

        pause_text = font.render("PAUSA", True, WHITE)

        info_text = small_font.render(
            "ESC para continuar",
            True,
            WHITE
        )

        screen.blit(
            pause_text,
            (WIDTH // 2 - 80, HEIGHT // 2 - 40)
        )

        screen.blit(
            info_text,
            (WIDTH // 2 - 110, HEIGHT // 2 + 20)
        )

        pygame.display.update()
        continue

    # Pantalla ganador
    if winner:

        win_text = font.render(f"{winner} GANA", True, WHITE)

        restart_text = small_font.render(
            "Presiona R para reiniciar",
            True,
            WHITE
        )

        screen.blit(win_text, (WIDTH // 2 - 170, 200))
        screen.blit(restart_text, (WIDTH // 2 - 150, 280))

        pygame.display.update()
        continue

    # Teclas
    keys = pygame.key.get_pressed()

    # Jugador izquierda
    if keys[pygame.K_w]:
        left_paddle.move(True)

    if keys[pygame.K_s]:
        left_paddle.move(False)

    # Jugador derecha
    if keys[pygame.K_UP]:
        right_paddle.move(True)

    if keys[pygame.K_DOWN]:
        right_paddle.move(False)

    # Movimiento pelota
    ball.move()

    # Colisiones
    ball.collide(left_paddle)
    ball.collide(right_paddle)

    # Punto jugador derecho
    if ball.x < 0:

        right_score += 1
        ball.reset()

    # Punto jugador izquierdo
    if ball.x > WIDTH:

        left_score += 1
        ball.reset()

    # Verificar ganador
    if left_score >= 5:
        winner = "IZQUIERDA"

    if right_score >= 5:
        winner = "DERECHA"

    # Dibujar jugadores
    left_paddle.draw(screen)
    right_paddle.draw(screen)

    # Dibujar pelota
    ball.draw(screen)

    # Línea central punteada
    for i in range(0, HEIGHT, 30):

        pygame.draw.rect(
            screen,
            GRAY,
            (WIDTH // 2 - 5, i, 10, 20)
        )
##hola JOSEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
    # Puntajes
    left_text = font.render(str(left_score), True, WHITE)

    right_text = font.render(str(right_score), True, WHITE)

    screen.blit(left_text, (WIDTH // 4, 20))

    screen.blit(right_text, (WIDTH * 3 // 4, 20))

    pygame.display.update()

pygame.quit()
