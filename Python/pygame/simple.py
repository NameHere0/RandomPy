import pygame
from time import sleep

pygame.init()

# create a game window
clock = pygame.time.Clock()
back = (255, 255, 255)  # background color
mw = pygame.display.set_mode((500, 500))  # main window
mw.fill(back)


class Text:
    def __init__(self, x=0, y=0, width=10, height=10, color=(200, 200, 255)):
        self.rect = pygame.Rect(x, y, width, height)

        self.color = pygame.Color(200, 200, 255)

    def setText(self, text: str, fsize=75, textColor=(10, 10, 10)):
        self.text = text
        self.image = pygame.font.Font(None, fsize).render(text, True, textColor)

    def draw(self, shiftX=10, shiftY=10):
        pygame.draw.rect(mw, self.color, self.rect)
        mw.blit(self.image, (self.rect.x + shiftX, self.rect.y + shiftY))


randomCard = Text(128, 100, 290, 70)
randomCard.setText("Press A")

randomCard2 = Text(128, 200, 290, 70)
randomCard2.setText("Not active")

exitCard = Text(128, 300, 290, 70)
exitCard.setText("Not active")

randomCard.draw()
randomCard2.draw()
exitCard.draw()

running = True

shown1 = False
shown2 = False

while running:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and not shown1:
                randomCard2.setText("Press B")
                shown1 = True
            if event.key == pygame.K_b and shown1:
                exitCard.setText("Press R")
            if event.key == pygame.K_r:  # Exit
                exitCard.setText("bye")
                shown2 = True
                exitCard.draw()
            if shown2:
                sleep(2)
                running = False

            randomCard.draw()
            randomCard2.draw()
            exitCard.draw()
    clock.tick(60)
