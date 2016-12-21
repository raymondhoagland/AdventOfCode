def is_valid_time(disc_info, time):
    for idx in xrange(len(disc_info)):
        if disc_info[idx][0] is None:
            continue
        #print disc_info[idx][0], disc_info[idx][1], disc_info[idx][0]+time+idx, time, idx
        if (disc_info[idx][0]+time+idx) % disc_info[idx][1] != 0:
            return False
    return True

def fill_disc_info(disc_info, num):
    n_disc_info = disc_info[:]
    while len(n_disc_info) <= num:
        n_disc_info.append([None, None])
    return n_disc_info

if __name__=="__main__":
    with open("directions.txt") as actions:
        disc_info = []
        for line in actions:
            action_info = line.split(" ")
            disc_num = int(action_info[1][1:])
            slots = int(action_info[3])
            position = int(action_info[-1][:-2])
            disc_info = fill_disc_info(disc_info, disc_num)
            disc_info[disc_num] = [position, slots]
        disc_info.append([0, 11])
        time = 0
        while (not is_valid_time(disc_info, time)):
            time += 1
        print time
