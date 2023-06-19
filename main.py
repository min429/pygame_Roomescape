import pygame
from pygame.locals import *
import sys
from mainclass import *  # 객체 관리용 클래스
import room1

global fadespeed
fadespeed = 10
global control
control = 1
global control2
control2 = 1
global control3
control3 = 1
#234(67, 116)크기 시작위치(695, 323)
# 인벤토리 객체 (140x720)

global text
text = 0

once_text_check = 0

def rotation(image, angle):
    """rotate a Surface, maintaining position."""

    loc = image.get_rect().center  # rot_image is not defined
    rot_sprite = pygame.transform.rotate(image, angle)
    rot_sprite.get_rect().center = loc
    image = rot_sprite
    return image

    # or return tuple: (Surface, Rect)
    # return rot_sprite, rot_sprite.get_rect()

def fade_out(width, height, img_temp, object_temp):  # fade-out 사용용 함수
    fade = pygame.Surface((width, height))  # 어느 범위만큼 fade 할건지
    global fadespeed
    for alpha in range(0, 255, fadespeed):  # alpha를 fadespeed씩 늘리며
        fade.set_alpha(alpha)               # 투명도 조절
        screen.blit(img_temp, (0, 0))       # 배경 출력
        for obj in object_temp:
            screen.blit(obj.m_img, obj.m_location)
            # 반복문에서 각 배경에 해당하는 객체들 출력
        screen.blit(fade, (0, 0))  # 전체화면 어둡게
        pygame.display.update()


def fade_in(width, height, img_temp, object_temp):  # fade-in 사용용 함수
    fade = pygame.Surface((width, height))  # 어느 범위만큼 fade 할건지
    global fadespeed
    for alpha in range(255, 0, -fadespeed):
        fade.set_alpha(alpha)
        screen.blit(img_temp, (0, 0))
        for obj in object_temp:
            screen.blit(obj.m_img, obj.m_location)
        screen.blit(fade, (0, 0))
        pygame.display.update()
        #pygame.time.delay(1)

################################
def fade_out2(width, height, img_temp, object_temp):  # fade-out 사용용 함수
    fade = pygame.Surface((width, height))            # 어느 범위만큼 fade 할건지
    global fadespeed
    for alpha in range(0, 255, 255):            # alpha를 1씩 늘리며
        fade.set_alpha(alpha)                   # 투명도 조절
        screen.blit(img_temp, (0, 0))           # 배경 출력
        for obj in object_temp:
            screen.blit(obj.m_img, obj.m_location)  # 반복문에서 각 배경에 해당하는 객체들 출력
        screen.blit(fade, (0, 0))  # 전체화면 어둡게
        pygame.display.update()


def fade_in2(width, height, img_temp, object_temp):  # fade-in 사용용 함수
    fade = pygame.Surface((width, height))  # 어느 범위만큼 fade 할건지
    global fadespeed
    for alpha in range(255, 0, -255):
        fade.set_alpha(alpha)
        screen.blit(img_temp, (0, 0))
        for obj in object_temp:
            screen.blit(obj.m_img, obj.m_location)
        screen.blit(fade, (0, 0))
        pygame.display.update()
        #pygame.time.delay(1)
############################################


def fade(width, height, img_temp, img_temp2):  # fade-in, fade-out 사용용 함수
    fade = pygame.Surface((width, height))     # 어느 범위만큼 fade 할건지
    global fadespeed
    for alpha in range(0, 255, fadespeed):     # alpha를 fadespeed씩 늘리며
        fade.set_alpha(alpha)                  # 투명도 조절
        screen.blit(img_temp, (0, 0))          #
        screen.blit(fade, (0, 0))
        pygame.display.update()
        #pygame.time.delay(1)

    for alpha in range(255, 0, -fadespeed):
        fade.set_alpha(alpha)
        screen.blit(img_temp2, (0, 0))
        screen.blit(fade, (0, 0))
        pygame.display.update()
        #pygame.time.delay(1)


def fadeonce(width, height, img_temp, img_temp2, object_temp):  # 맨 처음 불킬때 사용하는 페이드
    fade = pygame.Surface((width, height))  # 어느 범위만큼 fade 할건지
    global fadespeed

    for alpha in range(255, 0, -fadespeed * 20):
        fade.set_alpha(alpha)
        screen.blit(img_temp2, (0, 0))  # 1p
        screen.blit(fade, (0, 0))
        pygame.display.update()
        #pygame.time.delay(1)

    for alpha in range(0, 199, fadespeed * 15):
        fade.set_alpha(alpha)  # 투명도 조절
        screen.blit(img_temp2, (0, 0))
        for obj in object_temp:
            screen.blit(obj.m_img, obj.m_location)
        screen.blit(fade, (0, 0))
        pygame.display.update()
        #pygame.time.delay(1)


# 배경 초기화
pygame.init()  # pygame 사용시 무조건 필요한 초기화 함수

size = (1280, 720)  # 게임 해상도 변수 (1280 x 720 고정)
screen = pygame.display.set_mode(size)  # 게임 해상도 설정
pygame.display.set_caption("Room Escape")  # 게임 상단바 이름

clock = pygame.time.Clock()  # 게임 프레임 단위 설정
background_color = (255, 255, 255)  # background용 color (black)
screen.fill(background_color)

oncebg = pygame.image.load("oncebg.png")  # 맨 처음 어두운 화면
blackbg = pygame.image.load("black.png")  # 검은색 화면
small_blackbg = pygame.image.load("black.png")  # 검은화면
small_blackbg = pygame.transform.scale(small_blackbg, (1140, 720))
small_blackbg.set_alpha(0)
black2 = pygame.image.load("black2.png")

big_size = (400, 400)  # 확대된 사진 크기
big_x, big_y = big_size
big_location = (640 - big_x / 2, 360 - big_y / 2)

# 배경화면 객체화
img = objects("1p.png", (0, 0), (1140, 720))  # 첫번째 이미지 로드
img2 = objects("2p.png", (0, 0), (1140, 720))  # 두번째 이미지 로드
img3 = objects("3p.png", (0, 0), (1140, 720))  # 세번째 이미지 로드
img4 = objects("4p.png", (0, 0), (1140, 720))  # 네번째 이미지 로드
img1_p1 = pygame.image.load("1p.png")
img4_p1 = pygame.image.load("4p.png")
img_scary_p1 = pygame.image.load("scarypp.png")
img_scary = pygame.image.load("scaryp.png")
img_scary2 = pygame.image.load("scaryp2.png")
final1p = pygame.image.load("final1p.png")
ending = pygame.image.load("ending.png")
ending = pygame.transform.scale(ending, (1280, 720))
ending2 = pygame.image.load("ending2.png")
ending2 = pygame.transform.scale(ending2, (1280, 720))
noise = pygame.image.load("noise.png")
noise = pygame.transform.scale(noise, (1140, 720))
noise.set_alpha(0)
scarydoll = objects("scarydoll.png", (460, 420), (269, 296))
dolldoll = 0
p1back = 0
p1back2 = 0
scarydoll.set_alpha(0)

# 545,520
# 왼쪽 화살표 객체
arrow_left = objects("arrow.png", (0, 360 - 83 / 2), (83, 83))  # x는 0, y는 정중앙 (720반에서 화살표 크기의 반만큼 위에서)
arrow_left.self_rotate(180)  # 화살표를 180도 돌려줘야 왼쪽을 가리킴

# 오른쪽 화살표 객체
arrow_right = objects("arrow.png", (1140 - 83, 360 - 83 / 2), (83, 83))

# x버튼 객체
x = objects("x.png", (1050, 25), (80, 80))
x.set_alpha(0)

################################ 1번방 #################################################################
# 문 = 추상 객체
MOON = objects("x.png", (1, 1), (1, 1))
MOON.set_alpha(0)
MOONcheck = 0

# 마스료시카
Matryoshka_size = (85, 85)
Matryoshka_p1 = pygame.image.load("Matryoshka.png")
Matryoshka = objects("Matryoshka.png", (150, 280), (Matryoshka_p1.get_width()*0.23, Matryoshka_p1.get_height()*0.23))
Matryoshka_big = pygame.transform.scale(Matryoshka_p1, (Matryoshka_p1.get_width()*0.69, Matryoshka_p1.get_height()*0.69))  # 까기 전
Matryoshka_p2 = pygame.image.load("Matryoshka_p2.png")  # 1번 깠을 때
Matryoshka_p2 = pygame.transform.scale(Matryoshka_p2, (Matryoshka_p1.get_width()*0.69, Matryoshka_p1.get_height()*0.69))
Matryoshka_p3 = pygame.image.load("Matryoshka_p3.png")  # 2번 깠을 때
Matryoshka_p3 = pygame.transform.scale(Matryoshka_p3, (Matryoshka_p1.get_width()*0.69, Matryoshka_p1.get_height()*0.60375))
Matryoshka_p4 = pygame.image.load("Matryoshka_p4.png")  # 3번 깠을 때
Matryoshka_p4 = pygame.transform.scale(Matryoshka_p4, (Matryoshka_p1.get_width()*0.69, Matryoshka_p1.get_height()*0.345))
Matryoshka_head1 = pygame.image.load("Matryoshka_head.png")  # 마트료시카 뚜껑1
Matryoshka_head1 = pygame.transform.scale(Matryoshka_head1, (Matryoshka_p1.get_width()*0.552, Matryoshka_p1.get_height()*0.552))
Matryoshka_head2 = pygame.image.load("Matryoshka_head.png")  # 마트료시카 뚜껑2
Matryoshka_head2 = pygame.transform.scale(Matryoshka_head2, (Matryoshka_p1.get_width()*0.483, Matryoshka_p1.get_height()*0.483))
Matryoshka_head3 = pygame.image.load("Matryoshka_head.png")  # 마트료시카 뚜껑3
Matryoshka_head3 = pygame.transform.scale(Matryoshka_head3, (Matryoshka_p1.get_width()*0.414, Matryoshka_p1.get_height()*0.414))
Matryoshka_count = 0  # 마트료시카를 다 깠는지
Matryoshka_head1.set_alpha(0)  #  까기 전에 투명상태
Matryoshka_head2.set_alpha(0)  #  까기 전에 투명상태
Matryoshka_head3.set_alpha(0)  #  까기 전에 투명상태

# 공구박스
toolbox = objects("toolbox.png", (137, 474), (197, 123))
toolbox_p1 = pygame.image.load("toolbox.png")
toolbox_big = pygame.transform.scale(toolbox_p1, (toolbox.m_size_x * 3, toolbox.m_size_y * 3))
toolbox_p1 = pygame.transform.scale(toolbox_p1, (197, 123))

toolbox_p2 = pygame.image.load("open_toolbox.png")
toolbox_p2 = pygame.transform.scale(toolbox_p2, (550, 323))

toolbox2_p1 = pygame.image.load("second_toolbox.png")
toolbox2_big = pygame.transform.scale(toolbox2_p1, (toolbox.m_size_x * 3, toolbox.m_size_y * 3))
toolbox2_p1 = pygame.transform.scale(toolbox2_p1, (197, 123))

empty_toolbox = pygame.image.load("emptybox.png")
empty_toolbox = pygame.transform.scale(empty_toolbox, (550, 323))

# 트로피
trophy = objects("trophy.png", (160, 162), (80, 101))
trophy_p1 = pygame.image.load("trophy.png")
trophy_big = pygame.transform.scale(trophy_p1, (trophy.m_size_x * 3, trophy.m_size_y * 3))
trophy_p1 = pygame.transform.scale(trophy_p1, (80, 101))

# 화분
pot_p1 = pygame.image.load("pot.png")
pot_big = pot_p1
pot_p1 = pygame.transform.scale(pot_p1, (107, pot_p1.get_height()*107/279))
pot = objects("pot.png", (585, 390), pot_p1.get_size())

pot_p2 = pygame.image.load("pot2.png")
pot2_big = pygame.transform.scale(pot_p2, (pot_p2.get_width()*2, pot_p2.get_height()*2))

# 책 ######## 05/25 17:47
books_p1 = pygame.image.load("book.png")
books_big = pygame.transform.scale(books_p1, (books_p1.get_width() * 3, books_p1.get_height() * 3))
books = objects("book.png", (163, 388), (books_p1.get_size()))
books_p2 = pygame.image.load("book2.png")
books_p2 = pygame.transform.scale(books_p2, (books_p2.get_width() * 0.8, books_p2.get_height() * 0.8))
books_p3 = pygame.image.load("book3.png")
books_p3 = pygame.transform.scale(books_p3, (books_p3.get_width() * 0.7, books_p3.get_height() * 0.7))

# 프랑스 인형 (이승민 05/27 13:41추가)
doll = objects("doll.png", (675, 533), (125, 137))
doll_p1 = pygame.image.load("doll.png")
doll_big = pygame.transform.scale(doll_p1, (doll.m_size_x*3, doll.m_size_y*3))

#무서은 인형
doll_p2 = pygame.image.load("doll2.png")
doll2 = objects("doll2.png", (650, 550), (doll_p2.get_width()/2, doll_p2.get_height()/2))
doll2.set_alpha(0)

# 액자
photoframe = objects("photoframe.png", (382, 288), (55, 87))
photoframe_p1 = pygame.image.load("photoframe.png")
photoframe_p2 = pygame.image.load("photoframe2.png")
photoframe_big = pygame.transform.scale(photoframe_p1, (photoframe_p1.get_width() / 2, photoframe_p1.get_height() / 2))
photoframe2_big = pygame.transform.scale(photoframe_p2, (photoframe_p2.get_width() / 2, photoframe_p2.get_height() / 2))
photoframe_p1 = pygame.transform.scale(photoframe_p1, (55, 87))
photoframe_p2 = pygame.transform.scale(photoframe_p2, (55, 87))

# 철제 액자 #(390, 160)
steelframe = objects("steelframe.png", (580, 220), (160, 111))
steelframe_p1 = pygame.image.load("steelframe.png")
steelframe_big = pygame.transform.scale(steelframe_p1, (steelframe_p1.get_width() / 3, steelframe_p1.get_height() / 3))
steelframe_p1 = pygame.transform.scale(steelframe_p1, (160, 111))

################################ 2번방 #################################################################
# 마네킹 =추상객체
mannequin_size = (170, 489)
mannequin_location = (270, 186)
mannequin = objects("x.png", (1, 1), (1, 1))
mannequin.set_alpha(0)
mqcheck = 0

# 옷장
closet = objects("closet.png", (732, 154), (272, 519))
closet_p1 = closet.m_img
big_closet = closet.scale((310, 550))

# 열린 옷장
open_closet = objects("open.png", (732, 154), (454, 537))
open_closet_p1 = open_closet.m_img
open_closet_p2 = pygame.image.load("open2.png")
open_closet_p2 = pygame.transform.scale(open_closet_p2, (454, 537))

# 거울
mirror = objects("mirror.png", (100, 272), (165, 416))
mirror_p1 = pygame.image.load("mirror.png")
mirror_p2 = pygame.image.load("mirror_scene2.png")
big_mirror = pygame.transform.scale(mirror_p2, (mirror_p2.get_width()*0.75, mirror_p2.get_height()*0.75))
mirror_p1 = pygame.transform.scale(mirror_p1, (mirror_p1.get_width()*0.6273, mirror_p1.get_height()*0.6273))

# 도어락
doorlock = objects("doorlock.png", (400, 70), (407, 561))
doorlock_p1 = pygame.image.load("doorlock.png")
doorlock_p1 = pygame.transform.scale(doorlock_p1, (407, 561))
doorlock.set_alpha(0)

################################ 3번방 #################################################################
# 곰인형
bear = objects("bear.png", (783, 358), (295, 346))
bear_p1 = bear.m_img
bear_big = bear.scale((bear.m_size_x * 1.66, bear.m_size_y * 1.66))
bear2 = objects("bear2.png", (783, 358), (295, 346))  # 가짜 곰인형 객체
bear_p2 = bear2.m_img
bear_big2 = bear2.scale((bear2.m_size_x * 1.66, bear2.m_size_y * 1.66))
bear3 = objects("bear3.png", (783, 358), (295, 346))  # 가짜 곰인형 객체
bear_p3 = bear3.m_img
bear_big3 = bear3.scale((bear3.m_size_x * 1.66, bear3.m_size_y * 1.66))

bear_cut = 0

# 장난감 집
house = objects("house.png", (500, 400), (250, 290))
house_p1 = pygame.image.load("house.png")
house_p1 = pygame.transform.scale(house_p1, (250, 290))
house_big = house.scale((house.m_size_x * 1.5, house.m_size_y * 1.5))
house_open = pygame.image.load("house_open.png")
house_big2 = pygame.transform.scale(house_open, (492, 642))
house_p3 = pygame.image.load("house3.png")
house_big3 = pygame.transform.scale(house_p3, (492, 642))
house_p3 = pygame.transform.scale(house_p3, (328, 428))
first_house_open = 0
house_door_open = 0
safe_out = 0

# 아기침대
bed = objects("bed.png", (135, 455), (290, 240))
bed_p1 = bed.m_img
bed_p1_big=bed.scale((bed.m_size_x * 1.5, bed.m_size_y * 1.5))
bed_baby = pygame.image.load("bed_baby.png")
bed_baby = pygame.transform.scale(bed_baby, (290, 240))
bed_baby_big = pygame.transform.scale(bed_baby, (435, 360))
baby_in_bed = 0

# 금고 (602, 492) ~ (701, 657)
safe = objects("safe1.png", (660, 490), (100, 169))
safe_p1 = pygame.image.load("safe1.png")
safe_big = pygame.transform.scale(safe_p1, (safe.m_size_x*3, safe.m_size_y*3))
safe_p1 = pygame.transform.scale(safe_p1, (100, 169))
safe.set_alpha(0)

safe_p2 = pygame.image.load("safe2.png") # 드라이버 있는거
safe2_big = pygame.transform.scale(safe_p2, (safe_p2.get_width()*0.9, safe_p2.get_height()*0.9))
safe_p2 = pygame.transform.scale(safe_p2, (safe_p2.get_width()*0.3, safe_p2.get_height()*0.3))

safe_p3 = pygame.image.load("safe3.png") # 드라이버 없는거
safe3_big = pygame.transform.scale(safe_p3, (safe_p3.get_width()*0.9, safe_p3.get_height()*0.9))
safe_p3 = pygame.transform.scale(safe_p3, (safe_p3.get_width()*0.3, safe_p3.get_height()*0.3))

mainsound = pygame.mixer.Sound("dark3.mp3")
mainsound.set_volume(0.1)
mainsound.play(-1)
mainsound_on = 0

# 다이얼 (642, 313) ~ (671, 345)
dial = objects("dial.png", (310, 60), (570, 564))
dial.set_alpha(0)

dial_p1 = pygame.image.load("dial1.png")
dial_p1 = pygame.transform.smoothscale(dial_p1, dial.m_size)

dial_p2 = pygame.image.load("dial2.png")
dial_p2 = pygame.transform.smoothscale(dial_p2, dial.m_size)

dial_p3 = pygame.image.load("dial3.png")
dial_p3 = pygame.transform.smoothscale(dial_p3, dial.m_size)

dial_p4 = pygame.image.load("dial4.png")
dial_p4 = pygame.transform.smoothscale(dial_p4, dial.m_size)

dial_p5 = pygame.image.load("dial5.png")
dial_p5 = pygame.transform.smoothscale(dial_p5, dial.m_size)

dial_p6 = pygame.image.load("dial6.png")
dial_p6 = pygame.transform.smoothscale(dial_p6, dial.m_size)

dial_p7 = pygame.image.load("dial7.png")
dial_p7 = pygame.transform.smoothscale(dial_p7, dial.m_size)

dial_p8 = pygame.image.load("dial8.png")
dial_p8 = pygame.transform.smoothscale(dial_p8, dial.m_size)

dial_p9 = pygame.image.load("dial9.png")
dial_p9 = pygame.transform.smoothscale(dial_p9, dial.m_size)

dial_p0 = pygame.image.load("dial0.png")
dial_p0 = pygame.transform.smoothscale(dial_p0, dial.m_size)

dial_plist = [dial_p1, dial_p2, dial_p3, dial_p4, dial_p5, dial_p6, dial_p7, dial_p8, dial_p9, dial_p0]

dial2 = objects("dial2.png", (310, 60), (570, 564))
dial2.set_alpha(0)
dial_num = 0
dial_list = []
dial_password = [3, 8, 6]
dial_success = 0
dial_scary = 0

################################## 4번방 #################################################################
# 베토벤
frame1 = objects("frame1.png", (181, 120), (120, 150))
frame1_p1 = pygame.image.load("frame1.png")
frame1_big = pygame.transform.scale(frame1_p1, (360, 450))
frame1_p1 = pygame.transform.scale(frame1_p1, (120, 150))

# 바흐
frame2 = objects("frame2.png", (306, 66), (120, 150))
frame2_p1 = pygame.image.load("frame2.png")
frame2_big = pygame.transform.scale(frame2_p1, (360, 450))
frame2_p1 = pygame.transform.scale(frame2_p1, (120, 150))

# 모차르트
frame3 = objects("frame3.png", (227, 273), (120, 150))
frame3_p1 = pygame.image.load("frame3.png")
frame3_big = pygame.transform.scale(frame3_p1, (360, 450))
frame3_p1 = pygame.transform.scale(frame3_p1, (120, 150))

# 슈베르트
frame4 = objects("frame4.png", (360, 228), (120, 150))
frame4_p1 = pygame.image.load("frame4.png")
frame4_big = pygame.transform.scale(frame4_p1, (360, 450))
frame4_p1 = pygame.transform.scale(frame4_p1, (120, 150))

# 레코드 플레이어
rp = objects("rp.png", (589, 262), (140, 420))
rp_p1 = pygame.image.load("rp.png")
rp_big = pygame.transform.scale(rp_p1, (210, 630))
rp_p1 = pygame.transform.scale(rp_p1, (140, 420))

# 의자
chair = objects("chair.png", (844, 480), (150, 200))
chair_p1 = pygame.image.load("chair.png")
chair_big = pygame.transform.scale(chair_p1, (300, 400))
chair_p1 = pygame.transform.scale(chair_p1, (150, 200))
chair_p2 = pygame.image.load("chair_down.png")
chair_p2 = pygame.transform.scale(chair_p2, (chair_p2.get_width() * 0.5, chair_p2.get_height() * 0.5))
chair_p3 = pygame.image.load("chair_down2.png")
chair_p3 = pygame.transform.scale(chair_p3, (chair_p3.get_width() * 0.5, chair_p3.get_height() * 0.5))
chair_p4 = pygame.image.load("chair_down3.png")
chair_p4 = pygame.transform.scale(chair_p4, (chair_p4.get_width() * 0.5, chair_p4.get_height() * 0.5))
open_chair = 0
pass1 = 0

####################################### 인벤 #############################################################

# 바깥 라인
outline = pygame.image.load("outline.png")
outline = pygame.transform.scale(outline, (1140, 720))

# 인벤토리  # (이승민 05/30 14:30 추가)
spot_count = [0]*5  # 인벤 칸 개수만큼 리스트 생성
spot_size = (59, 56)  # 인벤 칸 사이즈
spot_location = [(1184, 94), (1184, 94+120), (1184, 94+120*2), (1184, 94+120*3), (1184, 94+120*4)]  # 각 칸의 위치

####################################### 1번화면 인벤 ############################################################# (이승민 05/27 13:41추가)

# 인벤 칼 (이승민 05/27 13:41추가)
knife = objects("knife.png", (0, 0), spot_size)
knife_p1 = pygame.image.load("knife.png")
knife_edge = pygame.image.load("knife_edge.png")
knife_edge = pygame.transform.scale(knife_edge, spot_size)  # 칼 빛나는 사진
inven_knife = pygame.transform.scale(knife_p1, spot_size)  # 빛나지 않을 때 사진
inven_knife_location = None  # 아직 인벤에 추가 안됐을 때 위치 None
get_knife = 0  # 칼을 얻었는지 여부
knife_glow = 0  # 칼이 빛나는지 여부
use_knife = 0  # 칼을 사용했는지 여부

# 인벤 십자드라이버 (이승민 05/30 14:30추가)
ten_driver = objects("ten_driver.png", (0, 0), spot_size)
ten_driver_p1 = pygame.image.load("ten_driver.png")
ten_driver_edge = pygame.image.load("ten_driver_edge.png")
ten_driver_edge = pygame.transform.scale(ten_driver_edge, spot_size)
inven_ten_driver = pygame.transform.scale(ten_driver_p1, spot_size)
inven_ten_driver_location = None
get_ten_driver = 0
ten_driver_glow = 0
use_ten_driver = 0

####################################### 2번화면에서 얻은 인벤 ############################################################# (이승민 05/27 13:41추가)
# 인벤 열쇠 (이승민 05/27 13:41추가)
key = objects("key.png", (0, 0), spot_size)
key_p1 = pygame.image.load("key.png")
key_edge = pygame.image.load("key_edge.png")
key_edge = pygame.transform.scale(key_edge, spot_size)
inven_key = pygame.transform.scale(key_p1, spot_size)
inven_key_location = None

key_glow = 0
use_key = 0

####################################### 3번화면에서 얻은 인벤 ############################################################# (이승민 05/27 13:41추가)
# 인벤 일자 드라이버 (이승민 05/27 13:41추가)
one_driver = objects("one_driver.png", (0, 0), spot_size)
one_driver_p1 = pygame.image.load("one_driver.png")
one_driver_edge = pygame.image.load("one_driver_edge.png")
one_driver_edge = pygame.transform.scale(one_driver_edge, spot_size)
inven_one_driver = pygame.transform.scale(one_driver_p1, spot_size)
inven_one_driver_location = None

one_driver_glow = 0
use_one_driver = 0

# 인벤 프랑스 인형 # (이승민 5/26 01:00 추가)
#  프랑스 인형은 다른 인벤 아이템과 달리 객체를 생성하지 않음
doll_edge = pygame.image.load("doll_edge.png")
doll_edge = pygame.transform.scale(doll_edge, spot_size)
inven_doll = pygame.transform.scale(doll_p1, spot_size)
inven_doll_location = None  # 마트료시카 인벤 위치
get_doll = 0  # 마트료시카 획득 여부
doll_glow = 0
use_doll = 0
nodoll = 0

####################################### 4번화면에서 얻은 인벤 ############################################################# (이승민 05/27 13:41추가)
# 인벤 레코드 판 (이승민 05/27 13:41추가)
record = objects("record.png", (0, 0), spot_size)
record_p1 = pygame.image.load("record.png")
record_edge = pygame.image.load("record_edge.png")
record_edge = pygame.transform.scale(record_edge, spot_size)
inven_record = pygame.transform.scale(record_p1, spot_size)
inven_record_location = None

record_glow = 0
use_record = 0

get_key, get_knife, get_ten_driver, get_one_driver, get_baby, get_record = 0, 0, 0, 0, 0, 0

ready_get_record = 0

moonopen = 0
# #스크립트 창

# textbox2 = pygame.image.load("textbox2.png")
textbox = objects("script1.png", (70,450), (1000, 221))
#여기가 어디지? V
textbox_p1 = pygame.image.load("script1.png")
textbox_p1 = pygame.transform.scale(textbox_p1, (1000, 221))
#어두워서 아무것도 보이지 않는다 V
textbox_p2 = pygame.image.load("script2.png")
textbox_p2 = pygame.transform.scale(textbox_p2, (1000, 221))
#문이 잠겨있다 V
textbox_p3 = pygame.image.load("script3.png")
textbox_p3 = pygame.transform.scale(textbox_p3, (1000, 221))
door = 0
#문을 열 방법을 찾아야겠다 V
textbox_p4 = pygame.image.load("script4.png")
textbox_p4 = pygame.transform.scale(textbox_p4, (1000, 221))
#방의 분위기와는 다르게 깔끔한 화분이 있다 V
textbox_p5 = pygame.image.load("script5.png")
textbox_p5 = pygame.transform.scale(textbox_p5, (1000, 221))
#화분이 깨져있다...
textbox_p6 = pygame.image.load("script6.png")
textbox_p6 = pygame.transform.scale(textbox_p6, (1000, 221))
#분명히 침대에 있던 인형이다
textbox_p7 = pygame.image.load("script7.png")
textbox_p7 = pygame.transform.scale(textbox_p7, (1000, 221))
#액자 뒷면이 나사로 조여져있다.  V
textbox_p8 = pygame.image.load("script8.png")
textbox_p8 = pygame.transform.scale(textbox_p8, (1000, 221))
#눈에 띄는 책 한 권이 있다.
textbox_p9 = pygame.image.load("script9.png")
textbox_p9 = pygame.transform.scale(textbox_p9, (1000, 221))
#자물쇠로 잠겨있다.  V
textbox_p10 = pygame.image.load("script10.png")
textbox_p10 = pygame.transform.scale(textbox_p10, (1000, 221))
#이상하게 생긴 마네킹이다  V
textbox_p11 = pygame.image.load("script11.png")
textbox_p11 = pygame.transform.scale(textbox_p11, (1000, 221))
#비밀번호로 잠겨있다
textbox_p12 = pygame.image.load("script12.png")
textbox_p12 = pygame.transform.scale(textbox_p12, (1000, 221))
#아기 침대이다  V
textbox_p13 = pygame.image.load("script13.png")
textbox_p13 = pygame.transform.scale(textbox_p13, (1000, 221))
#열리지 않는다. 이안에 무언가가 있다.  V
textbox_p14 = pygame.image.load("script14.png")
textbox_p14 = pygame.transform.scale(textbox_p14, (1000, 221))
#비밀번호가 필요하다.
textbox_p15 = pygame.image.load("script15.png")
textbox_p15 = pygame.transform.scale(textbox_p15, (1000, 221))
#배가 꿰어진 인형이다.   V
textbox_p16 = pygame.image.load("script16.png")
textbox_p16 = pygame.transform.scale(textbox_p16, (1000, 221))
#광장히 오래된 축음기로 보인다 V
textbox_p17 = pygame.image.load("script17.png")
textbox_p17 = pygame.transform.scale(textbox_p17, (1000, 221))
#오래앉아있기 힘들어보이는 의자이다
textbox_p18 = pygame.image.load("script18.png")
textbox_p18 = pygame.transform.scale(textbox_p18, (1000, 221))
#드라이버로 의자 밑면을 열 수 있을 듯하다. V
textbox_p19 = pygame.image.load("script19.png")
textbox_p19 = pygame.transform.scale(textbox_p19, (1000, 221))

# 노래가 나오고 있다.
textbox_p20 = pygame.image.load("script20.png")
textbox_p20 = pygame.transform.scale(textbox_p20, (1000, 221))


textbox.set_alpha(255)

password_doorlock = [2, 7, 5, 3]
# 자물쇠 확대 옷장
lock_number = []
lock_filled = {0: 0, 1: 0, 2: 0, 3: 0}


open_photo = 0  # 액자 사진 오픈
open_toolbox = 0
success_doorlock = 0

n0 = objects("n0.png", (90, 50), (29, 51))
n1 = objects("n1.png", (90, 50), (29, 51))
n2 = objects("n2.png", (90, 50), (29, 51))
n3 = objects("n3.png", (90, 50), (29, 51))
n4 = objects("n4.png", (90, 50), (29, 51))
n5 = objects("n5.png", (90, 50), (29, 51))
n6 = objects("n6.png", (90, 50), (29, 51))
n7 = objects("n7.png", (90, 50), (29, 51))
n8 = objects("n8.png", (90, 50), (29, 51))
n9 = objects("n9.png", (90, 50), (29, 51))
sblack = pygame.image.load("black.png")
sblack = pygame.transform.scale(sblack, (32, 32))
s1 = objects("black.png", (460, 99), (32, 32))
s2 = objects("black.png", (540, 99), (32, 32))
s3 = objects("black.png", (620, 99), (32, 32))
s4 = objects("black.png", (700, 99), (32, 32))

nlist = [n0, n1, n2, n3, n4, n5, n6, n7, n8, n9]
slist = [s1, s2, s3, s4]

for i in nlist:
    i.set_alpha(0)
for i in slist:
    i.set_alpha(0)

# 방의 객체들을 리스트로 모아놓음
object1 = [toolbox, trophy, Matryoshka, pot, books, photoframe, steelframe, doll2]
object2 = [closet, mirror, doorlock]
object3 = [bear, house, bed, safe, dial, dial2]
object4 = [frame1, frame2, frame3, frame4, rp, chair]

#인벤객체
invenlist = [inven_knife, inven_ten_driver, inven_key, inven_one_driver, inven_doll, inven_record]

rabbit, gomain = 0, 0

# 화면 전환용 변수들
noroom = 0
count = 0  # 시작 지점 설정 변수
startpoint = (0, 0)  # 시작좌표점 (0, 0) 으로 고정
countframe = 1  # 화살표 클릭시 프레임 구현용 (무한반복 방지)
leftright = 0  # 좌우 프레임 구현시 구분용 left=-1, right=1
once = 0  # 한번만 실행해야 하는 함수에 사용

####################################### 사운드 ############################################################# (이승민 05/30 14:30 추가)
record_music = pygame.mixer.music.load("record_music.mp3")  # 레코드 클릭시 음악