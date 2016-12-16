import md5

def find_n_digits(key, n, num_leading_zeroes=5, uses_position=False):
	idx = 0
	output = ['*' for i in xrange(n)]
	chars_found = 0
	while chars_found < n:
		(next_dig, m_idx, pos) = find_next_digit(key, idx, num_leading_zeroes, uses_position, n)
		if pos == -1:
			output[output.index('*')] = next_dig
			chars_found += 1
		else:
			if output[pos] == '*':
				output[pos] = next_dig
				chars_found += 1
		idx = m_idx+1
	return ''.join(output)

def find_next_digit(key, current_idx, num_leading_zeroes, uses_position, key_size=8):
	def is_valid_digit(dig):
		return dig[0:num_leading_zeroes] == ("0"*num_leading_zeroes)

	idx = current_idx
	md = md5.new()
	md.update(key)
	while True:
		tmp_md = md.copy()
		tmp_md.update(str(idx))
		dig = tmp_md.hexdigest()
		if is_valid_digit(dig):
			if not uses_position:
				#print dig[num_leading_zeroes], idx
				return (dig[num_leading_zeroes], idx, -1)
			else:
				#print dig[num_leading_zeroes], dig[num_leading_zeroes+1], idx
				if int(dig[num_leading_zeroes], 16) >= 0 and int(dig[num_leading_zeroes], 16) < key_size:
					return (dig[num_leading_zeroes+1], idx, int(dig[num_leading_zeroes]))
		idx += 1

# Part 1
#print find_n_digits("reyedfim", 8)

# Part 2
print find_n_digits("reyedfim", 8, uses_position=True)