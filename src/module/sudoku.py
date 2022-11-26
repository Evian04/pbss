from src.module.cell import Cell
from src.module.utils import get_index_as


class Sudoku:
    """ Contains the functions that apply directly to the sudoku """
    
    def __init__(self, content: list[list[str]]):
        self.content = content
        
    def solve(self): pass

    def set(self, box: Cell, value: str):
        if not value in [str(n + 1) for n in range(9)]: # = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            quit(f"Error function set : invalid value entered : {value}")
        
        self.content[box.get_a()][box.get_b()] = value

    def unset(self, box: Cell):
        self.content[box.get_a()][box.get_b()] = " "

    def is_valid(self): pass

    def first_empty_cell(self) -> Cell:
        """ Return the first empty cell """
        
        # for index_line in range(len(self.content)):
        #     for index_cell in range(len(self.content[index_line])):
        #         if self.content[index_line][index_cell] == " ":
        #             return Cell(" ", index_line, index_cell)
        for line in self.get_as("line"):
            for num in line:
                if self.content[line][num.index()] == " ":
                    return Cell(" ", line, num.index())

    def is_full(self) -> bool:
        """ Check if sudoku is full """
        for line in self.get_as("line"):
            for num in line:
                if num == " ":
                    return False
        return True
    
    def get_content(self, kind: str) -> list[list[str]]:
        """ Return the content with kind"""
        content = [["" for b in range(9)] for a in range(9)] # create a list of list of empty string, that's the future content to return
        
        for index_part in range(len(self.content)):
            for index_cell in range(len(self.content[index_part])):
                index_converted = get_index_as(index_part, index_cell, kind)
                content[index_converted[0]][index_converted[1]] = self.content[index_part][index_cell]
        
        return content