import csv
import os
import random

def makeGenerator(file):
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        l = []
        for row in reader:
            l.append(row[0])
        #for i in range(len(l)):
        #    print(l[i])

    csvfile.close()

    return l

def initializeLists():
    allLists = {}
    for filename in os.listdir('Resources'):
        #print(str(filename))
        name = str(filename).split('.', 1)[0]
        #print(name)
        allLists[name] = makeGenerator('Resources/' + str(filename))
        #for i in range(len(allLists[name])):
        #    print(allLists[name][i])
    return allLists

def generateRandom(list):
    top = len(list)
    #print(top)
    num = random.randint(0, top - 1)
    return list[num]

def interface():
    lists = initializeLists()
    numToList = []
    for key in lists.keys():
        numToList.append(key)
    print("Select the number of the list you would like to generate!")
    print("Enter 0 to exit")
    for n in range(len(numToList)):
        print(str(n + 1) + ': ' + numToList[n])

    passed = False
    while not passed:
        selection = int(input("Enter a number: "))
        if selection > 0 and selection <= len(numToList):
            passed = True
        elif selection == 0:
            return
        else:
            print("Invalid number, try again")

    passed = False
    name = numToList[selection - 1]
    while not passed:
        print("")
        print("Here is a random selection from: " + name)
        item = generateRandom(lists[name])
        print(item)
        print("")
        again = input("Generate again? y/n ")
        print(again)
        if again == 'y' or again == 'Y' or again == '':
            passed = False
        else:
            passed = True
    interface()
    return

interface()
#lists = initializeLists()
#print(len(lists))
#print(generateRandom(lists['MaleNames']))
#makeGenerator('Resources/Male Names.csv')