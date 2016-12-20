def get_val_or_reg(inp, registers):
    try:
        val = int(inp)
    except ValueError as e:
        val = registers[ord(inp)-ord('a')]
    return val

def process_line(line, registers):
    action_info = line.split(" ")

    # print line
    ret = 0
    if action_info[0] == "cpy":
        val = get_val_or_reg(action_info[1], registers)
        reg = action_info[2]
        registers[ord(reg)-ord('a')] = val
    elif action_info[0] == "inc":
        reg = action_info[1]
        registers[ord(reg)-ord('a')] += 1
    elif action_info[0] == "dec":
        reg = action_info[1]
        registers[ord(reg)-ord('a')] -= 1
    elif action_info[0] == "jnz":
        reg = get_val_or_reg(action_info[1], registers)
        skip_lines = int(action_info[2])
        if reg != 0:
            ret = skip_lines
    # print registers, ret
    return registers, ret

if __name__ == "__main__":
    with open("directions.txt") as actions:
        num_skip = 0
        registers = [0 for x in xrange(4)]
        # Part 2
        registers[2] = 1
        buffer = []
        for line in actions:
            buffer.append(line)
        idx = 0
        while idx < len(buffer):
            line = buffer[idx]
            registers, num_skip = process_line(line.strip(), registers)
            idx = idx + num_skip if num_skip != 0 else idx + 1
        print registers
