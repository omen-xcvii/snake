import pygame
import random
import time
from pause import PauseMenu
import os
from typing import List, Tuple, Optional


class Game:
    """
    this class sets up the elements and methods regarding Snake's logic

    readScore(): grabs the personal best score from a txt file
    updateBest(): overwrites the score in the txt file with a higher score
    showScore(): displays the score in real time, also displays the best as a score to beat
    gameOver(): handles what happens if the snake hits a wall or itself, and calls updateBest()
    reset(): resets all game elements to a new game without exiting and relaunching
    restart(): begins a new game from the pause menu
    snakeLoop(): handles all the snake's movements and collisions

    """

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.playHeight: int = screen.get_height() - 50
        self.playWidth: int = screen.get_width()
        self.snakePos: List[int] = [80, 50]
        self.snakeSpeed: int = 10
        self.snakeBody: List[List[int]] = [[80, 50], [70, 50]]
        self.orbPos: List[int] = [random.randrange(1, (self.playWidth // 10)) * 10,
                       random.randrange(1, (self.playHeight // 10)) * 10]
        self.orb: bool = True
        self.score: int = 0
        self.paused: bool = False
        self.pause = PauseMenu(screen)
        self.direc: str = 'RIGHT'
        self.nextDirec: Optional[str] = None
        self.bestFile: str = 'best.txt'
        self.best: int = self.readScore(self.bestFile)

    def readScore(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                try:
                    return int(file.read().strip())
                except ValueError:
                    return 0
        else:
            return 0

    def updateBest(self, newScore, filename, score):
        if newScore > score:
            with open(filename, 'w') as file:
                file.write(str(newScore))
            return newScore
        return score

    def showScore(self):
        boxRect = pygame.Rect(0, 0, self.playWidth, 50)
        pygame.draw.rect(self.screen, (0, 0, 0), boxRect)
        font = pygame.font.SysFont('Impact', 30)
        scoreText = font.render('SCORE: ' + str(self.score), True, (0, 150, 250))
        bestText = font.render('BEST: ' + str(self.best), True, (255, 215, 0))
        scoreRect = scoreText.get_rect(left=10, centery=25)
        bestRect = bestText.get_rect(right=self.playWidth - 10, centery=25)
        self.screen.blit(scoreText, scoreRect)
        self.screen.blit(bestText, bestRect)

    def gameOver(self):
        self.best = self.updateBest(self.score, self.bestFile, self.best)

        fontScore = pygame.font.SysFont('Impact', 50)
        fontRe = pygame.font.SysFont('Impact', 35)

        scoreText = fontScore.render('SCORE: ' + str(self.score), True, 'red')
        bestText = fontScore.render('BEST: ' + str(self.best), True, 'orange')

        scoreRect = scoreText.get_rect(center=(self.playWidth / 2, self.playWidth / 4))
        bestRect = bestText.get_rect(center=(self.playWidth / 2, self.playWidth / 3))

        reText = fontRe.render('RESTARTING...', True, 'red')
        reRect = reText.get_rect(center=(self.playWidth / 2, self.playWidth / 2))

        self.screen.fill((0, 0, 0))
        self.screen.blit(scoreText, scoreRect)
        self.screen.blit(bestText, bestRect)
        self.screen.blit(reText, reRect)
        pygame.display.flip()

        time.sleep(3)
        self.restart()

    def reset(self):
        self.snakePos = [80, 50]
        self.snakeBody = [[80, 50], [70, 50]]
        self.orbPos = [random.randrange(1, (600 // 10)) * 10, random.randrange(1, (500 // 10)) * 10]
        self.orb = True
        self.score = 0
        self.direc = 'RIGHT'
        self.nextDirec = 'RIGHT'

    def restart(self):
        self.reset()
        self.__init__(self.screen, self.clock)
        self.paused = False

    def snakeLoop(self):
        self.direc = 'RIGHT'
        self.nextDirec = self.direc

        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.paused = not self.paused

            if self.paused:
                for event in events:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if self.pause.buttonResume.collidepoint(event.pos):
                            self.paused = False
                        elif self.pause.buttonRestart.collidepoint(event.pos):
                            self.restart()
                        elif self.pause.buttonExit.collidepoint(event.pos):
                            pygame.quit()
                            quit()
                self.pause.pauseDraw()
                pygame.display.flip()
                continue
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.nextDirec = 'UP'
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.nextDirec = 'DOWN'
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.nextDirec = 'LEFT'
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.nextDirec = 'RIGHT'

            if self.nextDirec == 'UP' and self.direc != 'DOWN':
                self.direc = 'UP'
            if self.nextDirec == 'DOWN' and self.direc != 'UP':
                self.direc = 'DOWN'
            if self.nextDirec == 'LEFT' and self.direc != 'RIGHT':
                self.direc = 'LEFT'
            if self.nextDirec == 'RIGHT' and self.direc != 'LEFT':
                self.direc = 'RIGHT'

            if self.direc == 'UP':
                self.snakePos[1] -= 10
            if self.direc == 'DOWN':
                self.snakePos[1] += 10
            if self.direc == 'LEFT':
                self.snakePos[0] -= 10
            if self.direc == 'RIGHT':
                self.snakePos[0] += 10

            if self.snakePos[1] < 50:
                self.snakePos[1] = 50

            self.snakeBody.insert(0, list(self.snakePos))
            snakeHead = pygame.Rect(self.snakePos[0], self.snakePos[1], 10, 10)
            orbRect = pygame.Rect(self.orbPos[0], self.orbPos[1], 10, 10)

            if snakeHead.colliderect(orbRect):
                self.score += 1
                self.orb = False
            else:
                self.snakeBody.pop()

            if not self.orb:
                self.orbPos = [random.randrange(1, (600 // 10)) * 10, random.randrange(5, (500 // 10)) * 10 + 50]

            self.orb = True
            self.screen.fill((20, 20, 20), (0, 50, 600, 450))
            self.showScore()

            for pos in self.snakeBody:
                pygame.draw.rect(self.screen, (50, 100, 200), (pos[0], pos[1], 10, 10))
            pygame.draw.circle(self.screen, (0, 150, 250), (self.orbPos[0] + 10 // 2, self.orbPos[1] + 10 // 2),
                               10 // 2)

            if self.snakePos[0] < 0 or self.snakePos[0] > 600 - 10:
                self.gameOver()
            if self.snakePos[1] < 0 or self.snakePos[1] > 500 - 10:
                self.gameOver()
            for block in self.snakeBody[1:]:
                if self.snakePos[0] == block[0] and self.snakePos[1] == block[1]:
                    self.gameOver()

            pygame.display.flip()
            self.clock.tick(self.snakeSpeed)
