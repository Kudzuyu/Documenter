# !/usr/bin/env python
# -*- coding: utf-8 -*-

from bearlibterminal import terminal
import numpy as np

WINWIDTH = 100   # ウィンドウの幅
WINHEIGHT = 30  # ウィンドウの高さ。

MAPWIDTH = 40
MAPHEIGHT = 20
FONT = "font: font/M+_NerdMono_Win.ttf"

Map = np.zeros((WINWIDTH, WINHEIGHT))
terminal.open()


terminal.set("window:size=" + str(WINWIDTH) + "x" + str(WINHEIGHT) +
             ", title='Documenter'")
terminal.set(FONT + ", size=8x16")


class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        terminal.layer(2)
        terminal.printf(self.x, self.y, "@")
        terminal.layer(0)
        terminal.refresh()

    def erase(self):
        terminal.layer(2)
        terminal.printf(self.x, self.y, " ")
        terminal.layer(0)
        terminal.refresh()

    def moveright(self):
        if self.x < MAPWIDTH - 1 and self.ismovable(self.x + 1, self.y):
            self.erase()
            self.x += 1
            self.show()

    def moveleft(self):
        if self.x > 0 and self.ismovable(self.x - 1, self.y):
            self.erase()
            self.x -= 1
            self.show()

    def moveup(self):
        if self.y > 0 and self.ismovable(self.x, self.y - 1):
            self.erase()
            self.y -= 1
            self.show()

    def movedown(self):
        if self.y < MAPHEIGHT - 1 and self.ismovable(self.x, self.y + 1):
            self.erase()
            self.y += 1
            self.show()

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
            randx = np.random.randint(MAPWIDTH)
            randy = np.random.randint(MAPHEIGHT)
            Map[randx][randy] = 1
            terminal.printf(randx, randy, self.ch)
        terminal.refresh()


def Coord(obj):
    terminal.layer(0)
    terminal.bkcolor("black")
    terminal.printf(0, MAPHEIGHT - 1, '{0:2d},{1:2d}'.format(obj.x, obj.y))
    terminal.refresh()


def game(obj):
    obj.generete(10, 10, 15, 15, '#')
    obj.generete(13, 13, 17, 17, '*')


def pause():
    pass


def settings():
    terminal.clear()
    terminal.printf(10, 0, "Settigns")
    terminal.refresh()
    while True:
        key = terminal.read()
        if key == terminal.TK_ESCAPE:
            break


def title():
    options = [[15, "Play"], [45, "Settings"], [80, "Quit"]]
    selected = 0
    terminal.clear()
    terminal.set("title font: font/Erika_Ormig.ttf, size=160x320, spacing=6x1")
    terminal.printf(18, 6, "[font=title]Documenter")
    while True:
        selected = selected % len(options)
        for i in range(len(options)):
            if i == selected:
                terminal.color("orange")
            else:
                terminal.color("white")
            terminal.printf(options[i][0], 20, options[i][1])
        terminal.refresh()
        key = terminal.read()
        if key == terminal.TK_CLOSE:
            terminal.close()
            return 'Quit'
        elif key == terminal.TK_RIGHT:
            selected += 1
        elif key == terminal.TK_LEFT:
            selected -= 1

        elif key == terminal.TK_ENTER:
            return options[selected][1]


def main():
    terminal.clear()
    wall = mapobject('#')
    wall.generete(40)
    Coord(pl)
    while True:
        key = terminal.read()
        if key == terminal.TK_CLOSE:
            terminal.close()
            return 'Quit'
        elif key == terminal.TK_ESCAPE:
            pause()
        terminal.layer(2)
        terminal.color("red")
        pl.move(key)
        terminal.color("white")
        terminal.layer(0)


def title_game_loop():
    while True:
        opr = title()
        if opr == 'Quit':
            break
        elif opr == 'Settings':
            settings()
        elif opr == 'Play':
            play = main()
            if play == 'Quit':
                break


pl = Player(0, 0)

if __name__ == "__main__":
    title_game_loop()

