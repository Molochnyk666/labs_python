import sys




def power_of_two(num):
    if not num.isdigit():
        return print(num, 'не является целым положительным числом /n')
    num = int(num)
    if num==1 or num==0 :
        return print(num, 'не является точной степенью двойки /n')
    if (num-1)&num ==0:
        print(num, 'является точной степенью двойки /n')
    else: print(num, 'не является точной степенью двойки /n')

def main():
    a  = input('Введите число: ' )
    while a != 'exit':
        power_of_two(a)
        a = input('Выполнить еще раз? Если желаете продолжить введите число иначе exit')
    sys.exit()
            
    



if __name__ == "__main__":
    if  len(sys.argv) > 1:
        for x in sys.argv[:1]:
            power_of_two(x)
    else: main()
        