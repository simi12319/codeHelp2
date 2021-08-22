import pygame 
import os

pygame.init()

win = pygame.display.set_mode((500,500))

#loading images for characters

standing = pygame.image.load(os.path.join("Assets/Hero", "standing.png"))
left = [pygame.image.load(os.path.join("Assets/Hero", "L1.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L2.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L3.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L4.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L5.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L6.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L7.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L8.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L9.png"))]

right = [pygame.image.load(os.path.join("Assets/Hero", "R1.png")),
        pygame.image.load(os.path.join("Assets/Hero", "R2.png")),
        pygame.image.load(os.path.join("Assets/Hero", "R3.png")),
        pygame.image.load(os.path.join("Assets/Hero", "R4.png")),
        pygame.image.load(os.path.join("Assets/Hero", "R5.png")),
        pygame.image.load(os.path.join("Assets/Hero", "R6.png")),
        pygame.image.load(os.path.join("Assets/Hero", "R7.png")),
        pygame.image.load(os.path.join("Assets/Hero", "R8.png")),
        pygame.image.load(os.path.join("Assets/Hero", "R9.png"))]

#properties for character
x = 250
y = 250
vel = 10

#variables for moving character towards left and right
move_left = False
move_right = False
step_index = 0

def draw_characters():
    global step_index 
    win.fill((0,0,0)) #draw canvas
    if step_index >= 9:
        step_index = 0
    if move_left:
        win.blit(left[step_index],(x,y)) #shows image in the canvas (adding left)
        step_index += 1
    elif move_right:
        win.blit(right[step_index],(x,y))
        step_index += 1
    else:
        win.blit(standing,(x,y))


run = True 
while run: #main loop (close window)
 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False
    draw_characters()
    
    keys = pygame.key.get_pressed() #variable for key movements
    if keys[pygame.K_LEFT] and x > 0:  #top is y = 0 bottom is y = 500 left is x = 0 Right is x = 500
        x -= vel
        move_left = True
        move_right = False
    elif keys[pygame.K_RIGHT] and x < 460:
        x += vel
        move_right = True
        move_left = False
    else:
        move_left = False
        move_right = False
        step_index = 0
     

    
    pygame.time.delay(30)
    pygame.display.update()
    


