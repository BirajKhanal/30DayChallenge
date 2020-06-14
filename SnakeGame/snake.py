import random
import pygame
import time

#window creation
pygame.init()
clock = pygame.time.Clock()

#required colors
orange = (255, 123, 7)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Display window size
display_width = 600
display_height = 400
dis = pygame.display.set_mode((display_width, display_height))

#snake structure and position
snake_block = 10
snake_speed = 15
snake_list = []

def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, orange, [x[0], x[1], snake_block, snake_block])

#main
def snakegame():
    game_over = False
    game_end = False

    #co-ordinates of the snake
    x1 = display_width / 2
    y1 = display_height / 2

    #when the snake moves
    x1_change = 0
    y1_change = 0
    
    # snake length
    snake_list = []
    length_of_snake = 1

    # food co-ordinates
    foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0

    while not game_over:
        
        while game_end == True:
            
            # to replay game
            font_style = pygame.font.SysFont("mononoki", 20)
            msg = font_style.render("You lost, wanna play again? Press f", True, red)
            dis.blit(msg, [display_width / 4, display_height / 3])

            # display score
            score = length_of_snake - 1
            score_font = pygame.font.SysFont("mononoki", 35)
            value = score_font.render("Your Score: " + str(score), True, green)
            dis.blit(value, [display_width / 3, display_height / 5])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        snakegame()

                if event.type == pygame.QUIT:
                    game_over = True # game window still open
                    game_end = False # game has been ended

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_w:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_s:
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_end = True

        # updated co-ordinates with the changed position
        x1 += x1_change
        y1 += y1_change

        dis.fill(black)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        pygame.display.update()

        # game ends when the length of the snake exceeds
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # game ends when snake hits itself
        for x in snake_list[:-1]:
            if x == snake_head:
                game_end = True

        snake(snake_block, snake_list)
        pygame.display.update()

        # when snake hit food, snake size increase
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
        
        clock.tick(snake_speed)

    pygame.quit()
    quit()


snakegame()
