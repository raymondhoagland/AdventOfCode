def count_safe(line):
    count_safe = 0
    for idx in xrange(len(line)):
        count_safe = count_safe+1 if line[idx] == "." else count_safe
    return count_safe

def generate_next_row(line):
    def is_safe(line, idx):
            return (line[idx] == "^")

    new_row = [None for i in xrange(len(line))]
    safe_count = 0
    for idx in xrange(len(line)):
        if idx == 0:
            l_marker = False
        else:
            l_marker = is_safe(line, idx-1)
        if idx == len(line)-1:
            r_marker = False
        else:
            r_marker = is_safe(line, idx+1)
        m_marker = is_safe(line, idx)
        new_row[idx] = "^" if ((l_marker & ~r_marker) | (~l_marker & r_marker)) else "."
    safe_count = count_safe(new_row)
    return (''.join(new_row), safe_count)

with open("directions.txt") as actions:
    for line in actions:
        line = line.strip()
        num_rows = 400000
        row_idx = 1
        rows = [line]
        safe_count = count_safe(line)
        while row_idx < num_rows:
            (n_line, n_safe_count) = generate_next_row(rows[-1])
            rows.append(n_line)
            rows = [rows[-1]]
            safe_count += n_safe_count
            row_idx += 1
        #for row in rows:
        #    print row
        print safe_count
