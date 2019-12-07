import pygame
import random
import uuid

def gen_testcase():
    x,y = random.randint(100,500), random.randint(100,500)
    print('Image size is {}x{}'.format(x,y))

    surface = pygame.Surface((x,y))
    surface.fill(pygame.Color('white'))

    largest_radius = random.randint(min(x,y)//8, max(x,y)//2)
    print('Largest radius is',largest_radius)

    centerx,centery = random.randint(0, x), random.randint(0, y)

    pygame.draw.circle(surface, pygame.Color('black'), (centerx, centery), largest_radius, 1)

    print('Intended answer is:', (centerx, centery))

    last_circle = 0
    for i in range(largest_radius):
        if random.random()<0.6*(i/largest_radius):
            if i-last_circle > 3:
                last_circle=i
                pygame.draw.circle(surface, pygame.Color('black'), (centerx, centery), i, 1)

    s = 'testcase-{}.png'.format(str(uuid.uuid4()))
    pygame.image.save(surface, s)
    return centerx, centery, s
