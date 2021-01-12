from nqueens import Board, numAttackingQueens, getSuccessorStates


def localSearch(boardSize, decay_rate, terminateT):
    board1 = Board(boardSize)  # set up first board state
    board1.rand()
    currH = numAttackingQueens(board1)
    curr = board1

    print('Initial Board')
    board1.printBoard()  # output initial state
    print('h-value:', currH)  # output h value
    h = currH
    T = 100

    while T >= terminateT:
        if currH == 0:
            break
        succ = getSuccessorStates(curr)
        for x in succ:
            currH = numAttackingQueens(x)
            #print('In for loop', currH, 'seeking below', h) #  test
            if currH == 0:
                curr = x
                break
            if currH < h:
                # print('Im here', currH, h) # test
                h = currH
                curr = x
        T = T * decay_rate

    print('Final board h value:', currH)  # output final board
    curr.printBoard()
    return currH

def main():
    size = 4
    decay = .9
    tKill = .000001
    runCount = 0
    hTotal = 0
    print('Board Size:', size, '\nDecay Rate:', decay, '\nT Threshold', tKill)
    while runCount < 10:
        print('Run', runCount)
        h = localSearch(size, decay, tKill)
        hTotal += h
        runCount += 1
    print('Average h-cost of final solutions:', hTotal/10)

    size = 4
    decay = .75
    tKill = .0000001
    runCount = 0
    hTotal = 0
    print('Board Size:', size, '\nDecay Rate:', decay, '\nT Threshold', tKill)
    while runCount < 10:
        print('Run', runCount)
        h = localSearch(size, decay, tKill)
        hTotal += h
        runCount += 1
    print('Average h-cost of final solutions:', hTotal / 10)

    size = 4
    decay = .5
    tKill = .00000001
    runCount = 0
    hTotal = 0
    print('Board Size:', size, '\nDecay Rate:', decay, '\nT Threshold', tKill)
    while runCount < 10:
        print('Run', runCount)
        h = localSearch(size, decay, tKill)
        hTotal += h
        runCount += 1
    print('Average h-cost of final solutions:', hTotal / 10)

    size = 8
    decay = .9
    tKill = .000001
    runCount = 0
    hTotal = 0
    print('Board Size:', size, '\nDecay Rate:', decay, '\nT Threshold', tKill)
    while runCount < 10:
        print('Run', runCount)
        h = localSearch(size, decay, tKill)
        hTotal += h
        runCount += 1
    print('Average h-cost of final solutions:', hTotal / 10)

    size = 8
    decay = .75
    tKill = .0000001
    runCount = 0
    hTotal = 0
    print('Board Size:', size, '\nDecay Rate:', decay, '\nT Threshold', tKill)
    while runCount < 10:
        print('Run', runCount)
        h = localSearch(size, decay, tKill)
        hTotal += h
        runCount += 1
    print('Average h-cost of final solutions:', hTotal / 10)

    size = 8
    decay = .5
    tKill = .00000001
    runCount = 0
    hTotal = 0
    print('Board Size:', size, '\nDecay Rate:', decay, '\nT Threshold', tKill)
    while runCount < 10:
        print('Run', runCount)
        h = localSearch(size, decay, tKill)
        hTotal += h
        runCount += 1
    print('Average h-cost of final solutions:', hTotal / 10)

    size = 16
    decay = .9
    tKill = .000001
    runCount = 0
    hTotal = 0
    print('Board Size:', size, '\nDecay Rate:', decay, '\nT Threshold', tKill)
    while runCount < 10:
        print('Run', runCount)
        h = localSearch(size, decay, tKill)
        hTotal += h
        runCount += 1
    print('Average h-cost of final solutions:', hTotal / 10)

    size = 16
    decay = .75
    tKill = .0000001
    runCount = 0
    hTotal = 0
    print('Board Size:', size, '\nDecay Rate:', decay, '\nT Threshold', tKill)
    while runCount < 10:
        print('Run', runCount)
        h = localSearch(size, decay, tKill)
        hTotal += h
        runCount += 1
    print('Average h-cost of final solutions:', hTotal / 10)

    size = 16
    decay = .5
    tKill = .00000001
    runCount = 0
    hTotal = 0
    print('Board Size:', size, '\nDecay Rate:', decay, '\nT Threshold', tKill)
    while runCount < 10:
        print('Run', runCount)
        h = localSearch(size, decay, tKill)
        hTotal += h
        runCount += 1
    print('Average h-cost of final solutions:', hTotal / 10)


main()
