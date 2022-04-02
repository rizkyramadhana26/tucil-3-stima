def toString(puzzle):
    return ','.join(str(item) for innerlist in puzzle for item in innerlist)

def readFile(filename):
    with open(filename) as f:
        lines = f.readlines()
    lines = [line.strip().split() for line in lines]
    for i in range(4):
        for j in range(4):
            lines[i][j] = int(lines[i][j])
    return lines