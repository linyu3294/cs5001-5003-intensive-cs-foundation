'''
    Yu Lin
    CS 5001/5003 Spring 2019
    Homework 7 (space invaders)
    Apr 2 2019

    Hero class
'''

import turtle
from ammo import Ammo

class Hero:
    def __init__(self,
                 canvas = (600, 700),
                 shape = 'turtle',
                 color = 'purple',
                 speed = 20,
                 pos_x = 0,
                 pos_y = 0):

        
        self.ship = turtle.Turtle()
        self.space = canvas
        self.ship_shape = shape
        self.ship_color = color
        self.speed = speed
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.fired_ammos = []
        self.alive = True
    

    def render (self):
        self.ship.speed(0)
        self.ship.penup()
        self.ship.goto(self.pos_x, self.pos_y)
        self.ship.color(self.ship_color)
        self.ship.pendown()
        self.ship.begin_fill()
        self.ship.shape(self.ship_shape)
        self.ship.setheading (90)
        self.ship.penup()
        self.ship.speed(3)
    
    def stroll_to_coordinate(self, coordinate = "use default"):
        if coordinate == "use default":
            coordinate = (0, -(self.space[1]/2.5))
        for i in range(10):
            self.pos_x += coordinate[0] / 10
            self.pos_y += coordinate[1] / 10
            self.render()
        return [int(self.ship.position()[0]), int(self.ship.position()[1])]

    def move_left(self):
        if self.pos_x >= (-(self.space[0] / 2) + self.speed): 
            self.pos_x -= self.speed 
            self.ship.goto(self.pos_x, self.pos_y)
        return self.pos_x

    def move_right(self):
        if self.pos_x <= ((self.space[0] / 2) - self.speed): 
            self.pos_x += self.speed 
            self.ship.goto(self.pos_x, self.pos_y)
        return self.pos_x

    def flash (self):
        for i in range (40):
            self.ship.color('orange')
            self.ship.color(self.ship_color)

    def destroyed (self):
        self.alive = False
        self.flash()
        self.ship.hideturtle()
        self.ship.speed(0)

    def load_ammos(self):
        ammo = Ammo(self.pos_x, self.pos_y)
        ammo.render()
        self.fired_ammos.append(ammo)

    def shoot_ammos(self, enemy_fleet):
        for i in range(len(self.fired_ammos)):
            ammo = self.fired_ammos.pop()
            if ammo.pos_y <= ((self.space [1])):
                ammo.go_get_em(enemy_fleet)
                self.fired_ammos.insert (0, ammo)

    


    
    

    
  
