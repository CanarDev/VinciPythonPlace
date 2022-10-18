import pygame
import random

pygame.init()
size = (400,400)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

BLACK  = [0, 0, 0]
WHITE  = [255, 255, 255]
SILVER = [192, 192, 192]
GOLD   = [255, 223, 0]
RED    = [255, 0, 0]
colour_list = [WHITE, SILVER, GOLD, RED]
colour = random.choice(colour_list)

snow_list = []
for i in range(100):
    x = random.randrange(0, 400)
    y = random.randrange(0, 400)
    snow_list.append((WHITE, [x, y]))

def recolour_snowflake(snowflake):
    colour = random.choice(colour_list)
    return (colour, snowflake[1])

def animate_snowflake(snowflake):
    x, y = snowflake[1]
    y += random.randrange(1,3)
    if y > 400:
        x, y = (random.randrange(0, 400), random.randrange(-50, -10))
    return (snowflake[0], [x, y])

count = 0
done = False
while not done:

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # change the color of the snow flakes
    if count == 5:
        snow_list = list(map(recolour_snowflake, snow_list))
        count = 0
    count += 1

    # Process each snow flake in the list
    snow_list = list(map(animate_snowflake, snow_list))

    # Set the screen background
    screen.fill(BLACK)

    # draw the snow flakes
    for snow in snow_list:
        pygame.draw.circle(screen, *snow, 2)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    clock.tick(20)