import math as mth
import sys

        
                        
                        

def sqrt_decomp_list(T):
    M = [0]
    for i, x in enumerate(T,0):
        numb = i/mth.ceil(mth.sqrt(len(T)))
        if numb == mth.ceil(numb) and numb != 0:
            M.append(0)
        M[mth.floor(i/mth.ceil(mth.sqrt(len(T))))]+= x
    return M



def sqrt_decomp(T,M,f,L):
    final_sum = 0
    len_cell = mth.ceil(mth.sqrt(len(T)))
    first = mth.ceil(f / mth.ceil(mth.sqrt(len(T))))
    last = mth.floor(L / mth.ceil(mth.sqrt(len(T))))
    print(last)
    if L - f <= mth.ceil(mth.sqrt(len(T))) :
        for x in range(f,L + 1 ,1):
            final_sum += T[x]
    else:
        for x in range(first, last):
            final_sum += M[x]
        for x in range(f, (first)*len_cell, 1):
            final_sum += T[x]
        for x in range(last*len_cell, L + 1, 1):
            print(last)
            print(x)
            final_sum += T[x]
    return final_sum

def main():
    while True:
        a =input('Как хотите ввести массив?: \n 1.) Вручную \n 2.) Через файл \n Для того,чтобы выйти введите exit \n')
        
        if a == '1':
            massive = input('Вводите числа через пробел ').split(" ")
            massive1 = []
            for x in massive:
                if x.isalpha() :
                    print('Массив содержит не число, попробуйте еще раз \n')
                    continue
                else:
                    massive1.append(float(x)) 
            break
        elif a=='2' :
            file = input('Файл :')
            f1 = open(file, 'r')
            for x in f1.read().split(" "):
                if x.isalpha() :
                    print('Массив содержит не число, попробуйте еще раз \n')
                    continue
                else:
                    massive1.append(float(x))
        elif a=='exit':
            sys.exit()
        else:
            print('Попробуйте еще раз \n')
            continue
    massive2 = sqrt_decomp_list( massive1 )
    while True:
        segment = input('Введите начало и конец отрезка, на котором хотите найти сумму или exit, если хотите выйти: ')
        if segment == 'exit':
            sys.exit()
        segment = segment.split(" ")
        if len(segment) > 2:
            print('Вы ввели неправильно, попробуйте еще раз \n')
            continue
        segment_true = []
        for x in segment:
            if x.isdigit():
                if int(x)> len(massive1):
                    ('Вы ввели неправильно, попробуйте еще раз \n')
                    continue
                else: 
                    segment_true.append(int(x))
            else: 
                ('Вы ввели неправильно, попробуйте еще раз \n')
                continue
        print(sqrt_decomp(massive1,massive2,segment_true[0], segment_true[1]))
        
        


if __name__ == "__main__":
    main()
    
   
     
     





    
