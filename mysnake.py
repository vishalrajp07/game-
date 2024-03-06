import pygame
import sys
import random

pygame.init()

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

snake_block = 10
snake_speed = 10
initial_speed = snake_speed

snake = [(100, 50), (90, 50), (80, 50)]
snake_direction = 'RIGHT'

food = (random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10)

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, white, [segment[0], segment[1], snake_block, snake_block])

def draw_food(food):
    pygame.draw.rect(screen, red, [food[0], food[1], snake_block, snake_block])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and not snake_direction == 'DOWN':
        snake_direction = 'UP'
    if keys[pygame.K_DOWN] and not snake_direction == 'UP':
        snake_direction = 'DOWN'
    if keys[pygame.K_LEFT] and not snake_direction == 'RIGHT':
        snake_direction = 'LEFT'
    if keys[pygame.K_RIGHT] and not snake_direction == 'LEFT':
        snake_direction = 'RIGHT'

    if snake_direction == 'UP':
        snake[0] = (snake[0][0], (snake[0][1] - snake_block + height) % height)
    if snake_direction == 'DOWN':
        snake[0] = (snake[0][0], (snake[0][1] + snake_block) % height)
    if snake_direction == 'LEFT':
        snake[0] = ((snake[0][0] - snake_block + width) % width, snake[0][1])
    if snake_direction == 'RIGHT':
        snake[0] = ((snake[0][0] + snake_block) % width, snake[0][1])

    if snake[0][0] == food[0] and snake[0][1] == food[1]:
        food = (random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10)
        snake.append((0, 0))
        snake_speed += 1  # Increase speed when the snake eats food

    if snake[0][0] >= width or snake[0][0] < 0 or snake[0][1] >= height or snake[0][1] < 0:
        # Wrap around the screen
        snake[0] = (snake[0][0] % width, snake[0][1] % height)

    for segment in snake[1:]:
        if snake[0][0] == segment[0] and snake[0][1] == segment[1]:
            pygame.quit()
            sys.exit()

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    screen.fill(black)
    draw_snake(snake)
    draw_food(food)

    pygame.display.flip()
    pygame.time.Clock().tick(snake_speed)
