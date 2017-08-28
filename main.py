# !/usr/bin/env python
# -*- coding: utf-8 -*-

import curses


class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        screen.addstr(y, x, "@")

    def moveright(self):
        screen.addstr(self.y, self.x, " ")
        self.x += 1
        screen.addstr(self.y, self.x, "@")
        screen.refresh()

    def moveleft(self):
        screen.addstr(self.y, self.x, " ")
        self.x -= 1
        screen.addstr(self.y, self.x, "@")
        screen.refresh()

    def moveup(self):
        screen.addstr(self.y, self.x, " ")
        self.y -= 1
        screen.addstr(self.y, self.x, "@")
        screen.refresh()

    def movedown(self):
        screen.addstr(self.y, self.x, " ")
        self.y += 1
        screen.addstr(self.y, self.x, "@")
        screen.refresh()


screen = curses.initscr()
curses.noecho()

curses.cbreak()
screen.clear()
screen.keypad(True)

pl = Player(3, 4)

screen.refresh()


if __name__ == '__main__':
    while True:
        char = screen.getch()
        if char == curses.KEY_RIGHT:
            pl.moveright()
        elif char == curses.KEY_LEFT:
            pl.moveleft()
        elif char == curses.KEY_UP:
            pl.moveup()
        elif char == curses.KEY_DOWN:
            pl.movedown()

