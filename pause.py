import pygame


class PauseMenu:
    """
    this class handles the pause menu

    pauseLogic(): handles what the buttons in the pause menu do
    pauseDraw(): renders the pause menu buttons
    """
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()
        self.font = pygame.font.SysFont('Impact', 30)
        self.buttonResume = pygame.Rect(self.width // 2 - 100, self.height // 2 - 50, 200, 50)
        self.buttonRestart = pygame.Rect(self.width // 2 - 100, self.height // 2 + 20, 200, 50)
        self.buttonExit = pygame.Rect(self.width // 2 - 100, self.height // 2 + 90, 200, 50)
        self.textResume = self.font.render('Resume', True, (0, 50, 150))
        self.textRestart = self.font.render('Restart', True, (0, 150, 50))
        self.textExit = self.font.render('Exit', True, (200, 0, 50))
        self.clicked = False

    def pauseLogic(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.buttonResume.collidepoint(event.pos):
                        self.clicked = True
                    elif self.buttonRestart.collidepoint(event.pos):
                        pass
                    elif self.buttonExit.collidepoint(event.pos):
                        pass

    def pauseDraw(self):
        self.screen.fill((30, 30, 30))
        pygame.draw.rect(self.screen, (0, 0, 0), self.buttonResume)
        pygame.draw.rect(self.screen, (0, 0, 0), self.buttonRestart)
        pygame.draw.rect(self.screen, (0, 0, 0), self.buttonExit)

        pinResume = self.buttonResume.centerx - self.textResume.get_width() // 2
        pinRestart = self.buttonRestart.centerx - self.textRestart.get_width() // 2
        pinExit = self.buttonExit.centerx - self.textExit.get_width() // 2

        self.screen.blit(self.textResume, (pinResume, self.height // 2 - 40))
        self.screen.blit(self.textRestart, (pinRestart, self.height // 2 + 30))
        self.screen.blit(self.textExit, (pinExit, self.height // 2 + 100))
