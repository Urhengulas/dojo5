def initDep():
    dependencies = {
        "A": ["B", "C"],
        "B": ["C", "E"],
        "C": ["G"],
        "D": ["A", "F"],
        "E": ["F"],
        "F": ["H"],
        "G": [],
        "H": []
    }
    return dependencies


def fullDeps(deps):
    ret = {}
    for key in deps.keys():
        ret[key] = sorted(singleDeps(deps, key))
    return ret


def singleDeps(deps, key):
    retDeps = set(deps[key]).copy()
    while True:
        newDeps = retDeps.copy()
        for key in retDeps.copy():
            for newKey in deps[key]:
                retDeps.add(newKey)
        if newDeps == retDeps:
            break
    return retDeps


def testUnit(testDeps):
    rightDeps = {
        "A": ["B", "C", "E", "F", "G", "H"],
        "B": ["C", "E", "F", "G", "H"],
        "C": ["G"],
        "D": ["A", "B", "C", "E", "F", "G", "H"],
        "E": ["F", "H"],
        "F": ["H"],
        "G": [],
        "H": []
    }

    for key in testDeps.keys():
        if testDeps[key] == rightDeps[key]:
            pass
        else:
            return False
    return True



def main():
    deps = initDep()

    deps = fullDeps(deps.copy())

    if testUnit(deps):
        print("Right")
    else:
        print("Wrong")


if __name__ == "__main__":
    main()
