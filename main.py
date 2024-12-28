import pygame
import random

# Initialize pygame
pygame.init()

# Custom event IDs for color change events
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2

# Define basic colors using pygame.Color
# Background colors
BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')

# Sprite colors
YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')


# Sprite class representing the moving object
class Sprite(pygame.sprite.Sprite):

    #Constructor method
    def __init__(self, color, width, height):
        # Call to the parent class (Sprite) constructor
        super().__init__()
        # Get the sprite's surface with simensions and color
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # Get the sprite's rect defining its position and size
        self.rect = self.image.get_rect()
        # Set initial velocity with random direction
        self.velocity = [random.choice([-1, 1]),random.choice([-1, 1])]

    # Method to update the sprite's position
    def update(self):
        # Move the sprite by its velocity
        self.rect.move_ip(self.velocity)
        # Flag to track if the sprite hits a boundary
        boundary_hit = False
        # Check for collision with left or rightboundaries and reverse direction
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]

        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True

        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))

    # Method to change the sprite's color 
    def change_color(self):
        self.image.fill(random.choice([YELLOW, MAGENTA, ORANGE, WHITE]))
                        
# Function to change the background color
def change_background_color():
  global bg_color
  bg_color = random.choice([BLUE, LIGHTBLUE, DARKBLUE])
# Create a group to hold the sprite
all_sprites_list = pygame.sprite.Group()
sp1 = Sprite(WHITE, 20, 30)
sp1.rect.x = random.randint(0,480)
sp1.rect.y = random.randint(0,370)
all_sprites_list.add(sp1)
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Colorful bounce")
bg_color = BLUE
screen.fill(bg_color)

exit = False
clock = pygame.time.Clock()

while not exit:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
         exit = True
      elif event.type ==  SPRITE_COLOR_CHANGE_EVENT:
       sp1.change_color()
      elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
        change_background_color()
    all_sprites_list.update()
    screen.fill(bg_color)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(240)

pygame.quit()   
