import pygame
import sys
from settings import * 
from food import Food 
from snake import Snake 
from a_star import * 
import time

pygame.init()

def game_over():
    font = pygame.font.SysFont('arial', 35)
    game_over_surface = font.render('Game Over! Press R to Restart or Q to Quit', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (width / 2, height / 4)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

def get_direction(current, next):
    if next[0] - current[0] > 0:
        return pygame.K_RIGHT
    elif next[0] - current[0] < 0:
        return pygame.K_LEFT
    elif next[1] - current[1] > 0:
        return pygame.K_DOWN
    elif next[1] - current[1] < 0:
        return pygame.K_UP

def main():
    snake = Snake()
    food = Food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        safe_path = find_safe_path(snake, food, snake.body[-1])
        if safe_path and len(safe_path) > 1:
            next_move = safe_path[1]
            snake.direction = get_direction(snake.body[0], next_move)
        else:
            # If no safe path is found, attempt to move in a default direction
            # to prevent immediate game over
            possible_moves = [(0, -cell_size), (0, cell_size), (-cell_size, 0), (cell_size, 0)]
            for move in possible_moves:
                potential_head = (snake.body[0][0] + move[0], snake.body[0][1] + move[1])
                if (0 <= potential_head[0] < width and 0 <= potential_head[1] < height and 
                        potential_head not in snake.body[1:]):
                    snake.direction = get_direction(snake.body[0], potential_head)
                    break

        snake.move()

        if snake.body[0] == food.position:
            snake.grow()
            food.position = food.random_position()

        if snake.check_collision():
            game_over()

        screen.fill(black)
        snake.draw()
        food.draw()
        pygame.display.flip()
        clock.tick(speed)

if __name__ == '__main__':
    main()

