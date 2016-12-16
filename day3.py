def is_valid_triangle(a, b, c):
	return ((a+b) > c) and ((a+c) > b) and ((b+c) > a)

def sanitize_input(inp, max_size=3):
	def parse_ints(str_inp):
		(n_ret, remaining) = select_next_int(str_inp, max_size)
		ret = [n_ret]
		while remaining != '':
			(n_ret, remaining) = select_next_int(remaining, max_size)
			if n_ret != '':
				ret.append(n_ret)
		return tuple(ret)
		
	def select_next_int(str_inp, max_size):
		remaining_str_inp = str_inp[2:]
		return (remaining_str_inp[0:max_size], remaining_str_inp[max_size:])
	return map(int, parse_ints(inp))


def process_horizontal(fp):
	valid_triangles = 0
	for line in fp:
		sides = sanitize_input(line)
		valid_triangles = valid_triangles+1 if is_valid_triangle(*sides) else valid_triangles
	return valid_triangles

def process_vertical(fp):
	a_sides = None
	b_sides = None
	valid_triangles = 0
	for line in fp:
		sides = sanitize_input(line)
		if a_sides is None:
			a_sides = sides
		elif b_sides is None:
			b_sides = sides
		else:
			for idx in xrange(len(sides)):
				valid_triangles = valid_triangles+1 if is_valid_triangle(a_sides[idx], b_sides[idx], sides[idx]) else valid_triangles
			a_sides = b_sides = None
	return valid_triangles


with open("directions.txt") as actions:
	print process_horizontal(actions)
with open("directions.txt") as actions:
	print process_vertical(actions)