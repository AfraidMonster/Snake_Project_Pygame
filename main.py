# import the pygame module, so you can use it
import pygame, sys, time
import random

from pygame import Vector2

# define a main function
def main(): 
    
    class Fruit:
        def __init__(self):
            self.x = random.randint(0, cell_number - 1) 
            self.y = random.randint(0, cell_number - 1) 
            self.pos = Vector2(self.x, self.y)
            # create an x & y position
            # draw fruit
        def draw_fruit(self):
            fruit_rect = pygame.Rect(self.pos.x*cell_size ,self.pos.y*cell_size ,cell_size - 5,cell_size - 5)
            pygame.draw.rect(screen, 'red', fruit_rect)
        
        def randomize(self):
            self.x = random.randint(0, cell_number - 1) 
            self.y = random.randint(0, cell_number - 1) 
            self.pos = Vector2(self.x, self.y)
            
            
     
    class Snake:
        def __init__(self):
            self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
            self.direction = Vector2(1,0)
            self.new_block = False
            
        def draw_snake(self):
            for block in self.body[1:]:
                x_pos = block.x*(cell_size)
                y_pos = block.y*(cell_size)
                block_rect = pygame.Rect(x_pos ,y_pos ,cell_size- 5,cell_size- 5)
                pygame.draw.rect(screen,'yellow', block_rect)
            head_pos_x = self.body[0].x*cell_size
            head_pos_y = self.body[0].y*cell_size
            head_rect = pygame.Rect(head_pos_x, head_pos_y, cell_size - 5, cell_size - 5)
           
            pygame.draw.rect(screen, 'yellow', head_rect)
            
        def move_snake(self):
            if self.new_block == True:
                body_copy = self.body[:]
                body_copy.insert(0,body_copy[0] + self.direction)
                self.body = body_copy[:]
                self.new_block = False
            else:
                body_copy = self.body[:-1]
                body_copy.insert(0,body_copy[0] + self.direction)
                self.body = body_copy[:]   
         
        
        def add_block(self):
            self.new_block = True 
     
    
    class Main:
         def __init__(self):
             self.snake = Snake()
             self.fruit = Fruit()
            
             
             
         def update(self):
             self.snake.move_snake()
             self.check_collision()
             self.check_fail()
             
         def draw_elements(self):
             screen.fill(pygame.Color('black'))
             
             self.fruit.draw_fruit()
             
             self.snake.draw_snake()
             
        
         def check_collision(self):
            if self.fruit.pos == self.snake.body[0]:
                # reposition fruit
                self.fruit.randomize()
                
                # add another block to snake
                self.snake.add_block()
        
         def check_fail(self):
             if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
                 self.game_over()
                 
             for block in self.snake.body[1:]:
                 if block == self.snake.body[0]:
                    self.game_over()
        
         def game_over(self):
            pygame.quit()
            sys.exit()
        
        
                    
                  
            
            
        
        
            
        
        
        
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("Snake Py/logo.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Snake.py")
   

     
    # create a surface grid on screen 
    cell_size = 40
    cell_number = 20
    screen = pygame.display.set_mode(( cell_number*cell_size, cell_number*cell_size))
    
    #Set the game framerate
    clock = pygame.time.Clock()
     
    # define a variable to control the main loop
    running = True
    
    
     
    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 120)
    
    main_game = Main()
    running = False
    while running == False:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                running = True
        print('Press any key to start')
    # main loop
    while running:
         
        #(Event Loop)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == SCREEN_UPDATE:
                main_game.update()
                
            
           
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_UP and main_game.snake.direction != Vector2(0,1 ):
                    main_game.snake.direction = Vector2(0,-1 ) 
                if event.key == pygame.K_DOWN and main_game.snake.direction != Vector2(0,-1 ):
                    main_game.snake.direction = Vector2(0,1 )
                if event.key == pygame.K_LEFT and main_game.snake.direction != Vector2(1,0 ):
                    main_game.snake.direction = Vector2(-1, 0 )
                if event.key == pygame.K_RIGHT and main_game.snake.direction != Vector2(-1,0 ):
                    main_game.snake.direction = Vector2(1, 0 )
       
         
            main_game.draw_elements()
        
       
        
        
       
        pygame.display.update()
        clock.tick(60)
        
        
        
        
        
        
        
        
        
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()