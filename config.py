"""
This file saves the basic parameters
and the configuration of the game
"""

WIDTH = 800
HEIGHT = 600
windowSize = (WIDTH, HEIGHT)  # size of the window

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 120  # frames per second

playerSpeed = 10  # player moving speed
playerHP = 5  # the lives of the player
enemyHP = 5

enemyBulletSpeed = 20  # speed of enemy's bullet
playerBulletSpeed = 30  # speed of player's bullet
enemyShootingSpeed = 500  # the time gap between two shootings
enemySpawningSpeed = 5000
maxEnemyCount = 8  # the number of maximum enemies appear in the screen

saberImg = 'assets/player-saber.png'
tieImg = 'assets/player-tie.png'
enemyImg = 'assets/enemy_eg.png'
enemyBulletImg = 'assets/bullet-enemy.png'
playerBulletImg = 'assets/bullet-player.png'