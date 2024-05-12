import pygame


class StartMenu:
    """
    this class handles the main menu

    startLogic(): handles what the buttons in the main menu do
    startDraw(): renders the buttons
    """
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()
        self.font = pygame.font.SysFont('Impact', 30)
        self.controlFont = pygame.font.SysFont('Georgia', 20)
        self.buttonStart = pygame.Rect(self.width // 2 - 100, self.height // 2 - 50, 200, 50)
        self.buttonQuit = pygame.Rect(self.width // 2 - 100, self.height // 2 + 20, 200, 50)
        self.textStart = self.font.render('Start Game', True, (0, 150, 50))

        self.textQuit = self.font.render('Quit', True, (200, 0, 50))
        self.controlText = self.font.render('move: WASD + Arrow Keys | pause: P', True, (70, 70, 70))
        self.clicked = False

    def startLogic(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.buttonStart.collidepoint(event.pos):
                        self.clicked = True
                    elif self.buttonQuit.collidepoint(event.pos):
                        pygame.quit()
                        quit()

    def startDraw(self):
        self.screen.fill((20, 20, 20))
        pygame.draw.rect(self.screen, (0, 0, 0), self.buttonStart)
        pygame.draw.rect(self.screen, (0, 0, 0), self.buttonQuit)

        pinStart = self.buttonStart.centerx - self.textStart.get_width() // 2
        pinQuit = self.buttonQuit.centerx - self.textQuit.get_width() // 2

        self.screen.blit(self.textStart, (pinStart, self.height // 2 - 40))
        self.screen.blit(self.textQuit, (pinQuit, self.height // 2 + 30))
        self.screen.blit(self.controlText, (self.width - self.controlText.get_width() - 10, 10))

        pygame.display.flip()
