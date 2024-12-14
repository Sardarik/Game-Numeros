from random import choice
import pygame as pg
#every constant
FPS = 15
WINDOW_SIZE = [800,750]

IMG_PATH = '/Users/aidasardarova/Documents/HSE/АиП/Numeros/Images/'
ICON = 'icon.png'
IMAGE = ['Cell.png', 'Center_cell.png']
CELL_COUNT = 15
CELL_SIZE = 40
CELL_COLOR = (244,200,133)
LINE_COLOR = (176,144,95)
CENTER_COLOR = (98, 68, 20)
HAND_CELL_COUNT_ELEMENTS = 7
HAND_CELL_COUNT_LINES = 2
all_field_cells = []
SIGNS_PATH = '/Users/aidasardarova/Documents/HSE/АиП/Numeros/Images/Signs/'
SIGNS_ARRAY = ['0','1','2','3','4','5','6','7','8','9','+','-','*',':']
FONT_TEXT = pg.font.SysFont('applemyungjo', 30)

BUTTONS_PATH = '/Users/aidasardarova/Documents/HSE/АиП/Numeros/Images/Buttons/'


VALUE_OF_NUMBER = 1
VALUE_OF_OPERATOR = 2



