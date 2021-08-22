import pygame 
import os

pygame.init()

win = pygame.display.set_mode((1000,500))

bg_img = pygame.image.load(os.path.join("Assets", "StoresBackground.png"))
bg = pygame.transform.scale(bg_img,(1000,500))
width = 1000
i = 0

run = True #main loop (close window)
while run: 
    #pygame.time.delay(100)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False

    win.fill((0,0,0))

    #creating a contious background
    win.blit(bg,(i,0)) #first bckgd

    win.blit(bg,(width + i,0)) #sec bckgd

    if i == -width: #repeating bckgd
        win.blit(bg,(width + i,0))
        i = 0

    i -= 2 #speed of moving bckgd

    pygame.display.update()