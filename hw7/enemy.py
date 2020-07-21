'''
    Yu Lin
    CS 5001/5003 Spring 2019
    Homework 7 (space invaders)
    Apr 2 2019

    Contains two classes
    Enemy class and Enemy_Fleet class
    Enemy_Fleet class uses Enenmy class
    
'''



import turtle
import random

class Enemy:
    def __init__(self,
                 canvas = (600, 700),
                 pos_x = 0,
                 pos_y = 0,
                 hori_speed = 10,
                 vert_speed = 70):
        
        self.ship = turtle.Turtle()
        self.space = canvas
        self.ship_shape = 'triangle'
        self.ship_color = 'blue'
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hori_speed = hori_speed
        self.vert_speed = vert_speed
        self.alive = True

    def render (self):
        self.ship.speed(0)
        self.ship.penup()
        self.ship.goto(self.pos_x, self.pos_y)
        self.ship.color(self.ship_color)
        self.ship.pendown()
        self.ship.begin_fill()
        self.ship.shape('triangle')
        self.ship.setheading (270)
        self.ship.penup()
        self.ship.speed(3)
        return
    
    def move_right (self):
        self.pos_x += self.hori_speed
        self.ship.goto(self.pos_x, self.pos_y)
        return self.pos_x

    def move_down (self):
        self.pos_y -= self.vert_speed
        self.ship.goto(self.pos_x, self.pos_y)
        return self.pos_y

    def generate_position(self):
        x = int (self.space [0] / 2)
        y = int (self.space [1] /2)
        return [random.randint (-x, x) , random.randint (int(y/3), y)]

    def stroll_to_coordinate (self, coordinate):
        print (coordinate)
        for i in range(2):
            self.pos_x += coordinate[0] / 2
            self.pos_y += coordinate[1] / 2
            self.render()
        return [int(self.ship.position()[0]), int(self.ship.position()[1])]
        
    def destroyed (self):
        self.alive = False
        self.ship.hideturtle()
        self.ship.speed(0)
    
    

class Enemy_Fleet:
    def __init__(self, count = 10, canvas = (600, 700)):
        self.space = canvas
        self.count = count
        self.enemies = []
        return

    def create_formation (self):
        for i in range(self.count):
            new_ship = Enemy(self.space)
            self.enemies.append(new_ship)
            starting_coordinate = new_ship.generate_position()
            new_ship.stroll_to_coordinate(starting_coordinate)
        return 

    def deploy_attack (self, hero):
        for i in range(len(self.enemies)):
            unit = self.enemies.pop()
            if unit.pos_x <= ((self.space [0] / 2) - 10):
                unit.move_right()
                if unit.alive == True:
                    if (unit.pos_x - 20) < hero.pos_x < (unit.pos_x + 20):
                        if (unit.pos_y - 20) < hero.pos_y < (unit.pos_y + 20):
                           hero.destroyed()
            else:
                unit.ship.speed(0)
                unit.pos_x = (-(self.space [0] / 2))
                unit.move_down()
                unit.ship.speed(3)
            self.enemies.insert(0,unit)
        return

    

