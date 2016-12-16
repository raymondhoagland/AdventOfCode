def sanitize_input(str_inp):
	(name_and_sector, checksum) = str_inp.strip().split("[")
	checksum = checksum.replace(']', '')
	name_and_sector = name_and_sector.split('-')
	sector = name_and_sector[-1]
	name = ''.join(name_and_sector[0:-1])
	return (name, sector, checksum)

def count_letter_freq(str_inp):
	letter_freq = [0 for i in xrange(ord('z')-ord('a')+1)]
	for idx in xrange(len(str_inp)):
		letter_freq[ord(str_inp[idx])-ord('a')] += 1
	return letter_freq

def retrieve_top_n(letter_freq, n):
	letter_ladder = [None for i in xrange(n)]
	for idx in xrange(len(letter_freq)):
		if letter_ladder[0] is None:
			letter_ladder[0] = idx
			continue
		elif letter_freq[idx] > letter_freq[letter_ladder[0]]:
			letter_ladder = [idx]+letter_ladder[0:-1]
			continue
		ladder_idx = 0
		while True:
			if ladder_idx >= (n-1):
				break
			elif letter_ladder[ladder_idx+1] is None:
				letter_ladder[ladder_idx+1] = idx
				break
			elif letter_freq[idx] > letter_freq[letter_ladder[ladder_idx+1]]:
				letter_ladder = letter_ladder[0:ladder_idx+1] + [idx] + letter_ladder[ladder_idx+1:n-1]
				break
			ladder_idx +=1 
	return ''.join(map(lambda x: chr(int(str(x))+ord('a')), letter_ladder))

if __name__ == "__main__":
	# Part 1
	with open("directions.txt") as actions:
		valid_checksums_sum = 0
		for line in actions:
			(name, sector, checksum) = sanitize_input(line)
			valid_checksums_sum = valid_checksums_sum+int(sector) if retrieve_top_n(count_letter_freq(name), 5) == checksum else valid_checksums_sum
		print valid_checksums_sum