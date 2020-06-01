import pygame as pg
from pygame import mixer

vec = pg.math.Vector2

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (106, 55, 5)

# game settings
WIDTH = 1024  # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Tilemap Demo"
BGCOLOR = BROWN

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

WALL_IMG1 = r'PNG\Tiles\tile_131.png'
WALL_IMG2 = r'PNG\Tiles\tile_02.png'
WALL_IMG3 = r'PNG\Tiles\tile_03.png'
WALL_IMG4 = r'PNG\Tiles\tile_04.png'
WALL_IMG5 = r'PNG\Tiles\tile_05.png'
WALL_IMG6 = r'PNG\Tiles\tile_06.png'
WALL_IMG7 = r'PNG\Tiles\tile_07.png'
WALL_IMG8 = r'PNG\Tiles\tile_08.png'
WALL_IMG9 = r'PNG\Tiles\tile_09.png'
WALL_IMG10 = r'PNG\Tiles\tile_10.png'
WALL_IMG11 = r'PNG\Tiles\tile_11.png'
WALL_IMG12 = r'PNG\Tiles\tile_12.png'
WALL_IMG13 = r'PNG\Tiles\tile_13.png'
WALL_IMG14 = r'PNG\Tiles\tile_14.png'
WALL_IMG15 = r'PNG\Tiles\tile_15.png'
WALL_IMG16 = r'PNG\Tiles\tile_16.png'
WALL_IMG17 = r'PNG\Tiles\tile_17.png'
WALL_IMG18 = r'PNG\Tiles\tile_18.png'
WALL_IMG19 = r'PNG\Tiles\tile_19.png'
WALL_IMG20 = r'PNG\Tiles\tile_20.png'
WALL_IMG21 = r'PNG\Tiles\tile_21.png'
WALL_IMG22 = r'PNG\Tiles\tile_22.png'
WALL_IMG23 = r'PNG\Tiles\tile_23.png'
WALL_IMG24 = r'PNG\Tiles\tile_24.png'
WALL_IMG25 = r'PNG\Tiles\tile_25.png'
WALL_IMG26 = r'PNG\Tiles\tile_26.png'
# WALL_IMG27 = r'PNG\Tiles\tile_27.png'
WALL_IMG28 = r'PNG\Tiles\tile_28.png'
WALL_IMG29 = r'PNG\Tiles\tile_29.png'
WALL_IMG30 = r'PNG\Tiles\tile_30.png'
WALL_IMG31 = r'PNG\Tiles\tile_31.png'
WALL_IMG32 = r'PNG\Tiles\tile_32.png'
WALL_IMG33 = r'PNG\Tiles\tile_33.png'
WALL_IMG34 = r'PNG\Tiles\tile_34.png'
WALL_IMG35 = r'PNG\Tiles\tile_35.png'
WALL_IMG36 = r'PNG\Tiles\tile_36.png'
WALL_IMG37 = r'PNG\Tiles\tile_37.png'
WALL_IMG38 = r'PNG\Tiles\tile_38.png'
WALL_IMG39 = r'PNG\Tiles\tile_39.png'
WALL_IMG40 = r'PNG\Tiles\tile_40.png'
WALL_IMG41 = r'PNG\Tiles\tile_41.png'
WALL_IMG42 = r'PNG\Tiles\tile_42.png'
WALL_IMG43 = r'PNG\Tiles\tile_43.png'
WALL_IMG44 = r'PNG\Tiles\tile_44.png'
WALL_IMG45 = r'PNG\Tiles\tile_45.png'
WALL_IMG46 = r'PNG\Tiles\tile_46.png'
WALL_IMG47 = r'PNG\Tiles\tile_47.png'
WALL_IMG48 = r'PNG\Tiles\tile_48.png'
WALL_IMG49 = r'PNG\Tiles\tile_49.png'
WALL_IMG50 = r'PNG\Tiles\tile_50.png'
WALL_IMG51 = r'PNG\Tiles\tile_51.png'
WALL_IMG52 = r'PNG\Tiles\tile_52.png'
WALL_IMG53 = r'PNG\Tiles\tile_53.png'
WALL_IMG54 = r'PNG\Tiles\tile_54.png'
WALL_IMG55 = r'PNG\Tiles\tile_55.png'
WALL_IMG56 = r'PNG\Tiles\tile_56.png'
WALL_IMG57 = r'PNG\Tiles\tile_57.png'
WALL_IMG58 = r'PNG\Tiles\tile_58.png'
WALL_IMG59 = r'PNG\Tiles\tile_59.png'
WALL_IMG60 = r'PNG\Tiles\tile_60.png'
WALL_IMG61 = r'PNG\Tiles\tile_61.png'
WALL_IMG62 = r'PNG\Tiles\tile_62.png'
WALL_IMG63 = r'PNG\Tiles\tile_63.png'
WALL_IMG64 = r'PNG\Tiles\tile_64.png'
WALL_IMG65 = r'PNG\Tiles\tile_65.png'
WALL_IMG66 = r'PNG\Tiles\tile_66.png'
WALL_IMG67 = r'PNG\Tiles\tile_67.png'
WALL_IMG68 = r'PNG\Tiles\tile_68.png'
WALL_IMG69 = r'PNG\Tiles\tile_69.png'
WALL_IMG70 = r'PNG\Tiles\tile_70.png'
WALL_IMG71 = r'PNG\Tiles\tile_71.png'
WALL_IMG72 = r'PNG\Tiles\tile_72.png'
WALL_IMG73 = r'PNG\Tiles\tile_73.png'
WALL_IMG74 = r'PNG\Tiles\tile_74.png'
WALL_IMG75 = r'PNG\Tiles\tile_75.png'
WALL_IMG76 = r'PNG\Tiles\tile_76.png'
WALL_IMG77 = r'PNG\Tiles\tile_77.png'
WALL_IMG78 = r'PNG\Tiles\tile_78.png'
WALL_IMG79 = r'PNG\Tiles\tile_79.png'
WALL_IMG80 = r'PNG\Tiles\tile_80.png'
WALL_IMG81 = r'PNG\Tiles\tile_81.png'
WALL_IMG82 = r'PNG\Tiles\tile_82.png'
WALL_IMG83 = r'PNG\Tiles\tile_83.png'
WALL_IMG84 = r'PNG\Tiles\tile_84.png'
WALL_IMG85 = r'PNG\Tiles\tile_85.png'
WALL_IMG86 = r'PNG\Tiles\tile_86.png'
WALL_IMG87 = r'PNG\Tiles\tile_87.png'
WALL_IMG88 = r'PNG\Tiles\tile_88.png'
WALL_IMG89 = r'PNG\Tiles\tile_89.png'
WALL_IMG90 = r'PNG\Tiles\tile_90.png'
WALL_IMG91 = r'PNG\Tiles\tile_91.png'
WALL_IMG92 = r'PNG\Tiles\tile_92.png'
WALL_IMG93 = r'PNG\Tiles\tile_93.png'
WALL_IMG94 = r'PNG\Tiles\tile_94.png'
WALL_IMG95 = r'PNG\Tiles\tile_95.png'
WALL_IMG96 = r'PNG\Tiles\tile_96.png'
WALL_IMG97 = r'PNG\Tiles\tile_97.png'
WALL_IMG98 = r'PNG\Tiles\tile_98.png'
WALL_IMG99 = r'PNG\Tiles\tile_99.png'
MAP_IMG = r'sprite_tiles.tmx'

# player settings
PLAYER_HEALTH = 2000
PLAYER_SPEED = 300
PLAYER_ROT_SPEED = 250
PLAYER_IMG = r'PNG\MAN BLUE\manBlue_gun.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)

# Gun setting
BULLET_IMG = r'PNG\star2.png'
BULLET_SPEED = 500
BULLET_LIFETIME = 1000
BULLET_RATE = 150
BARREL_OFFSET = vec(30, 10)
KICKBACK = 200
GUN_SPREAD = 5
BULLET_DAMAGE = 10

# Mob setting
MOB_IMG = r'PNG\Zombie 1\zoimbie1_hold.png'
MOB_SPEED = 150
MOB_HIT_RECT = pg.Rect(0, 0, 30, 30)
MOB_HEALTH = 100
MOB_DAMAGE = 10
MOB_KNOCKBACK = 20

# sound try
