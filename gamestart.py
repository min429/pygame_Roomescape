import pygame
from pygame.locals import *
import sys

pygame.init()           # pygame 사용시 무조건 필요한 초기화함수
size = (1280, 720)       # 게임 해상도 변수 (800x600 고정)
screen = pygame.display.set_mode(size)      # 게임 해상도 설정
pygame.display.set_caption("Room Escape")  # 게임 상태표시줄 이름
clock = pygame.time.Clock()                 # 게임 프레임 단위 설정

bgx = 1280
bgy = 720
bgsize = (bgx, bgy)
bgimg = pygame.image.load("startbackground2.png")
bgimg = pygame.transform.scale(bgimg, bgsize)
startpoint = (0, 0)

pygame.mixer.music.load("Dining-Room.ogg")
pygame.mixer.music.play(-1)

while True:

    screen.blit(bgimg, startpoint)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_F12:          # F12 누르면 게임 시작
                exec(open("main.py", 'r', encoding="UTF-8").read())
                # (625, 335), (685, 360)
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:      # start 누르면 게임 시작
            if 1000 <= pygame.mouse.get_pos()[0] <= 1100:
                if 400 <= pygame.mouse.get_pos()[1] <= 430:
                    pygame.mixer.music.stop()
                    exec(open("main.py", 'r', encoding="UTF-8").read())

            if 1000 <= pygame.mouse.get_pos()[0] <= 1100:
                if 453 <= pygame.mouse.get_pos()[1] <= 483:
                    pygame.quit()
                    sys.exit()
