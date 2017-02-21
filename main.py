import sys

M = 'M'
T = 'T'
row = 0
col = 0
min = 0
max = 0
pizza = None
nbM = 0
nbT = 0

def algo():
    nbM = 0
    nbT = 0

    print(pizza)

    for line in pizza:
        nbM += line.count(M)
        nbT += line.count(T)

    search = M if nbT > nbM else T
    for i in range (len(pizza)):
        if (search in pizza[i]):
            print ("Index cc= ", list[i].index(search))


if __name__ == '__main__':
    file = open("example.in")
    content = file.read()
    content = content.split('\n')
    row = int(content[0].split(' ')[0])
    col = int(content[0].split(' ')[1])
    min = int(content[0].split(' ')[2])
    max = int(content[0].split(' ')[3])
    pizza = content[1:]
    pizza = pizza[:-1]
    algo()
