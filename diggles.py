"""
Clone of 2048 game.
By Brandon Sorrow
"""

import poc_2048_gui, random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def tile_walk(start_cell, direction, num_steps):
    """
    Helper function that returns a list of points based on a
    starting point and a direction.
    """
    
    templst = []
    for step in range(num_steps):
        row = start_cell[0] + step * direction[0]
        col = start_cell[1] + step * direction[1]
        templst.append((row, col))
        
    return templst
        

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    
    result_list = pusher(line)
    
    result_list = adder(result_list)
    
    result_list = pusher(result_list)
    
            
            
        
    return result_list




def pusher(lst):
    """
    A Helper Function that takes all non zero numbers and
    pushes them to the front of the list.
    """
    
    sorted_list = []
    
    for dummy_num in range(len(lst)):
        if lst[dummy_num] != 0:
            sorted_list.append(lst[dummy_num])
            
    for dummy_i in range((len(lst)) - (len(sorted_list))):
        sorted_list.append(0)
        
    return sorted_list
        
def adder(addee):
    """
    Helper Function that takes a list and adds all pairs of
    adjacent numbers together.
    """
    added = addee
    for dummy_num2 in range(len(addee)):
        if dummy_num2 != (len(addee) - 1):
            if added[dummy_num2] == added[dummy_num2 + 1]:
                added[dummy_num2] *= 2
                added[dummy_num2 + 1] = 0
            
            
    return added


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.grid = None
        
        # Computation of indicies for the move() dict
        
        self.ind_dic = self.dict_gen()
       
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.grid = [[row + col for col in range(self.grid_width)]
                           for row in range(self.grid_height)]
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                self.grid[row][col] = 0
        
        
        self.new_tile()
        self.new_tile()
    
    def dict_gen(self):
        """
        Generates a dictionary of indicies for use in the 
        move() function.
        """
        dicty = {UP: [], DOWN: [], LEFT: [], RIGHT: []}
        lstup = []
        lstdwn = []
        lstleft = []
        lstright = []
        for foob in range(self.grid_width):
            lstup.append((0, foob))
        dicty[UP] = lstup


        for ambulance in range(self.grid_width):
            lstdwn.append(((self.grid_height - 1), ambulance))
        dicty[DOWN] = lstdwn

        for busy in range(self.grid_height):
            lstleft.append((busy, 0))
        dicty[LEFT] = lstleft

        for exxxxtralongnaaaameee in range(self.grid_height):
            lstright.append((exxxxtralongnaaaameee, (self.grid_width - 1)))
        dicty[RIGHT] =lstright
        
        return dicty
        

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str(self.grid)
        
    def get_grid_height(self):
        """
        Get the height of the board.
        """
        
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self.grid_width
    

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        count = 0
        
        #Start by grabbing the initial tiles and iterating over them.
        for point in self.ind_dic[direction]:
                
            #Now, walk in the correct direction one row at a time and
            # store those tile's coordinates in a temp list.
            if direction == UP or direction == DOWN:
                tmplst = tile_walk(point, OFFSETS[direction], self.grid_height)
            else:
                tmplst = tile_walk(point, OFFSETS[direction], self.grid_width)
            
            lsty = []
            
            #Now grab the values of the tiles in the temp list.
            for dummyi in range(len(tmplst)):
                
                for dummyj in range(len(tmplst[dummyi])-1):
                    
                    jiggy = self.get_tile(tmplst[dummyi][dummyj], tmplst[dummyi][dummyj+1])
                    
                    lsty.append(jiggy)
                
            #Merge those values and check for changes.
            
            copy_lst = lsty
            lsty = merge(lsty)
            
            if copy_lst != lsty:
                count = count + 1
           
                
            
            #Now iterate back over the list and update the grid
            for indigo in range(len(tmplst)):
                for jasper in range(len(tmplst[indigo])-1):
                    self.set_tile(tmplst[indigo][jasper],
                                  tmplst[indigo][jasper+1],
                                  lsty[indigo])
            
        # Add a new tile if the tiles moved.
        if count > 0:
            self.new_tile()
     
        

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        while True:
        
            row = random.randint(0, self.grid_height - 1)
            col = random.randint(0, self.grid_width - 1)
        
            elements = [2] * 90 + [4] * 10
        
        
        
        
        
            if self.grid[row][col] == 0:
                self.grid[row][col] = random.choice(elements)
                break

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        
        return self.grid[row][col] 


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))






