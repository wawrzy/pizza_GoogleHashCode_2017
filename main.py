import sys

row = 0
col = 0
min = 0
max = 0
pizza = None

def algo():
    print(row)
    print(col)
    print(min)
    print(max)
    print(pizza)


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
