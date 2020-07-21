'''
    Yu Lin
    CS 5001/5003 Spring 2019
    Homework 7 (space invaders)
    Apr 2 2019

    Ammo class
    Used by Hero class
'''

from enemy import Enemy
from enemy import Enemy_Fleet
import turtle

class Ammo:
    
    def __init__ (self, pos_x, pos_y):
        self.bullet = turtle.Turtle()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = 'red'
        self.used = False

    def render (self):
        self.bullet.speed(0)
        self.bullet.penup()
        self.bullet.goto(self.pos_x, self.pos_y)
        self.bullet.color(self.color)
        self.bullet.pendown()
        self.bullet.begin_fill()
        self.bullet.shape('circle')
        self.bullet.shapesize(0.5,0.2)
        self.bullet.penup()
        self.bullet.speed(5)
        return

    def go_get_em (self, enemy_fleet):
        self.pos_y += 20
        self.bullet.goto(self.pos_x, self.pos_y)
        for i in range(len(enemy_fleet.enemies)):
            unit = enemy_fleet.enemies.pop()
            if (unit.pos_x - 20) <= self.pos_x <= (unit.pos_x + 20):
                if (unit.pos_y - 15) <= self.pos_y <= (unit.pos_y + 15):
                    if unit.alive == True and self.used ==False:
                        self.hit()
                        unit.destroyed()
            enemy_fleet.enemies.insert(0, unit)
        return self.pos_y

    def hit (self):
        self.used = True
        self.bullet.hideturtle()
        
    
