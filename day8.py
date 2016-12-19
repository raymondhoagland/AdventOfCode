class Grid:
    def __init__(self, n_cols, n_rows):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.mat = [[0 for k in xrange(n_cols)] for i in xrange(n_rows)]

    def init_grid(self, mat):
        self.mat = mat[:]

    def rect(self, n_cols, n_rows):
        n_rows = min(self.n_rows, n_rows)
        n_cols = min(self.n_cols, n_cols)
        for i in xrange(n_rows):
            for k in xrange(n_cols):
                self.mat[i][k] = 1

    def rotate_row(self, row, offset, grid=None):
        if grid is None:
            offset %= self.n_cols
            offset = self.n_cols - offset
            self.mat[row] = self.mat[row][offset:] + self.mat[row][0:offset]
            return None
        else:
            offset %= len(grid[row])
            offset = len(grid[row]) - offset
            grid[row] = grid[row][offset:] + grid[row][0:offset]
            return grid

    def rotate_col(self, col, offset):
        col_as_arr = [self.mat[i][col] for i in xrange(len(self.mat))]
        col_as_arr = self.rotate_row(0, offset, [col_as_arr])[0]
        for i in xrange(len(self.mat)):
            self.mat[i][col] = col_as_arr[i]

    def disp(self, show_zeroes=True):
        buffer = ""
        buffer += '-'*self.n_cols+'\n'
        for row in self.mat:
            if show_zeroes:
                buffer += str(row) +'\n'
            else:
                buffer += str(map(lambda x: "-" if x == 1 else " ", row))+'\n'
        buffer += '-'*self.n_cols+'\n'
        return buffer

    def count_active(self):
        count = 0
        for i in xrange(self.n_rows):
            for k in xrange(self.n_cols):
                count = count+1 if self.mat[i][k] == 1 else count
        return count

    def split_chars(self, width, height):
        for i in xrange(0, self.n_rows, height):
            for k in xrange(0, self.n_cols, width):
                tmp_grid = Grid(width, height)
                smat = [row[k:k+width] for row in self.mat[i:i+height]]
                #print smat
                tmp_grid.init_grid(smat)
                print tmp_grid.disp(show_zeroes=False)

if __name__ == "__main__":
    grid = Grid(50, 6)
    with open("directions.txt") as actions:
        for line in actions:
            action_info = line.split(" ")
            if action_info[0] == "rect":
                cols, rows = map(int, action_info[1].split('x'))
                grid.rect(cols, rows)
            elif action_info[0] == "rotate":
                if action_info[1] == "row":
                    row = int(action_info[2].split('=')[1])
                    offset = int(action_info[4])
                    grid.rotate_row(row, offset)
                elif action_info[1] == "column":
                    col = int(action_info[2].split('=')[1])
                    offset = int(action_info[4])
                    grid.rotate_col(col, offset)
    print grid.disp()
    print grid.count_active()
    grid.split_chars(5,6)
