x1 = 0
y1 = 1
x2 = 2
y2 = 3

def solve(data, horizontal):
    terrain = [[0 for i in range(1000)] for j in range(1000)]
    for c in data:
        if c[x1] == c[x2] or c[y1] == c[y2] or horizontal: 
            x = c[x1]
            y = c[y1]
            while True:
                terrain[y][x] +=  1
                if x == c[x2] and y == c[y2]:
                    break

                if x > c[x2]:
                    x -= 1
                elif x < c[x2]:
                    x+=1

                if y > c[y2]:
                    y-= 1
                elif y < c[y2]:
                    y+=1


    overlap = 0
    for x in range(1000):
        for y in range(1000):
            if terrain[x][y] >= 2:
                overlap += 1
    print(overlap)



if __name__ == "__main__":
    f = open("./input.txt", "r")
    buffer = [i for i in f.readlines()]
    data = [
        [int(i) for i in line.replace(' -> ', ',').strip().split(',')]
        for line in buffer
    ]

    f.close()
    solve(data, False)
    solve(data, True)