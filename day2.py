class directions:
	num_dirs = 4
	UP, RIGHT, DOWN, LEFT  = 'U', 'R', 'D', 'L'

class grid:
    def __init__(self, row_widths, shape, invalid_char, valid_char, start_col, start_row):
        self.col = start_col
        self.row = start_row
        self.row_widths = row_widths
        self.invalid_char = invalid_char
        max_cols = -1
        for r_idx in xrange(len(row_widths)):
            max_cols = max(row_widths[r_idx], max_cols)
        self.grid = grid = [[invalid_char for c_idx in xrange(max_cols)] for r_idx in xrange(len(row_widths))]

        for r_idx in xrange(len(row_widths)):
            if shape == "cross":
                s_range = (max_cols/2-((row_widths[r_idx]/2)), max_cols/2+(row_widths[r_idx]/2)+1)
            elif shape == "square":
                s_range = (0, max_cols)
            for s_idx in xrange(s_range[0], s_range[1]):
                self.grid[r_idx][s_idx] = valid_char
    def is_valid_location(self, col, row):
        if len(self.grid) == 0:
            return False

        if (not col >= 0) or (not col < len(self.grid[0])):
            return False
        return (row >= 0) and (row < len(self.grid)) and (self.grid[row][col] != self.invalid_char)
    def process_movement(self, direction):
        if direction == directions.UP:
            self.row = (self.row - 1) if self.is_valid_location(self.col, self.row-1) else self.row
        elif direction == directions.RIGHT:
            self.col = (self.col + 1) if self.is_valid_location(self.col+1, self.row) else self.col
        elif direction == directions.DOWN:
            self.row = (self.row + 1) if self.is_valid_location(self.col, self.row+1) else self.row
        elif direction == directions.LEFT:
            self.col = (self.col - 1) if self.is_valid_location(self.col-1, self.row) else self.col
    def calculate_digit(self):
        sum = 0
        for r_idx in xrange(self.row):
            sum += self.row_widths[r_idx]
        for c_idx in xrange(self.col+1):
            sum = sum + 1 if self.is_valid_location(c_idx, self.row) else sum
        return sum

if __name__=="__main__":
    grid_a = grid([1,3,5,3,1], "cross", "*", "%", 0, 2)
    #grid_a = grid([3,3,3], "square", "*", "%", 1, 1)
    with open("directions.txt") as actions:
        key_str = ""
        for line in actions:
            line = line.replace(' ', '')
            for action in line:
                grid_a.process_movement(action)
            digit = grid_a.calculate_digit()
            digit = chr(digit-10+ord('A')) if digit > 9 else digit
            key_str += str(digit)
        print key_str
