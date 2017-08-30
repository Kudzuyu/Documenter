# !/usr/bin/env python
# -*- coding: utf-8 -*-

from bearlibterminal import terminal
import numpy as np

WINWIDTH = 80   # ウィンドウの幅
WINHEIGHT = 40  # ウィンドウの高さ。

Map = np.zeros((WINWIDTH, WINHEIGHT))
terminal.open()
terminal.set("font: Ricty-Regular.ttf, size=12")
terminal.set("window:size=" + str(WINWIDTH) + "x" + str(WINHEIGHT))


class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        terminal.layer(2)
        terminal.printf(y, x, "@")
        terminal.layer(0)
        terminal.refresh()

    def moveright(self):
        if self.x < WINWIDTH - 1 and self.ismovable(self.x + 1, self.y):
            terminal.printf(self.x, self.y, " ")
            self.x += 1
            terminal.printf(self.x, self.y, "@")
            terminal.refresh()

    def moveleft(self):
        if self.x > 0 and self.ismovable(self.x - 1, self.y):
            terminal.printf(self.x, self.y, " ")
            self.x -= 1
            terminal.printf(self.x, self.y, "@")
            terminal.refresh()

    def moveup(self):
        if self.y > 0 and self.ismovable(self.x, self.y - 1):
            terminal.printf(self.x, self.y, " ")
            self.y -= 1
            terminal.printf(self.x, self.y, "@")
            terminal.refresh()

    def movedown(self):
        if self.y < WINHEIGHT - 1 and self.ismovable(self.x, self.y + 1):
            terminal.printf(self.x, self.y, " ")
            self.y += 1
            terminal.printf(self.x, self.y, "@")
            terminal.refresh()

    def ismovable(self, x, y):
        if Map[x][y] == 0:
            return True
        else:
            return False

    def move(self, char):
        if char == terminal.TK_RIGHT:
            self.moveright()
        elif char == terminal.TK_LEFT:
            self.moveleft()
        elif char == terminal.TK_UP:
            self.moveup()
        elif char == terminal.TK_DOWN:
            self.movedown()


class mapobject():
    def __init__(self, ch):
        self.ch = ch

    def generete(self, num):
        for i in range(num):
            randx = np.random.randint(WINWIDTH)
            randy = np.random.randint(WINHEIGHT)
            Map[randx][randy] = 1
            terminal.printf(randx, randy, self.ch)
        terminal.refresh()


def Coord(obj):
    terminal.layer(0)
    terminal.bkcolor("black")
    terminal.printf(0, WINHEIGHT - 1, '{0:2d},{1:2d}'.format(obj.x, obj.y))
    terminal.refresh()


def game(obj):
    obj.generete(10, 10, 15, 15, '#')
    obj.generete(13, 13, 17, 17, '*')


wall = mapobject('#')
pl = Player(0, 0)

terminal.bkcolor("gray")
wall.generete(4)

while True:
    Coord(pl)
    key = terminal.read()
    if key == terminal.TK_CLOSE:
        break

    terminal.layer(2)
    terminal.color("red")
    pl.move(key)
    terminal.color("white")
    terminal.layer(0)

terminal.close()

