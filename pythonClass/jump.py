import pygame 

pygame.init()

win = pygame.display.set_mode((500,500))


#properties for character
x = 250
y = 250
width = 40
height = 60 
vel_x = 10
vel_y = 10
jump = False 


run = True 
while run: #main loop (close window)
    pygame.time.delay(100)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed() #variable for key movements
    if keys[pygame.K_LEFT] and x > 0:  #top is y = 0 bottom is y = 500 left is x = 0 Right is x = 500
        x -= vel_x
    if keys[pygame.K_RIGHT] and x < 460:
        x += vel_x
   
   #jumping effect
    if jump is False and keys[pygame.K_SPACE]:
        jump = True 
    if jump is True:
        y -= vel_y * 3 
        
        vel_y -= 1
        if vel_y < -10:
            jump = False 
            vel_y = 10 
        

    win.fill((0,0,0))  #fill window color
    
    pygame.draw.rect(win,(0,255,0),(x,y,width,height))
   

    pygame.display.update()



pygame.quit()