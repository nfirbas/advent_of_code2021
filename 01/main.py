def solve(data, x):
    increased = 0
    for i in range(x, len(data)):
        increased += value(data, i-1, x) <  value(data, i, x)
    print(increased)

def value(data, i, x):
    value = 0
    for j in range(x):
        value += data[i-j]
    return valuecd

if __name__ == "__main__":
    f = open("./input.txt", "r")
    data = [int(x) for x in f.readlines()]
    f.close()
    solve(data, 1)
    solve(data, 3)