import pygame, random

def draw_grid(screen):
    #draw vertical lines
    for i in range(0, 640, 32):
        pygame.draw.line(screen,(0,0,0), (i,0), (i, 512))
    #draw horizontal lines
    for j in range(0, 512, 32):
        pygame.draw.line(screen, (0,0,0), (0,j), (640, j))

def move_mole(screen, image, coord):
    screen.blit(image, image.get_rect(topleft = coord))

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        coordinates = (random.randrange(0, 640, 32), random.randrange(0, 512, 32)) #create mole location
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (coordinates[0] <= event.pos[0] <= coordinates[0]+31) and (coordinates[1] <= event.pos[1] <= coordinates[1]+31):
                        coordinates = (random.randrange(0,640,32), random.randrange(0,512,32)) #generate new mole location
            screen.fill("light green")
            draw_grid(screen)
            move_mole(screen, mole_image, coordinates) #places mole on screen
            pygame.display.flip()
            clock.tick(60)
            screen.blit(mole_image, mole_image.get_rect(topleft=(32, 32)))
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
