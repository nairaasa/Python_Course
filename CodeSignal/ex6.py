def solution(statues):
    statues.sort()
    prev = statues[0]
    addStatue = 0
    for x in statues:
        if x == prev + 1:
            prev = x
        else:
            addStatue += x - prev - 1
            prev = x
    return addStatue

statues = [6, 2, 3, 8]
print(solution(statues))