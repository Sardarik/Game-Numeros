import pygame as pg
#pygame is a Python wrapper for the SDL library, which stands for Simple DirectMedia Layer
from configurations import *

class Sign(pg.sprite.Sprite):
    def __init__(self, cell_size: int, points: str, field_name: str, file_name: str):
        super().__init__()
        picture = pg.image.load(Signs_path + file_name)
        self.image = pg.transform.scale(picture,(cell_size,cell_size))
        self.rect = self.image.get_rect()
        self.points = points
        self.field_name = field_name

    def move_to_cell(self,cell):
        self.rect = cell.rect.copy()
        self.field_name = cell.field_name

    def move_to_hand_cell(self,hand_cell):
        self.rect = hand_cell.rect.copy()
        self.field_name = hand_cell.field_name


class Sign_0(Sign):
    def __init__(self, cell_size: int, points: str, field: str):
        super().__init__(cell_size, points, field, '0.png')


class Sign_1(Sign):
    def __init__(self, cell_size: int, points: str, field: str):
        super().__init__(cell_size, points, field, '1.png')
    
class Sign_2(Sign):
    def __init__(self, cell_size: int, points: str, field: str):
        super().__init__(cell_size, points, field, '2.png')

class Sign_3(Sign):
    def __init__(self, cell_size: int, points: str, field: str):
        super().__init__(cell_size, points, field, '3.png')

class Sign_4(Sign):
    def __init__(self, cell_size: int, points: str, field: str):
        super().__init__(cell_size, points, field, '4.png')

class Sign_5(Sign):
    def __init__(self, cell_size: int, points: str, field: str):
        super().__init__(cell_size, points, field, '5.png')


class Sign_6(Sign):
    def __init__(self, cell_size: int, points: str, field: str):
        super().__init__(cell_size, points, field, '6.png')


class Sign_7(Sign):
    def __init__(self, cell_size: int, points: str, field: str):
        super().__init__(cell_size, points, field, '7.png')


class Sign_8(Sign):
    def __init__(self, cell_size: int, points: str, field: str):
        super().__init__(cell_size, points, field, '8.png')


class Sign_9(Sign):
    def __init__(self, cell_size: int, points: str, field: str):
        super().__init__(cell_size, points, field, '9.png')


class Sign_plus(Sign):
    def __init__(self, cell_size: int, points: str, field: str):
        super().__init__(cell_size, points, field, '+.png')


class Sign_minus(Sign):
    def __init__(self, cell_size: int, points: str, field: str):
        super().__init__(cell_size, points, field, '-.png')


class Sign_product(Sign):
    def __init__(self, cell_size: int, points: str, field: str):
        super().__init__(cell_size, points, field, '*.png')

class Sign_divide(Sign):
    def __init__(self, cell_size: int, points: str, field: str):
        super().__init__(cell_size, points, field, ':.png')

class Sign_equal(Sign):
    def __init__(self, cell_size: int, points: str, field: str):
        super().__init__(cell_size, points, field, '=.png')
