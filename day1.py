class directions:
	num_dirs = 4
	North, East, South, West = xrange(num_dirs)

direction = directions.North
x_dist = 0
y_dist = 0
location_set = set()

# Determine which direction we are now facing
def process_dir_change(dir):
	global direction

	if dir == "L":
		direction = (direction - 1) % directions.num_dirs
	elif dir == "R":
		direction = (direction + 1) % directions.num_dirs

# Move n steps in the current direction
def move_marker(dist):
	global direction, x_dist, y_dist

	if direction >= (directions.num_dirs/2):
		dist *= -1

	result = -1
	if direction % 2 == 0:
		result = update_set(0, dist)
		y_dist += dist
	else:
		result = update_set(dist, 0)
		x_dist += dist
	return result

# Update the set of locations that have been visited ()
def update_set(x_disp=0, y_disp=0):
	global x_dist, y_dist, location_set
	
	def perform_update(x, y, result):
		if (x, y) in location_set:
			res = calc_displacement(location=(x, y))
		else:
			location_set.add((x, y))
			res = -1
		return res

	result = -1
	for disp in xrange(1, abs(x_disp)+1):
		n_disp = disp if x_disp > 0 else disp*-1
		res = perform_update(x_dist+n_disp, y_dist, result)
		result = res if (result == -1) else result
	for disp in xrange(1, abs(y_disp)+1):
		n_disp = disp if y_disp > 0 else disp*-1
		res = perform_update(x_dist, y_dist+n_disp, result)
		result = res if (result == -1) else result

	return result

# Calculate the "distance" from the origin
def calc_displacement(location=None):
	global x_dist, y_dist 

	if location:
		return  abs(location[0])+abs(location[1])
	return abs(x_dist)+abs(y_dist)

if __name__=="__main__":
	location_set.add((0,0))
	first_result_found = False
	with open("directions.txt") as actions:
		for line in actions:
			line = line.replace(' ', '')
			for action in line.split(','):
				process_dir_change(action[0])
				res = move_marker(int(action[1:]))
				if not first_result_found:
					if res != -1:
						print "Distance to first revisited location: "+str(res)
						first_result_found = True
	print "Distance to final location: "+str(calc_displacement())
