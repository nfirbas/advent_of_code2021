def solve(lanternfishes, days):
    fishes = [0] * 9
    for x in lanternfishes:
        fishes[x] += 1

    for x in range(days):
        fishes = fishes[1:] + fishes[:1]
        fishes[6] += fishes[8]
    print(sum(fishes))

if __name__ == "__main__":
    f = open("./input.txt", "r")
    lanternfishes = [int(x) for x in f.readline().split(',')]
    f.close()

    solve(lanternfishes,256)