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
'''
'''
import pygame #导入pygame模块
import sys    #我们利用import语句 输入 sys模块。基本上，这句语句告诉Python，我们想要使用这个模块。sys模块包含了与Python解释器和它的环境有关的函数。

pygame.init() #初始化pygame

size = width,height = 640,480  #设置窗口大小
screen = pygame.display.set_mode(size) #显示窗口


while True:  #死循环确保窗口一直显示
    for event in pygame.event.get():  #遍历所有事件
        if event.type == pygame.QUIT:   #如果事件类型是单击关闭窗口
            sys.exit()  #退出sys

pygame.quit() #退出pygame
'''

import pygame
import sys

pygame.init()
size = width,height =480,240
screen = pygame.display.set_mode(size)
color = (255,255,0)
ball = pygame.image.load('ball.png')
ballrect = ball.get_rect()
'''
上述代码中，首先导入pygame模块，
然后调用init()方法初始化pygame模块，
接下来，设置窗口的宽和高，
最后使用display模块显示窗体。
'''
'''
运行第一步的代码后会出现一个一闪而过的黑色窗口，
这是因为程序执行完成后，会自动关闭。
如果想要让窗口一直显示，需要使用while True让程序一直执行，
此外，还需要设置关闭按钮。具体代码如下：
'''

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(color)
    screen.blit(ball,ballrect)
    pygame.display.flip()

pygame.quit()
'''
上述代码中添加了轮询事件检测。
pygame.event.get()能够获取事件队列，
使用for...in遍历事件，然后根据type属性判断事件类型。
如event.type等于pygame.QUIT表示检测到关闭pygame窗口事件，
pygame.KEYDOWN表示键盘按下事件，
pygame.MOUSEBUTTONDOWN表示鼠标按下事件等。

'''





