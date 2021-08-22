import pygame 
import os

pygame.init()
win_height = 400
win_width = 800
i = 0

win = pygame.display.set_mode((win_width,win_height)) #drawing out window 


#images used for loading hero 
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


#bullet images
bullet_img = pygame.image.load(os.path.join("Assets/Bullets", "light_bullet.png")) #loading bullet image
bi = pygame.transform.scale(bullet_img, (15, 15)) #sizing bullet image

bckg = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Background.png")), (win_width, win_height))#loaded bckg image
bg = pygame.transform.scale(bckg,(1000,500)) #sizing the bckg image 




class Hero: 
    def __init__(self,x,y): #variables for walking of the characters
        self.x = x
        self.y = y
        self.vel_x = 10
        self.vel_y = 10
        self.face_right = True
        self.face_left = False
        self.stepIndex = 0
        self.jump = False
        self.bullets = []
        
        #variable used in jump of the character
        self.jump = False 
        self.cool_down_count = 0

    #first method
    def move_hero (self, keys):
        if(keys[pygame.K_RIGHT]) and self.x <= win_width - 62: 
            self.x += self.vel_x
            self.face_right = True 
            self.face_left = False 
        elif(keys[pygame.K_LEFT]) and self.x >= 0:
            self.x -= self.vel_x
            self.face_right = False
            self.face_left = True 

        else: 
            self.step_index = 0 #repeat the images 

    #second method 
    #drawing the characters
    def draw(self,win):
        if self.step_index >= 9:
            self.step_index = 0
        if self.face_left: 
            win.blit(left[self.step_index],(self.x,self.y))
            self.step_index += 1
        if self.face_right: 
            win.blit(right[self.step_index],(self.x,self.y))
            self.step_index += 1
    
    #third method
    def jump_motion(self,keys):
        if keys[pygame.K_SPACE]and self.jump is False: 
            self.jump = True
        if self.jump:
            self.y -= self.vel_y * 4
            self.vel_y -= 1
        if self.vel_y <- 10:
            self.jump = False          
            self.vel_y = 10 

    #fourth method
    def direction(self):
        if self.face_right:
            return 1
        if self.face_left:
            return -1

    #fifth method
    def shoot_bullet(self):
        self.cool_down()
        if (keys[pygame.K_v] and self.cool_down_count == 0):
            #creating bullet instances when 'V' key is pressed 
            bullet = Bullet(self.x, self.y, self.direction())
            self.bullets.append(bullet)
            self.cool_down_count = 1
        for bullet in self.bullets:
            bullet.move_bullet()
            if bullet.off_screen():
                self.bullets.remove(bullet) 

    def cool_down(self):
        if self.cool_down_count >= 10:
            self.cool_down_count = 0
        elif self.cool_down_count > 0:
            self.cool_down_count += 1


class Bullet:
    def __init__(self, x, y, direction):
        self.x = x + 15
        self.y = y + 25
        self.direction = direction

    def draw_bullet(self):
        win.blit(bi, (self.x,  self.y))

    def move_bullet(self):
        if self.direction == 1:
            self.x += 15
        if self.direction == -1:
            self.x -= 15
    
    def off_screen(self): #when bullet goes offscreen
      return not(self.x >= 0 and self.x <= win_width)
      

#drawing the game
def draw_game():
    win.fill((0,0,0)) #filling canvas color
    win.blit(bckg,(0,0))
    player.draw(win)
    for bullet in player.bullets:
        bullet.draw_bullet() #drawing bullet
    pygame.time.delay(30)
    pygame.display.update()

#creating instance of objects in hero (1 instance --> 1 hero)
player = Hero(250,290)

 #creating main loop and calling all the functions
run = True 
while run: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False

    #input 
    keys = pygame.key.get_pressed()
    
    #calling the function movement
    player.move_hero(keys)
    player.jump_motion(keys)
    player.shoot_bullet()
    draw_game()
   

