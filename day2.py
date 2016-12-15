class directions:
	num_dirs = 4
	UP, RIGHT, DOWN, LEFT  = 'U', 'R', 'D', 'L'

num_cols = 3
num_rows = 3

def process_movement(direction, current_col, current_row):
	global num_cols, num_rows

	n_col, n_row = current_col, current_row
	if direction == directions.UP:
		n_row -=1 if current_row > 0 else current_row
	elif direction == directions.RIGHT:
		n_col = (n_col + 1) if current_col < (num_cols - 1) else current_col
	elif direction == directions.DOWN:
		n_row = (n_row + 1) if current_row < (num_rows - 1) else current_row
	elif direction == directions.LEFT:
		n_col -=1 if current_col > 0 else current_col
	return (n_col, n_row)

def calculate_digit(location):
	return (location[0])+((location[1])*num_cols)+1

if __name__=="__main__":
	with open("directions.txt") as actions:
		key_str = ""
		current_col, current_row = (num_cols/2, num_rows/2)
		for line in actions:
			line = line.replace(' ', '')
			for action in line:
				current_col, current_row = process_movement(action, current_col, current_row)
			key_str += str(calculate_digit((current_col, current_row)))
		print key_str