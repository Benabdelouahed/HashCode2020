import Parser


def solve(dataset):
    solution = {}
    for i in range(dataset['nbrelibraries']):
        days = getScanDays(dataset)
        nbrebook = dataset['libraries'][i][2] * days[i]
        if nbrebook > 0:
            solution[i] = dataset['booklist'][i][0:nbrebook]
    print(solution)
    return solution


def getScanDays(dataset):
    days = dataset['scandays']
    librariesDays = []
    for i in range(dataset['nbrelibraries']):
        days -= dataset['libraries'][0][1]
        librariesDays.append(days)
    return librariesDays


solve(Parser.parser("a_example.txt"))
