def toString(puzzle):
    return ','.join(str(item) for innerlist in puzzle for item in innerlist)
