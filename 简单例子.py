'''
#导入pygame sys模块
import pygame
import sys

#初始化pygame
pygame.init()
size = width,height = 320,240  #设置窗口大小
screen = pygame.display.set_mode(size)   #显示窗口

while True:   #死循环确保窗口一直显示
    for event in pygame.event.get():  #遍历所有事件
        if event.type == pygame.QUIT:  #如果单击关闭窗口，则退出
            sys.exit()
pygame.quit()

'''
'''
import pygame
import sys

pygame.init()

size = width,height = 640,480
screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()
pygame.quit()

'''
'''
import sys
import pygame

pygame.init()

size = width,height = 125,125
screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

pygame.quit()
'''
import pygame
import sys
pygame.init()
size = width,height = 248,248
screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

pygame.quit()

