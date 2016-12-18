freq_counters = None

def process_row(row):
    global freq_counters

    row = row.strip('\n')
    if freq_counters is None:
        freq_counters = [[0 for i in xrange(26)] for k in xrange(len(row))]
    for char_idx in xrange(len(row)):
        freq_counters[char_idx][ord(row[char_idx])-ord('a')] += 1

def evaluate_cols():
    global freq_counters

    # Part 1
    def find_max_in_col(freq_counter):
        fmic = lambda x: x.index(max(x))
        return fmic(freq_counter)

    # Part 2
    def find_min_in_col(freq_counter):
        fmic = lambda x: x.index(min([v for v in x if v != 0]))
        return fmic(freq_counter)

    ret = ''
    for counter in freq_counters:
        ret += chr(find_min_in_col(counter)+ord('a'))
    return ret

if __name__ == "__main__":
    with open("directions.txt") as actions:
        for line in actions:
            process_row(line)
    print evaluate_cols()
