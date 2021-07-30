import pygame
import time
import random
import pickle
 
pygame.init()
 
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
gray = (128, 128, 128)
 
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

BLOCK = 50
 
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Eyes')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 15
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
 
def Your_score(score):
    value = score_font.render("Score: " + str(score), True, GREEN)
    SCREEN.blit(value, [0, 0])
 
 
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(SCREEN, WHITE, [x[0], x[1], snake_block, snake_block])
 
 
 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = SCREEN_WIDTH / 2
    y1 = SCREEN_HEIGHT / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, SCREEN_WIDTH - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, SCREEN_HEIGHT - snake_block) / 10.0) * 10.0

    def askSave():
        ask = input("Do you want to save?\n--> ").upper()
        if ask == "Y" or ask == "YES":
            Save = Player(PlayerIG.name)
            #date = time.strftime("%d %b %Y", time.localtime())
            pickle.dump(Save, open("Save File", "wb"))
        elif ask == "N" or ask == "NO":
            print("Okay, maybe next time!")
            return
        else:
            print("Sorry, that does not compute with me! Please try again!")
            askSave()
 
    while not game_over:
 
        while game_close == True:
            SCREEN.fill(WHITE)
            
            Your_score(Length_of_snake - 1)
            pygame.display.flip()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= SCREEN_WIDTH or x1 < 0 or y1 >= SCREEN_HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        SCREEN.fill(BLACK)
        pygame.draw.rect(SCREEN, GREEN, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        if len(snake_List) > 3:

            pygame.draw.rect(SCREEN, pygame.Color('gray'), (0, 0, BLOCK * 3, BLOCK))
            pygame.draw.rect(SCREEN, pygame.Color('gray'), (0, 20, BLOCK * 3, BLOCK))
            pygame.draw.rect(SCREEN, pygame.Color('gray'), (0, 50, BLOCK, BLOCK * 4))
            pygame.draw.rect(SCREEN, pygame.Color('gray'), (70, 80, BLOCK, BLOCK * 4))
            # левый нижний угольник
            pygame.draw.rect(SCREEN, pygame.Color('gray'), (440, 450, BLOCK * 2, BLOCK))
            pygame.draw.rect(SCREEN, pygame.Color('gray'), (380, 400, BLOCK, BLOCK))
            # правый верхний угольник
            pygame.draw.rect(SCREEN, pygame.Color('gray'), (370, 150, BLOCK * 2, BLOCK))
            pygame.draw.rect(SCREEN, pygame.Color('gray'), (230, 200, BLOCK, BLOCK))
            # правый нижний угольник
            pygame.draw.rect(SCREEN, pygame.Color('gray'), (345, 450, BLOCK * 2, BLOCK))
            pygame.draw.rect(SCREEN, pygame.Color('gray'), (570, 500, BLOCK, BLOCK))

         
 
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)


        pygame.display.flip()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, SCREEN_WIDTH - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, SCREEN_HEIGHT - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
        while len(snake_List) > 3:
            if x1 == 0 and y1 == 20:
                game_over == True
            if x1 == 0 and y1 == 50:
                game_over == True
            if x1 == 70 and y1 == 80:
                game_over == True
            if x1 == 440 and y1 == 450:
                game_over == True
            if x1 == 380 and y1 == 400:
                game_over == True
            if x1 == 370 and y1 == 150:
                game_over == True
            if x1 == 230 and y1 == 200:
                game_over == True
            if x1 == 345 and y1 == 450:
                game_over == True
            if x1 == 570 and y1 == 500:
                game_over == True
 
        clock.tick(snake_speed)


 
    pygame.quit()
    quit()
  
 
gameLoop()
