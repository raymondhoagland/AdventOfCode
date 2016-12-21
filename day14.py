import md5
import pprint

def find_first_n_in_row(num, n):
    if len(num) == 0:
        return (n == 0)

    n_in_row = 0
    num_str = str(num)
    last_seen_char = num[0]

    for idx in xrange(1, len(num_str)):
        if last_seen_char == num_str[idx]:
            n_in_row += 1
        else:
            last_seen_char = num_str[idx]
            n_in_row = 0
        if n_in_row == (n-1):
            return last_seen_char
    return None

def calc_next_hash(salted_hash, idx, runs=0):
    t_hash = salted_hash.copy()
    t_hash.update(str(idx))
    result = t_hash.hexdigest()
    for i in xrange(runs):
        result = md5.new(result).hexdigest()
    return result

def add_potential(potential, potential_keys, n):
    idx = 0

    while idx < len(potential_keys):
        if potential == potential_keys[idx][0]:
            potential_keys[idx][1].append(n)
            return potential_keys
        elif potential < potential_keys[idx][0]:
            potential_keys.insert(idx, (potential, [n]))
            return potential_keys
        idx += 1
    potential_keys.append((potential, [n]))
    return potential_keys

# def prune_keys(potential_keys, idx):
#     n_idx =0
#
#     while n_idx < len(potential_keys):
#         for pot_idx in xrange(len(potential_keys[n_idx][1])):
#             if (idx - potential_keys[n_idx][1][0] > 1000):

def update_keys(potential, potential_keys, keys_identified, idx):
    n_idx = 0

    while n_idx < len(potential_keys):
        if potential == potential_keys[n_idx][0]:
            savers = []
            for pot_idx in xrange(len(potential_keys[n_idx][1])):
                if ((idx - potential_keys[n_idx][1][0]) <= 1000):
                    if idx - potential_keys[n_idx][1][0] == 0:
                        savers.append(potential_keys[n_idx][1][0])
                    else:
                        print "taking out", potential_keys[n_idx][1][0], idx, potential_keys[n_idx][0]
                        keys_identified.append(potential_keys[n_idx][1][0])
                potential_keys[n_idx][1].pop(0)
            for x in savers:
                potential_keys[n_idx][1].append(x)
        elif potential < potential_keys[n_idx][0]:
            break
        n_idx += 1
    return potential_keys, keys_identified

def calc_min_check(potential_keys):
    max_check = 0
    for i in xrange(len(potential_keys)):
        for k in xrange(len(potential_keys[i][1])):
            if potential_keys[i][1][k] > max_check:
                max_check = potential_keys[i][1][k]
    return max_check+1000

if __name__ == "__main__":
    with open("directions.txt") as actions:
        for line in actions:
            keys_identified = []
            potential_keys = []
            idx = 0
            min_check = 0
            salted_hash = md5.new(line.strip())
            while (len(keys_identified) < 64) or (idx < min_check):
                hash_res = calc_next_hash(salted_hash, idx, 2016)
                potential = find_first_n_in_row(hash_res, 3)
                if not potential is None:
                    potential_keys = add_potential(potential, potential_keys, idx)
                    confirms_keys = find_first_n_in_row(hash_res, 5)
                    if not confirms_keys is None:
                        potential_keys, keys_identified = update_keys(potential, potential_keys, keys_identified, idx)
                if len(keys_identified) >= 64 and min_check == 0:
                    min_check = calc_min_check(potential_keys)
                    print min_check
                idx += 1
            results = sorted(keys_identified)[:64]
            print results, len(results)
            # pp = pprint.PrettyPrinter(indent=4)
            # pp.pprint(potential_keys)
