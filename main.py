import pygame
from gui import GUI
from snake import Game
from start import StartMenu
from pause import PauseMenu


def main():
    pygame.init()
    w, h = 600, 500
    gui = GUI(w, h)
    start = StartMenu(gui.getScreen())
    pause = PauseMenu(gui.getScreen())
    setup = None

    menuON = True
    gameON = False
    paused = False

    while True:
        if menuON:
            start.startLogic()
            start.startDraw()
            pygame.display.flip()

            if start.clicked:
                menuON = False
                gameON = True
                setup = Game(gui.getScreen(), gui.getClock())
                gui.getScreen().fill((20, 20, 20))
                pygame.display.flip()

        if gameON and not paused:
            setup.snakeLoop()
            pygame.display.flip()

        if gameON and paused:
            pause.pauseLogic()
            pause.pauseDraw()
            pygame.display.flip()


if __name__ == '__main__':
    main()
