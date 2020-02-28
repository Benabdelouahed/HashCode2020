usedBooks = []


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
    dataset['scoreLib'] = []
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
            score = 0
            intsecond = []
            for i in range(len(second) - 1):
                intsecond.append(int(second[i]))
                score += int(dataset["books"][int(second[i])])

            score += int(dataset["books"][int(second[-1].split("\n")[0])])
            intsecond.append(int(second[-1].split("\n")[0]))
            dataset["scoreLib"].append(score)
            dataset['booklist'].append((intsecond))
        alt += 1
    return dataset


def solve(dataset):
    solution = {}
    # process = getProcessLibrarySorted(dataset)
    process = maxScoreLib(dataset)
    for i in process:
        days = getScanDays(dataset)
        nbrebook = dataset['libraries'][i][2] * days[i]
        if nbrebook > 0:
            solution[i] = maxScoreBooksByLib(dataset, dataset['booklist'][i])
    return solution


def maxScoreBooksByLib(dataset, books):
    scoreBooks = dataset['books']
    dict = {}
    for item in books:
        dict[item] = scoreBooks[item]
    sorted2 = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    sorted3 = [i[0] for i in sorted2]
    return sorted3


def getProcessLibrarySorted(dataset):
    process = dataset['libraries']
    listSorted = {}
    for i in range(len(process)):
        listSorted[i] = process[i][1]
    listSorted = sorted(listSorted, key=listSorted.__getitem__)
    return listSorted


def getScanDays(dataset):
    days = dataset['scandays']
    librariesDays = []
    for i in range(dataset['nbrelibraries']):
        days -= dataset['libraries'][0][1]
        librariesDays.append(days)
    return librariesDays


"""solution={}
solution[1]=[5,2,3]
solution[0]=[0,1,2,3,4]"""


def maxScoreLib(dataset):
    dic = {}
    for i in range(len(dataset["libraries"])):
        dic[i] = dataset["scoreLib"][i]
    sorted2 = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    sorted3 = [i[0] for i in sorted2]
    return sorted3


def resolve(input):
    dataset = parser(input)
    nblib = dataset['nbrelibraries']
    solution = solve(dataset)
    nbLibUsed = len(solution.keys())

    toPrint = str(nbLibUsed)

    for cle, valeur in solution.items():
        toPrint = toPrint + "\n" + str(cle) + " " + str(len(valeur))
        books = ""
        for item in valeur:
            books = books + str(item) + " "
        toPrint = toPrint + "\n" + books
    return toPrint


datasets = ["d_tough_choices.txt"]
# datasets = ["e_so_many_books.txt","f_libraries_of_the_world.txt"]
for item in datasets:
    result = resolve(item)
    fichier = open("data_" + item + ".txt", "w")
    fichier.write(result)
    fichier.close()
