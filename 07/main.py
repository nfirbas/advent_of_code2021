def solve(positions, function):
    i = 0
    last = function(positions, i)
    while True:
        new = function(positions, i+1)
        if last < new:
            print(int(last))
            break
        i+=1
        last = new


def calculate_cost_1(positions, position):
    cost= 0
    for x in positions:
        cost += abs(x-position)
    return cost 

def calculate_cost_2(positions, position):
    cost= 0
    for x in positions:
        price = abs(x-position)
        cost += (price + 1) * (price/2)
    return cost 

if __name__ == "__main__":
    f = open("./input.txt", "r")
    positions = [int(x) for x in f.readline().split(',')]
    f.close()

    solve(positions, calculate_cost_1)
    solve(positions, calculate_cost_2)