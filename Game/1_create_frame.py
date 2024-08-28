#pip install pygame
import pygame   

pygame.init()

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption = "Hak Game"

running = True
bacgground = pygame.image.load()

while running:
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    
    screen.blit(background, (0,0))

pygame.quit()