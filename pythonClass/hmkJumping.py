import pygame 

pygame.init()

win = pygame.display.set_mode((500,500))

#properties for character
x = 150
y = 250

x2 = 250
y2 = 250

x3 = 350
y3 = 250

radius = 20

vel_x = 10
vel_y = 10

jump = False
jump1 = False
jump2 = False 


run = True 
while run: #main loop (close window)
    pygame.time.delay(100)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed() #variable for key movements
    if keys[pygame.K_LEFT] and x > 0 and x2 > 0 and x3 > 0:  #top is y = 0 bottom is y = 500 left is x = 0 Right is x = 500
        x -= vel_x
        x2 -= vel_x
        x3 -= vel_x
    if keys[pygame.K_RIGHT] and x < 460 and x2 < 460 and x3 <460:
        x += vel_x
        x2 += vel_x
        x3 += vel_x
   
   #jumping effect
    if jump is False and keys[pygame.K_SPACE]:
        jump = True 
    if jump is True:
        y -= vel_y * 3 
        vel_y -= 1
        if vel_y < -10:
            jump = False 
            vel_y = 10

    if jump1 is False and keys[pygame.K_UP]:
        jump1 = True 
    if jump1 is True:
        y2 -= vel_y * 3 
        vel_y -= 1
        if vel_y < -10:
            jump1 = False 
            vel_y = 10

    if jump2 is False and keys[pygame.K_w]:
        jump2 = True 
    if jump2 is True:
        y3 -= vel_y * 3 
        vel_y -= 1
        if vel_y < -10:
            jump2 = False 
            vel_y = 10 
        

    win.fill((0,0,0))  #fill window color
    
    pygame.draw.circle(win,(193,103,91),(int (x),int (y)), radius)
    pygame.draw.circle(win,(0,255,0),(int (x2),int (y2)), radius)
    pygame.draw.circle(win,(0,0,241),(int (x3),int (y3)), radius)

   

    pygame.display.update()



pygame.quit()