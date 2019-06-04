"""Parameters and configs"""

## CONSTANTS ##

WIDTH = 800
HEIGHT = 600
WINDOWSIZE = (WIDTH, HEIGHT)  # size of the window

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 120  # frames per second

playerImg = 'assets/player-saber.png'
tieImg = 'assets/player-tie.png'
enemyImg = 'assets/enemy_eg.png'
enemyBulletImg = 'assets/bullet-enemy.png'
playerBulletImg = 'assets/bullet-player.png'
playerBulletShortImg = 'assets/bullet-player-short.png'

## CONFIGURATIONS ##

playerSpeed = 10  # player moving speed
playerHP = 10  # the lives of the player
enemyHP = 5  # the lives of the enemy

enemyBulletSpeed = 20  # speed of enemy's bullet
playerBulletSpeed = 30  # speed of player's bullet
enemyShootingSpeed = 500  # the time gap between two shootings
enemySpawningSpeed = 5000
maxEnemyCount = 8  # the number of maximum enemies appear in the screen
defenseDistance = 100  # how far could the defense bullet reach
