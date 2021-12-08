def flatten(input):
    new_list = []
    for i in input:
        for j in i:
            new_list.append(j)
    return new_list

if __name__ == "__main__":
    f = open("./input.txt", "r")
    data = flatten([i.replace(' \n ', ' ').strip().split(' ') for i in f.readlines()])
    
    f.close()
