'''
    Yu Lin
    CS 5001/5003 Spring 2019
    Homework 7 (space invaders)
    Apr 2 2019
'''
import unittest
from enemy import Enemy
from enemy import Enemy_Fleet
from hero import Hero
from ammo import Ammo

class TestAmmo(unittest.TestCase):
    def test_init(self):
        ammo = Ammo (3, 5)
        self.assertEqual(ammo.pos_x, 3)
        self.assertEqual(ammo.pos_y, 5)
        self.assertEqual(ammo.color, 'red')
        self.assertFalse(ammo.used)
        
        ammo = Ammo (-335,-596)
        self.assertEqual(ammo.pos_x, -335)
        self.assertEqual(ammo.pos_y, -596)
        self.assertEqual(ammo.color, 'red')
        self.assertFalse(ammo.used)

        ammo = Ammo (0,0)
        self.assertEqual(ammo.pos_x, 0)
        self.assertEqual(ammo.pos_y, 0)
        self.assertEqual(ammo.color, 'red')
        self.assertFalse(ammo.used)
        

class test_enemy(unittest.TestCase):
    def test_init(self):    
        enemy = Enemy ((600, 700), 45, 14, 46, 38)
        self.assertEqual(enemy.space, (600,700))
        self.assertEqual(enemy.ship_shape, 'triangle')
        self.assertEqual(enemy.pos_x, 45)
        self.assertEqual(enemy.pos_y, 14)
        self.assertEqual(enemy.hori_speed ,46)
        self.assertEqual(enemy.vert_speed, 38)
        


class test_enemy_fleet(unittest.TestCase):
    def test_init(self):
        enemy_fleet = Enemy_Fleet(48, canvas = (600, 700))
        self.assertEqual(enemy_fleet.space, (600, 700))
        self.assertEqual(enemy_fleet.count, 48)
   
            
class test_hero(unittest.TestCase):
    def test_init(self):
        hero = Hero((400,355),'triangle','orange', 35, 57, 34)
        self.assertEqual(hero.ship_shape, 'triangle')
        self.assertEqual(hero.ship_color, 'orange')
        self.assertEqual(hero.speed, 35)
        self.assertEqual(hero.pos_x, 57)
        self.assertEqual(hero.pos_y, 34)
        
    

def main():
    unittest.main()
main()
