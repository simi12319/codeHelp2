import pygame 

pygame.init()

win = pygame.display.set_mode((600,600))

#object 1 (Top Left)
x = 0
y = 0
width = 40
height = 60
vel = 10

#object 2 (Top Right)
x1 = 500
y1 = 0

#object 3 (Bottom Left)
x2 = 0
y2 = 500

#object 4 (Bottom Right)
x3 = 500
y3 = 500

run = True #main loop (close window)
while run: 
    pygame.time.delay(100)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False

    win.fill((0,0,0))  #fill window color
    
    pygame.draw.rect(win,(142, 158, 108),(x, y, width, height))#draw the rectangles and color for them
    pygame.draw.rect(win,(205, 204, 188),(x1, y1, width, height))
    pygame.draw.rect(win,(205, 205, 233),(x2, y2, width, height))
    pygame.draw.rect(win,(235, 187, 171),(x3, y3, width, height))

    #Top left
    x += vel #moving to intersect 
    y += vel

    #Top Right
    x1 -= vel
    y1 += vel

    #Bottom Left
    x2 += vel
    y2 -= vel

    #Bottom Right
    x3 -= vel
    y3 -= vel

   



pygame.quit()