def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))


def towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        towers(n - 1, fr, spare, to)
        towers(1, fr, to, spare)
        towers(n - 1, spare, to, fr)


print(towers(4, 'P1', 'P2', 'P3'))