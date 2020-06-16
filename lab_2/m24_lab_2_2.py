from random import randint, choice 
import sys


    
def string_generation( K = (10,100), L=(3,10 )):
    list_chr = []
    for x in range(65,91):
        list_chr.append(x)
    for x in range(97,123):
        list_chr.append(x)
    string = ''
    for x in range(randint(K[0],K[1])):
        word = ''
        for x in range(randint(L[0],L[1])):
            word = word + chr(choice(list_chr))
        string += word + ' ' 
    string += '\n'
    return string
    
def text_generation( namefile, Mb, K = (10,100), L=(3,10 )):
    if type(K) != type(L) != tuple or len(K) != len(L) != 2  :
        return
    if type(namefile) != str:
        return
    if type(Mb) != int or type(Mb) != float:
        return
    file = open(namefile, "a")
    lenstr = 0
    while Mb*1024**2 > (lenstr):
        string = string_generation(K,L )
        lenstr += len(string)
        file.write(string)
        progress = lenstr*100/(Mb*1024**2)
        print('\r Запись файла завершена на %3d%%' % progress, end = '', flush = True)
    print(' \n Запись файла окончена')
    file.close()
        
if __name__ == "__main__":
    if len(sys.argv) > 1:
        if len(sys.argv) == 2:
            text_generation(sys.argv[1])
        elif len(sys.argv) == 3:
            text_generation(sys.argv[1],sys.argv[2])
        elif len(sys.argv) == 4:
            text_generation(sys.argv[1],sys.argv[2],sys.argv[3])
        elif len(sys.argv) == 5:
            text_generation(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])  
        elif len(sys.argv) > 5:
            print('Слишком много аргументов')
            
    else: print('Недостаточно аргументов')
    
        
    







        
        