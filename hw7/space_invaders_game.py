'''
    Yu Lin
    CS 5001/5003 Spring 2019
    Homework 7 (space invaders)
    Apr 2 2019
    
    Main driver for the game 
'''

from enemy import Enemy
from enemy import Enemy_Fleet
from hero import Hero
import turtle

def main ():
    result = 'Game just started'
    score = 0
    canvas = (600, 700)
    turtle.setup(canvas[0]+100, canvas [1]+40)
    turtle.bgcolor("black")
    
    dooms_fleet = Enemy_Fleet(10, canvas)  
    dooms_fleet.create_formation ()
    
    hero = Hero(canvas)
    hero.stroll_to_coordinate ()
    hero.flash()

    turtle.listen()
    turtle.onkey(hero.move_left, "Left")
    turtle.onkey(hero.move_right, "Right")
    turtle.onkey(hero.load_ammos, "space")

    game_in_play = True
    while game_in_play:
        hero.shoot_ammos(dooms_fleet)
        dooms_fleet.deploy_attack(hero)
        dooms_fleet_livestock = [dooms_fleet.enemies[i].alive for i in range(len(dooms_fleet.enemies))]
        print (dooms_fleet_livestock)
         
        if True not in dooms_fleet_livestock:
            game_in_play = False
            winner = 'YOU'
            for value in dooms_fleet_livestock:
                if value == False:
                    score += 10
        if hero.alive == False:
            game_in_play = False
            winner = 'DOOMS FLEET'
            for value in dooms_fleet_livestock:
                if value == False:
                    score += 10
    print ('The winner is', winner)
    print ('Your Score is', score)
main()
