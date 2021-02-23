
def checkStates(state1, state2):
    if len(state1) != len(state2):
        return False
    s1 = set(state1)
    s2 = set(state2)
    if s1 == s2:
        return True
    else:
        return False


def gps(initial, final, ops):
    curState = initial.copy()
    while not checkStates(curState, final):
        op = {}
        for i in ops:
            f = True
            for j in i["preconds"]:
                if j not in curState:
                    f = False
                    break
            if f:
                op = i
                break
        if op == {}:
            print("Failed")
            return
        print(op["action"])
        curState.extend(op["add"])
        for i in op["delete"]:
            if i in curState:
                curState.remove(i)
