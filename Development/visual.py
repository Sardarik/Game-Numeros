from sign_items import *
import board_data
pg.init()
Font_text = pg.font.SysFont('applemyungjo', 30)

class Field:
    def __init__(self, parent_surface: pg.Surface, 
                 cell_count: int=Cell_count, cell_size: int = Cell_size):
        self.__screen = parent_surface
        self.__table = board_data.playboard
        self.__count = cell_count
        self.__size = cell_size
        self.__signs_types = Signs_types
        self.__all_cells = pg.sprite.Group()
        self.__all_signs = pg.sprite.Group()
        self.__pressed_cell = None
        self.__picked_sign = None
        self.__draw_field()
        self.__draw_all_signs()
        pg.display.update()


    def __draw_field(self):
        total_width = self.__count * self.__size
        self.__all_cells = self.__create_all_cells()
        cell_offset = ((Window_size[0] - total_width) // 2, (Window_size[1]-total_width) // 2 - 25)
        self.__draw_cells_on_playboard(cell_offset)


    def __create_all_cells(self):
        group = pg.sprite.Group()
        for x in range(self.__count):
            for y in range(self.__count):
                if x == Cell_count//2 and y == x:
                    cell = Cell(
                        1,
                        self.__size,
                        (x,y),
                        'F' + str(self.__count-y) + str(self.__count-x)
                        )
                else:
                    cell = Cell(
                        0,
                        self.__size,
                        (x,y),
                        'F' + str(self.__count-y) + str(self.__count-x)
                        )
                group.add(cell)
        return group
    
    
    def __draw_cells_on_playboard(self,cell_offset):
        for cell in self.__all_cells:
            cell.rect.x += cell_offset[0]
            cell.rect.y += cell_offset[1]
        self.__all_cells.draw(self.__screen)


    def __draw_all_signs(self):
        self.__setup_board()
        self.__all_signs.draw(self.__screen)


    def __setup_board(self):
        for j, row in enumerate(self.__table):
            for i, field_value in enumerate(row):
                if field_value != 0:
                    sign = self.__create_sign(field_value, (j,i))
                    self.__all_signs.add(sign)
        for sign in self.__all_signs:
            for cell in self.__all_cells:
                if sign.field_name == cell.field_name:
                    sign.rect = cell.rect.copy()
    

    def __create_sign(self, sign_symbol: str, table_coord: tuple):
        field_name = self.__to_field_name(table_coord)
        sign_tuple = self.__signs_types[sign_symbol]
        classname = globals()[sign_tuple[0]]
        return classname(self.__size, sign_tuple[1], field_name)


    def __to_field_name(self, table_coord: tuple):
        return 'F' + str(self.__count - table_coord[0]) + str(self.__count - table_coord[1])


    def __get_cell(self, position:tuple):
        for cell in self.__all_cells:
            if cell.rect.collidepoint(position):
                return cell
        return None
    

    def btn_down(self, button_type: int, position: tuple):
        self.__pressed_cell = self.__get_cell(position)

    
    def btn_up(self, button_type: int, position:tuple):
        released_cell = self.__get_cell(position)
        if (released_cell is not None) and (released_cell == self.__pressed_cell):
            if button_type == 1:
                self.__pick_cell(released_cell)
        self.__grand_update()

    def __pick_cell(self,cell):
        if self.__picked_sign is None:
            for sign in self.__all_signs:
                if sign.field_name == cell.field_name:
                    self.__picked_sign = sign
                    break
            if sign is not None:
                self.__picked_sign = sign
        else:
            self.__picked_sign.rect=cell.rect
            self.__picked_sign.field__name = cell.field_name
            self.__picked_sign = None

    def __grand_update(self):
        self.__all_cells.draw(self.__screen)
        self.__all_signs.draw(self.__screen)
        pg.display.update()


class Hand:
    def __init__(self, parent_surface: pg.Surface, 
                 cell_count: int = Cell_count, cell_size: int = Cell_size,
                 hand_cell_count_elements: int=Hand_cell_count_elements, hand_cell_count_lines: int=Hand_cell_count_lines):
        self.__screen = parent_surface
        self.__hand_table = board_data.handboard
        self.__count = cell_count
        self.__size = cell_size
        self.__signs_types = Signs_types
        self.__all_hand_cells = pg.sprite.Group()
        self.__all_signs = pg.sprite.Group()
        self.__hand_count_elements = hand_cell_count_elements
        self.__hand_count_lines = hand_cell_count_lines
        self.__pressed_hand_cell = None
        self.__picked_hand_sign = None
        self.__draw_hand()
        self.__draw_all_signs()
        pg.display.update()

    def __draw_hand(self):
        self.__all_hand_cells = self.__create_hand()
        hand_cell_offset  = ((Window_size[0] - self.__hand_count_elements*self.__size) // 2,(Window_size[1])//2 + self.__count*self.__size//2 - 15)

        self.__draw_hand_cells(hand_cell_offset)


    def __create_hand(self):
        group = pg.sprite.Group()
        for x in range(self.__hand_count_elements):
            for y in range(self.__hand_count_lines):
                hand_cell = Cell(
                    0,
                    self.__size,
                    (x,y),
                    'H'+str(self.__hand_count_lines-y)+str(self.__hand_count_elements-x)
                )
                group.add(hand_cell)
        return group


    def __draw_hand_cells(self, hand_cell_offset):
        for hand_cell in self.__all_hand_cells:
            hand_cell.rect.x += hand_cell_offset[0]
            hand_cell.rect.y += hand_cell_offset[1]
        self.__all_hand_cells.draw(self.__screen)


    def __draw_all_signs(self):
        self.__setup_board()
        self.__all_signs.draw(self.__screen)


    def __setup_board(self):
        for j, row in enumerate(self.__hand_table):
            for i, field_value in enumerate(row):
                if field_value != 0:
                    sign = self.__create_sign(field_value, (j,i))
                    self.__all_signs.add(sign)
        for sign in self.__all_signs:
            for hand_cell in self.__all_hand_cells:
                if sign.field_name == hand_cell.field_name:
                    sign.rect = hand_cell.rect.copy()
    

    def __create_sign(self, sign_symbol: str, table_coord: tuple):
        field_name = self.__to_field_name(table_coord)
        sign_tuple = self.__signs_types[sign_symbol]
        classname = globals()[sign_tuple[0]]
        return classname(self.__size, sign_tuple[1], field_name)


    def __to_field_name(self, table_coord: tuple):
        return 'H' + str(self.__hand_count_lines - table_coord[0]) + str(self.__hand_count_elements - table_coord[1])

    def __get_hand_cell(self, position:tuple):
        for hand_cell in self.__all_hand_cells:
            if hand_cell.rect.collidepoint(position):
                return hand_cell
        return None

    
    def btn_down(self, button_type: int, position: tuple):
        self.__pressed_hand_cell = self.__get_hand_cell(position)


    
    def btn_up(self, button_type: int, position:tuple):
        released_hand_cell = self.__get_hand_cell(position)
        if (released_hand_cell is not None) and (released_hand_cell == self.__pressed_hand_cell):
            if button_type == 1:
                self.__pick_hand_cell(released_hand_cell)
        self.__grand_update()

    def __pick_hand_cell(self,hand_cell):
        if self.__picked_hand_sign is None:
            for sign in self.__all_signs:
                if sign.field_name == hand_cell.field_name:
                    self.__picked_hand_sign = sign
                    break
            if sign is not None:
                self.__picked_hand_sign = sign
        else:
            self.__picked_hand_sign.rect=hand_cell.rect
            self.__picked_hand_sign.field__name = hand_cell.field_name
            self.__picked_hand_sign = None

    def __grand_update(self):
        self.__all_hand_cells.draw(self.__screen)
        self.__all_signs.draw(self.__screen)
        pg.display.update()




class Cell(pg.sprite.Sprite):
    def __init__(self, color_index: int, size: int, coords: tuple, name: str):
        super().__init__()
        x,y = coords
        self.color = color_index
        self.field_name = name
        self.image = pg.image.load(Img_path+image[color_index])
        self.image = pg.transform.scale(self.image, (size, size))
        self.rect = pg.Rect(x * size, y * size, size, size)



