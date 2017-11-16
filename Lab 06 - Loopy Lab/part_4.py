import pygame
pygame.init()
size = (800, 800)
screen = pygame.display.set_mode(size)

GREEN = (50, 205, 50)
done = False
while not done:
    y_offset = -4
    for x in range(1, 100):
        y_offset = y_offset + 10
        x_offset = 6
        for y in range(1, 100):
            pygame.draw.circle(screen, GREEN, [x_offset, y_offset], 3, 0)
            x_offset = x_offset + 10

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
pygame.quit()            
            
