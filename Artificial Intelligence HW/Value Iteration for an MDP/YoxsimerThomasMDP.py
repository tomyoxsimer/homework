import numpy as np
from vi_util import getIndexOfState, getPolicyForGrid, printPolicyForGrid, P


#### Initialization ####


class State:
    def __init__(self, x, y):
        self.x = x
        self.y = y


### value iteration inputs ###
S = [State(1, 1), State(1, 2), State(1, 3), State(1, 4),
     State(2, 1), State(2, 3), State(2, 4),
     State(3, 1), State(3, 2), State(3, 3), State(3, 4)]

A = ['u', 'r', 'd', 'l']

P = P

# make a version of R_states with changeable rewards
R_states = np.array([-.04, -.04, -.04, 1,
                     -.04, -.04, -1,
                     -.04, -.04, -.04, -.04])

# make a version of discount with changeable discount
discount = 1

# values not reward
tr = [3, 6]

U = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0, 1.0])

U_prime = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0, 1.0])

U.astype(float)
U_prime.astype(float)


def getExpectedUtility(S, s, discount):
    """

    :param S:
    :param s:
    :param discount:
    :return:
    """
    index_of_state = getIndexOfState(S, s.x, s.y)

    if index_of_state == 0:
        uP = R_states[index_of_state] + (discount * max(.8 * U[1] + .1 * U[4] + .1 * U[0],  # up
                                                        .9 * U[0] + .1 * U[1],  # left
                                                        .9 * U[0] + .1 * U[4],  # down
                                                        .8 * U[4] + .1 * U[1] + .1 * U[0]))  # right
    if index_of_state == 1:
        uP = R_states[index_of_state] + (discount * max(.8 * U[1] + .1 * U[2] + .1 * U[0],  # up
                                                        .9 * U[0] + .1 * U[2],  # left
                                                        .8 * U[1] + .1 * U[0] + .1 * U[2],  # down
                                                        .9 * U[2] + .1 * U[0]))  # right
    if index_of_state == 2:
        uP = R_states[index_of_state] + (discount * max(.8 * U[5] + .1 * U[1] + .1 * U[3],  # up
                                                        .9 * U[1] + .1 * U[5],  # left
                                                        .8 * U[2] + .1 * U[1] + .1 * U[3],  # down
                                                        .9 * U[3] + .1 * U[5]))  # right
    if index_of_state == 3:
        uP = R_states[index_of_state] + (discount * max(.8 * U[6] + .1 * U[2] + .1 * U[3],  # up
                                                        .9 * U[2] + .1 * U[6],  # left
                                                        .9 * U[3] + .1 * U[6],  # down
                                                        .9 * U[3] + .1 * U[2], ))  # right
    if index_of_state == 4:
        uP = R_states[index_of_state] + (discount * max(.8 * U[7] + .1 * U[4] + .1 * U[0],  # up
                                                        .8 * U[4] + .1 * U[7] + .1 * U[0],  # left
                                                        .8 * U[4] + .1 * U[7] + .1 * U[0],  # right
                                                        .8 * U[0] + .1 * U[4] + .1 * U[7]))  # down
    if index_of_state == 5:
        uP = R_states[index_of_state] + (discount * max(.8 * U[9] + .1 * U[6] + .1 * U[5],  # up
                                                        .8 * U[5] + .1 * U[9] + .1 * U[2],  # left
                                                        .8 * U[6] + .1 * U[9] + .1 * U[2],  # right
                                                        .8 * U[2] + .1 * U[5] + .1 * U[5]))  # down
    if index_of_state == 6:  # terminate ?
        uP = R_states[index_of_state] + (discount * max(.8 * U[10] + .1 * U[4] + .1 * U[0],  # up
                                                        .9 * U[5] + .1 * U[1],  # left
                                                        .9 * U[0] + .1 * U[4],  # down
                                                        .8 * U[4] + .1 * U[1] + .1 * U[0]))  # right
    if index_of_state == 7:
        uP = R_states[index_of_state] + (discount * max(.8 * U[7] + .1 * U[8] + .1 * U[4],  # up
                                                        .9 * U[7] + .1 * U[4],  # left
                                                        .8 * U[4] + .1 * U[8] + .1 * U[7],  # down
                                                        .8 * U[8] + .1 * U[7] + .1 * U[4]))  # right
    if index_of_state == 8:
        uP = R_states[index_of_state] + (discount * max(.8 * U[7] + .1 * U[8] + .1 * U[9],  # left
                                                        .8 * U[8] + .1 * U[7] + .1 * U[9],  # up
                                                        .8 * U[9] + .1 * U[8] + .1 * U[7],  # right
                                                        .8 * U[8] + .1 * U[7] + .1 * U[9]))  # down
    if index_of_state == 9:
        uP = R_states[index_of_state] + (discount * max(.8 * U[9] + .1 * U[8] + .1 * U[10],  # up
                                                        .9 * U[8] + .1 * U[9],  # left
                                                        .9 * U[5] + .1 * U[9],  # down
                                                        .8 * U[10] + .1 * U[5] + .1 * U[9]))  # right
    if index_of_state == 10:  # terminate
        uP = R_states[index_of_state] + (discount * max(.8 * U[10] + .1 * U[9] + .1 * U[6],  # up
                                                        .9 * U[9] + .1 * U[10],  # left
                                                        .9 * U[6] + .1 * U[10],  # down
                                                        .9 * U[10] + .1 * U[6]))  # right
    return uP


def valueIterations(S, A, P, R_states, discount, tr, error):
    """
    :param S:
    :param A:
    :param P:
    :param R_states:
    :param discount:
    :param tr:
    :return:
    """
    U = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0, 1.0])
    U_prime = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0, 1.0])

    U.astype(float)
    U_prime.astype(float)

    convergence = False
    i = 0
    oldV = []
    count = 0
    while not convergence:
        delta = -100  # arbitrary number
        count += 1
        U = U_prime  # change old U to new U
        for s in S:  # for state in state list
            i += 1  # iterate the counter
            oldV.append(s)  # add old state to old states list
            uP = getExpectedUtility(S, s, discount)  # get utility of state
            U_prime[getIndexOfState(S, s.x, s.y)] = uP

            #print((U_prime[getIndexOfState(S, s.x, s.y)]))  # test
            #print(U[getIndexOfState(S, s.x, s.y)])  # test

            if (U_prime[getIndexOfState(S, s.x, s.y)] - U[getIndexOfState(S, s.x, s.y)]) > delta: # calculate the difference
                delta = U_prime[getIndexOfState(S, s.x, s.y)] - U[getIndexOfState(S, s.x, s.y)] # if the difference is greater replace delta

        if delta < .000001:  # .000001 is placeholder value
            convergence = True

    return U


#### Below is provided by class ####

def main():
    # Call value iteration function
    U = valueIterations(S, A, P, R_states, discount, tr, 2)
    print('\n\n\n')
    print('Utilities: \n%s' % U)

    # List of terminal state indices
    i_terminal_states = [6, 10]

    policy = getPolicyForGrid(S, U, A, P, i_terminal_states)
    print('Policy: %s' % policy)

    # Print the policy
    # Last parameter is list of obstacle indices
    # printPolicyForGrid(policy, w, h, [5])


main()
