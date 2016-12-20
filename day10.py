class Out:
    def __init__(self):
        self.chips = []

    def add_chip(self, val):
        self.chips.append(val)

    def disp(self):
        print self.chips

class Bot:
    def __init__(self):
        # [0/1, -1->infinity]
        # first index is robot/output
        # second index is number
        self.high = None
        self.low = None
        self.chips = []
        self.bot_idx = -1

    def add_chip(self, val):
        self.chips.append(val)
        if len(self.chips) == 2:
            # Part 1 Check
            if (max(self.chips) == 61) and (min(self.chips) == 17):
                print "Magic bot: ", self.bot_idx

            self.high.add_chip(max(self.chips))
            self.low.add_chip(min(self.chips))
            self.chips = []

    def disp(self):
        print 'Bot ', self.bot_idx, ' contents: '
        print self.chips

    def set_high(self, obj):
        self.high = obj

    def set_low(self, obj):
        self.low = obj

    def set_idx(self, idx):
        self.bot_idx = idx

def fill_bots(num_bots, bots):
    n_bots = bots[:]
    while True:
        if len(n_bots) > num_bots:
            break
        n_bots.append(Bot())
        n_bots[-1].set_idx(len(n_bots)-1)
    return n_bots

def fill_outs(num_outs, outs):
    n_outs = outs[:]
    while True:
        if len(n_outs) > num_outs:
            break
        n_outs.append(Out())
    return n_outs

def pre_process_action(bots, outs, line):
    action_info = line.split(' ')
    action_queue = []
    if action_info[0] == "value":
        bot_num = int(action_info[-1])
        bots = fill_bots(bot_num, bots)
        action_queue.append([bot_num, action_info[1]])
    elif action_info[0] == "bot":
        bot_num = int(action_info[1])
        low_type = action_info[5]
        low_dest = int(action_info[6])
        high_type = action_info[10]
        high_dest = int(action_info[11])
        bots = fill_bots(bot_num, bots)

        if low_type == "bot":
            bots = fill_bots(low_dest, bots)
            bots[bot_num].set_low(bots[low_dest])
        elif low_type == "output":
            outs = fill_outs(low_dest, outs)
            bots[bot_num].set_low(outs[low_dest])
        if high_type == "bot":
            bots = fill_bots(high_dest, bots)
            bots[bot_num].set_high(bots[high_dest])
        elif high_type == "output":
            outs = fill_outs(high_dest, outs)
            bots[bot_num].set_high(outs[high_dest])
    return (bots, outs, action_queue)

def process_actions(bots, outs, actions):
    n_bots = bots[:]
    for action in actions:
        bot_num = action[0]
        value = action[1]
        t_bot = n_bots[bot_num]
        t_bot.add_chip(int(value))
        n_bots[bot_num] = t_bot
    return (n_bots, outs)

if __name__ == "__main__":
    with open("directions.txt") as actions:
        bots = []
        outs = []
        action_queue = []
        for line in actions:
            (bots, outs, n_action_queue) = pre_process_action(bots, outs, line)
            action_queue += n_action_queue
        (bots, outs) = process_actions(bots, outs, action_queue)

        # Part 2
        mult = 1
        for i in xrange(0, 3):
            mult *= outs[i].chips[0]
        print mult
