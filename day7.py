import re

pattern = re.compile("(\[[^\[\]]*\])|([^\[\]]*)")

def split_into_ns(inp, n):
    pots = []
    for idx in xrange(len(inp)-(n-1)):
        pots.append(inp[idx:idx+n])
    return pots

# Part 1
def is_abba(inp):
    if len(inp) != 4:
        return False
    return (inp[0] != inp[1]) and (inp[0:2] == inp[2:4][::-1])

# Check if any substring contains abba
def contains_abba(inp):
    pots = split_into_ns(inp, 4)
    for pot in pots:
        if is_abba(pot):
            return True
    return False

# Check if this supports TLS
def is_valid_abba(inp):
    validate = lambda x: 1 if contains_abba(x) else 0
    sections = re.findall(pattern, inp)
    sections = map(''.join, sections)
    sections = [sec for sec in sections if sec != '']

    ret = False
    print sections
    for section in sections:
        evaluate = lambda x: validate(x[1:-1]) * -1 if '[' in section else validate(x)
        result = evaluate(section)

        if result < 0:
            return False
        elif result > 0:
            ret = True
    return ret

# Part 2
def is_aba(inp):
    if len(inp) != 3:
        return False
    return (inp[0] != inp[1]) and (inp[0] == inp[2])

def is_aba_bab_pair(inp1, inp2):
    return is_aba(inp1) and is_aba(inp2) and (inp1[0] == inp2[1]) and (inp1[1] == inp2[0])

def find_aba(inp):
    pots = split_into_ns(inp, 3)
    return [pot for pot in pots if is_aba(pot)]

def is_valid_aba_bab(inp):
    sections = re.findall(pattern, inp)
    sections = map(''.join, sections)
    sections = [sec for sec in sections if sec != '']

    candidates_valid = []
    candidates_invalid = []
    print sections
    for section in sections:
        candidates_valid = candidates_valid + find_aba(section) if not '[' in section else candidates_valid
        candidates_invalid = candidates_invalid + find_aba(section) if '[' in section else candidates_invalid
    results_valid = map(lambda x: map(lambda y: is_aba_bab_pair(y, x), candidates_valid), candidates_valid)
    results_valid = [True in v for v in results_valid]
    results_invalid = map(lambda x: map(lambda y: is_aba_bab_pair(y, x), candidates_invalid), candidates_invalid)
    results_invalid = [True in v for v in results_invalid]
    return (True in results_valid) and (not True in results_invalid)

if __name__ == "__main__":
    with open("directions.txt") as actions:
        count = 0
        for line in actions:
            # Part 1
            #count = count+1 if is_valid_abba(line) else count

            # Part 2
            count = count+1 if is_valid_aba_bab(line) else count
    print count
