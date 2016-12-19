def expand_sequence(sequence, times):
    return process_buf(sequence, need_output=True)[1]*times

def expand_sequence_len(sequence, times):
    return process_buf(sequence)[0]*times

def read_into_buf(fp, buf):
    for line in fp:
        line = line.strip()
        buf += line
    return buf

def process_buf(buf, need_output=False):
    def process_expansion_request(request):
        expansion_request = request[1:-1]
        return map(int, expansion_request.split("x"))
    idx = 0
    ret = [0]
    if need_output:
        ret.append("")
    while idx < len(buf):
        if buf[idx] == '(':
            rparens_idx = buf.find(')', idx)
            expansion_request = buf[idx:rparens_idx+1]
            num_chars, times = process_expansion_request(expansion_request)
            ret[0] += expand_sequence_len(buf[rparens_idx+1:rparens_idx+1+num_chars], times)
            if need_output:
                ret[1] += expand_sequence(buf[rparens_idx+1:rparens_idx+1+num_chars], times)
            idx = rparens_idx+num_chars+1
        else:
            ret[0] += 1
            if need_output:
                ret[1] += buf[idx]
            idx += 1
    return ret

if __name__ == "__main__":
    with open("directions.txt") as actions:
        buf = read_into_buf(actions, "")
        print process_buf(buf, need_output=False)
