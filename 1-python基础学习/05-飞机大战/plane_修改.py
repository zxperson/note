# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import time
import sys

'''
说明
1.按下b键,让玩家飞机爆炸 
2.爆炸效果的原理是:换图片
'''

class Hero(object):
    '''英雄飞机类'''
    def __init__(self, screen_temp):
        self.offset = 0  #英雄飞机运动方向 标志. 0代表原地不动,-2代表向左移动,2代表向右移动
        self.switch = False   #英雄飞机的 大炮开关,True为开,False为关
        self.x = 210
        self.y = 720
        self.image = pygame.image.load("./feiji/hero1.png")
        self.screen = screen_temp
        self.bullet_list = []#用来存储子弹对象的引用

        #爆炸效果用的如下属性
        self.hit = False #表示是否要爆炸
        self.bomb_list = [] #用来存储爆炸时需要的图片
        self.__crate_images() #调用这个方法向bomb_list中添加图片
        self.image_num = 0#用来记录while True的次数,当次数达到一定值时才显示一张爆炸的图,然后清空,,当这个次数再次达到时,再显示下一个爆炸效果的图片
        self.image_index = 0#用来记录当前要显示的爆炸效果的图片的序号

    def __crate_images(self):
        self.bomb_list.append(pygame.image.load("./feiji/hero_blowup_n1.png"))
        self.bomb_list.append(pygame.image.load("./feiji/hero_blowup_n2.png"))
        self.bomb_list.append(pygame.image.load("./feiji/hero_blowup_n3.png"))
        self.bomb_list.append(pygame.image.load("./feiji/hero_blowup_n4.png"))

    def display(self):
        """显示玩家的飞机"""
        #如果被击中,就显示爆炸效果,否则显示普通的飞机效果
        if self.hit == True:
            self.screen.blit(self.bomb_list[self.image_index], (self.x, self.y))
            self.image_num += 1
            if self.image_num == 7:
                self.image_num = 0
                self.image_index += 1
            if self.image_index > 3:
                time.sleep(1)
                sys.exit()#调用exit让游戏退出
                #self.image_index = 0
        else:
            #检测英雄飞机的运动方向
            if self.offset < 0:
                self.x -= 3
            elif self.offset > 0:
                self.x += 3

            self.screen.blit(self.image, (self.x, self.y))

        # 检测英雄飞机的 大炮开关是否打开
        if self.switch == True:
            self.fire()

        #不管玩家飞机是否被击中,都要显示发射出去的子弹,判断子弹的位置,如果子弹越界,把这个子弹对象添加到临时的列表中
        bullet_temp_list =[]
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.y < 10:
                bullet_temp_list.append(bullet)

        #越界的子弹从内存里面删除掉
        for temp in bullet_temp_list:
            self.bullet_list.remove(temp)

    def fire(self):
        """通过创建一个子弹对象,完成发射子弹"""
        print("-----1----")
        if self.bullet_list == []:
            bullet = Bullet(self.screen, self.x, self.y) #创建第一个子弹对象
            self.bullet_list.append(bullet)
        else:
            if self.bullet_list[-1].y  < 650:
                bullet = Bullet(self.screen, self.x, self.y)  # 满足条件之后 创建一个子弹对象,添加到列表中
                self.bullet_list.append(bullet)

    def bomb(self):
        self.hit = True

class Bullet(object):
    '''子弹类'''
    def __init__(self, screen_temp, x_temp, y_temp):
        self.x = x_temp+40
        self.y = y_temp-20
        self.image = pygame.image.load("./feiji/bullet.png")
        self.screen = screen_temp
        
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= 5

class EnemyPlane(object):
    '''敌人飞机类'''
    def __init__(self, screen_temp):
        self.x = 0
        self.y = 0
        self.image = pygame.image.load("./feiji/enemy0.png")
        self.screen = screen_temp
        #self.bullet_list = []#用来存储子弹对象的引用
        self.direction = "right"#用来设置这个飞机默认的移动方向

    def display(self):
        """显示敌人的飞机"""
        self.screen.blit(self.image,(self.x, self.y))

    def move(self):

        if self.direction == "right":
            self.x+=2
        elif self.direction == "left":
            self.x-=2

        if self.x>480-50:
            self.direction="left"
        elif self.x<0:
            self.direction="right"

def key_control(hero_temp):
    #获取事件，比如按键等
    for event in pygame.event.get():

        #判断是否是点击了退出按钮
        if event.type == QUIT:
            print("exit")
            sys.exit()
        #判断是否是按下了键
        elif event.type == KEYDOWN:
            #检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                hero_temp.offset = -2

            #检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero_temp.offset = 2

            #检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')
                hero_temp.switch = True
            elif event.key == K_b:
                print('b')
                hero_temp.bomb()

        elif event.type == KEYUP:
            if event.key == K_a or event.key == K_LEFT or event.key == K_d or event.key == K_RIGHT:
                hero_temp.offset = 0
            elif event.key == K_SPACE:
                hero_temp.switch = False

def main():
    #色深：用bit数来表示。色深用2的幂指数来表示，bit数越高，代表能表示的颜色种类越多。24bit 可显示16777216种色彩（接近人眼能分辨的极限）
    # 除了24bit外，还有32bit和48bit
    screen = pygame.display.set_mode((480,852),0,32)
    background = pygame.image.load("./feiji/background.png")

    #创建玩家飞机
    hero = Hero(screen)

    #创建敌机
    enemy = EnemyPlane(screen)

    while True:
        screen.blit(background,(0,0))
        hero.display()
        enemy.display()
        enemy.move()
        pygame.display.update()
        key_control(hero)
       
if __name__ == "__main__":
    main()

