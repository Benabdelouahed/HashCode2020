def parser(filename):
    dataset = {}
    f = open(filename, "r")
    firstline = f.readline().split(" ")
    dataset['nbrebooks'] = int(firstline[0])
    dataset['nbrelibraries'] = int(firstline[1])
    dataset['scandays'] = int(firstline[2].split("\n")[0])
    secondline = f.readline().split(" ")
    dataset['books'] = []
    for i in range(len(secondline) - 1):
        dataset['books'].append(int(secondline[i]))
    dataset['books'].append(int(secondline[-1].split("\n")[0]))
    dataset['libraries'] = []
    dataset['booklist'] = []
    alt = 0
    for line in f.readlines():
        if (line == "\n"):
            continue
        if (alt % 2 == 0):

            first = line.split(" ")
            intfirst = []
            for i in range(len(first) - 1):
                intfirst.append(int(first[i]))

            intfirst.append(int(first[-1].split("\n")[0]))
            dataset['libraries'].append(intfirst)
        else:
            second = line.split(" ")
            intsecond = []
            for i in range(len(second) - 1):
                intsecond.append(int(second[i]))
            intsecond.append(int(second[-1].split("\n")[0]))
            dataset['booklist'].append((intsecond))
        alt += 1
    return dataset
