def mod_dragon_curve(a):
    b = a[::-1].replace('0', '2').replace('1', '0').replace('2', '1')
    return a + '0' + b

def calc_dragon_curve(a, max_length):
    while len(a) < max_length:
        a = mod_dragon_curve(a)
    return a[:max_length]

def calc_checksum(a):
    checksum = a
    while True:
        n_checksum = ''
        for i in xrange(0, len(checksum), 2):
            n_checksum += '1' if checksum[i]==checksum[i+1] else '0'
        checksum = n_checksum
        if len(checksum) % 2 != 0:
            return checksum

if __name__=="__main__":
    max_len = 35651584
    with open("directions.txt") as actions:
        for line in actions:
            line = line.strip()
            drag = calc_dragon_curve(line, max_len)
            #print "Drag: ", drag
            print "Checksum: ", calc_checksum(drag)
