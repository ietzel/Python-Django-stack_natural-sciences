import pygame

pygame.init()

screen = pygame.display.set_mode((2048,1024))

clock = pygame.time.Clock()

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    screen.fill("red")  

    pygame.display.flip()   
    clock.tick(240)         