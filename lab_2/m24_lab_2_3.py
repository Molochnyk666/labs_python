import linecache

def merge_help_str(T):
    if len(T) <= 1:
        return T
    mid = int(len(T)/2)
    left = merge_help_str(T[:mid])
    right = merge_help_str(T[mid:])
    return merge_hs(left, right)

def merge_hs(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if len(left[0]) <= len(right[0]):
            result.append(left[ 0 ])
            left = left[ 1: ]
        else:
            result.append(right[0])
            right = right[1:]
    if len(left) > 0:
            result += left
    if len(right) > 0:
            result += right
    return result
    

def merge_help(T):
    if len(T) <= 1:
        return T
    mid = int(len(T)/2)
    left = merge_help(T[:mid])
    right = merge_help(T[mid:])
    return merge_h(left, right)

def merge_h(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0][0] <= right[0][0]:
            result.append(left[ 0 ])
            left = left[ 1: ]
        else:
            result.append(right[0])
            right = right[1:]
    if len(left) > 0:
            result += left
    if len(right) > 0:
            result += right
    return result


def merge_it(filename):
    data = tuple()
    with open(filename, 'r') as file:
        for i,line in enumerate(file,0):
            data += ((len(line),i),)
    data = merge_help(data)
    with open ('merge_file.txt', "a") as file_write:
    for x in data:
        line = merge_help_str(linecache.getline('merge_file.txt',x[1]).split(" "))
        del line[0]
        line.append('\n')
        file_write.write(" ".join(line))


f __name__ == "__main__":
    if  len(sys.argv) == 2:
        flatten_it_final1(sys.argv[1])
    else: 
        print('Не верное количество вргументов')



