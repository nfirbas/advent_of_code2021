def solve(f):
    forward = 0
    depth = 0
    aim = 0
    for x in f:
        change = int(x.split(" ")[1])
        match x.split(" ")[0]:
            case "forward":
                forward += change
                depth += change*aim
            case "down":
                aim += change
            case "up":
                aim -= change
    print(aim * forward)
    print(depth * forward)


if __name__ == "__main__":
    f = open("./input.txt", "r")
    solve(f)
    f.close()
