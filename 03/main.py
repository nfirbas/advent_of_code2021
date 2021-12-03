def solve(data):
    number_of_ones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(12):
        number_of_ones[i] =  get_number_of_ones(data, i)

    gamma = 0
    epsilon = 0
    for i in range(len(number_of_ones)-1, -1, -1):
        gamma = (gamma << 1) + (number_of_ones[i]/len(data) >= 0.5)
        epsilon = (epsilon << 1) + (number_of_ones[i]/len(data) < 0.5)
    print(gamma * epsilon)

    oxygen = data
    co2 = data

    for i in range(11, -1, -1):
        oxygen = [number for number in oxygen if ((number >> i)&1) == resolve_oxygen(oxygen, i)]
        if len(oxygen) == 1:
            break
    for i in range(11, -1, -1):
        co2 = [number for number in co2 if ((number >> i)&1) == resolve_co2(co2, i)]
        if len(co2) == 1:
            break

    print(co2[0]*oxygen[0])

def resolve_co2(data, i ):
    number_of_ones = get_number_of_ones(data, i)
    
    zeros = len(data)-number_of_ones
    if zeros <= number_of_ones:
        return 0
    return 1

def resolve_oxygen(data, i ):
    number_of_ones = get_number_of_ones(data, i)
    
    zeros = len(data)-number_of_ones
    if zeros > number_of_ones:
        return 0
    return 1

def get_number_of_ones(data, i):
    number_of_ones = 0
    for number in data:
        number_of_ones += int((number >> i) & 1)
    return number_of_ones

if __name__ == "__main__":
    f = open("./input.txt", "r")
    data = [int(x, 2) for x in f.readlines()]
    f.close()
    solve(data)


