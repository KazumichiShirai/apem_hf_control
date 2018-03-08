#! /usr/bin/env python
# coding: utf-8
# coding=utf-8
# -*- coding: utf-8 -*-
# vim: fileencoding=utf-8
import time
import pygame
from pygame.locals import *

print (pygame.version.ver)
pygame.init()
pygame.joystick.init()
try:
        j = pygame.joystick.Joystick(0) # create a joystick instance
        j.init() # init instance
        print('Joystick ' , j.get_name())
        print("axis_number:", j.get_numaxes())
except pygame.error:
        print ('No Joystick')
pygame.display.init()
msg = ''
limit = 50
while 1:
        e = pygame.event.poll() # イベントチェック
        # Joystick関連のイベントチェック
        if e.type == pygame.locals.JOYAXISMOTION: # 7
            x , y , z= j.get_axis(0), j.get_axis(1), j.get_axis(2)
            print ("x:",x,",y:",y,"z:",z)
            pygame.event.pump()
        elif e.type == pygame.locals.JOYBUTTONDOWN: # 10
            print ("button-down:",e.button)
        elif e.type == pygame.locals.JOYBUTTONUP: # 11
            print ("button-up:",e.button)
        elif e.type == pygame.locals.NOEVENT:
            time.sleep(0.02)
        else:
            print(e.type)
# end of file
