#写一个你好世界的小例子，用两张图片
import pygame
import time

from pygame.locals import *
from sys import exit
background_image_filename = 'sea.jpg'
mouse_image_filename = 'fish.png'

pygame.init() #初始化pygame，为使用硬件作准备

screen = pygame.display.set_mode((640,480),0,32) #创建一个窗口

pygame.display.set_caption("hello,world!") #设置窗口标题

background = pygame.image.load(background_image_filename) #加载图片并转换
mouse_crusor = pygame.image.load(mouse_image_filename)

while True: #游戏主循环
    for event in pygame.event.get():
        if event.type == QUIT: #接收到退出后 退出程序 
            exit() 

    screen.blit(background,(0,0)) #画背景

    x,y = pygame.mouse.get_pos() #获得鼠标位置

    x -= mouse_crusor.get_width() / 2 #计算光标左上角位置
    y -= mouse_crusor.get_height() / 2

    screen.blit(mouse_crusor,(x,y)) #将光标画上去

    pygame.display.update() #刷新画面

input()