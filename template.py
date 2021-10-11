import pygame
# --Global Constant

# -- Color 
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50, 255)
YELLOW = (255,255,0)
RED = (255,50,50)

# -- Initialize pygame
pygame.init()

# -- Blank Screen
size = (640, 480)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("My window")
# -- Exit game flag set to False
done = False
# -- Manages how fast screen refresh
clock = pygame.time.Clock()

### -- Game loop
while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #Endif
    #Next event
    #--Game logic goes after this comment
    
    # -- Screen background is BLACK
    screen.fill(BLACK)

    # -- Draw here
    # screen, [red, blue, green], (left, top, width, height))
    pygame.draw.rect(screen,RED,(220,100,150,150))

    # circle(surface, color, center, radius, width)
    pygame.draw.circle(screen,YELLOW,(40,40),40,2)

    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)

#Endwhile
pygame.quit()