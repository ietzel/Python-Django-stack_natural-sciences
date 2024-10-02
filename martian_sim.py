import pygame

pygame.init()

screen = pygame.display.set_mode((2048,1024))

clock = pygame.time.Clock()

class Rover:
  def __init__(self, name, image):
    self.name = name
    self.image = image

r1 = Rover("Sixwheeler", "1.jpg")
r2 = Rover("Flier", "2.jpg")
r3 = Rover("Slitherer", "3.jpg")
r4 = Rover("Hopper", "4.jpg")
r5 = Rover("Crawler", "5.jpg")
r6 = Rover("6", "6.jpg")

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    screen.fill("red")  

    pygame.display.flip()   
    clock.tick(40)         
