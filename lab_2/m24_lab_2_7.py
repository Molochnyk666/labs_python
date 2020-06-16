import sys



def leonardo_num(n):
    if type(n) != int:
        raise TypeError
    if n < 2:
        return 1
    lnum1 = 1
    lnum2 = 1 
    for x in range(n-2):
        lnum = lnum1+ lnum2 +1
        lnum2 = lnum1
        lnum1 = lnum
    return lnum


def main():
    a = input('Введите число или exit, если хотите выйти: ' )
    if a == 'exit':
        return
    elif a.isdigit():
        a = int(a) 
    while a != 'exit':
        print(leonardo_num(a))
        a = input('Выполнить еще раз? Если желаете продолжить введите число иначе exit ')
    sys.exit()
    

if __name__ == "__main__":
    if  len(sys.argv) > 1:
        for x in sys.argv[:1]:
            leonardo_num(x)
    else: main()