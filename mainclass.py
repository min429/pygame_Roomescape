import pygame


class objects():
    def __init__(self, m_file, m_location=(0, 0), m_size=None):
        self.m_size = m_size
        self.m_size_x, self.m_size_y = self.m_size
        self.m_location = m_location
        self.m_x, self.m_y = self.m_location
        self.m_img = pygame.image.load(m_file)
        self.m_img = pygame.transform.scale(self.m_img, self.m_size)
        self.m_firstimg = self.m_img
        self.m_firstsize = m_size
        self.m_firstlocation = m_location
        self.m_state = 0

    def scale(self, m_size):  # 비율조정
        return pygame.transform.scale(self.m_img, m_size)

    def self_rotate(self, m_degree):
        self.m_img = pygame.transform.rotate(self.m_img, m_degree)

    def rotate(self, m_degree):
        return pygame.transform.rotate(self.m_img, m_degree)

    def self_locate(self, m_location):  # 객체 위치 변환
        self.m_location = m_location
        self.m_x, self.m_y = self.m_location

    def set_alpha(self, x):
        self.m_img.set_alpha(x)

    def change_img(self, img, spot):
        self.m_img = img
        self.m_location = spot

    def change_img_scale(self, size):  # 사진 크기가 바뀌면 클릭 범위도 바뀌기 때문에 이미지 크기에 맞춰 실제 객체 크기도 바꿔줘야 함  # (이승민 05/30 14:30 추가)
        self.m_size = size
        self.m_size_x, self.m_size_y = self.m_size

    def return_img(self, img, spot):
        self.m_img = img
        self.m_location = spot

    def clicked(self):          # 앞에 띄우기
        if self.m_state == 0:
            self.m_state = 1
        elif self.m_state == 1:
            self.m_state = 0
