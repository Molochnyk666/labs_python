

def flatten_tuple(T):
    if type(T) is set:
        T = list(T)
    if type(T) != list  and  type(T) != tuple : 
        return (T,)
    elif len(T) == 0: 
        return ()
    else: 
        return flatten_tuple(T[0]) + flatten_tuple(T[1:])



def flatten_list(T):
    if type(T) is set:
        T = tuple(T)
    if type(T) != list  and  type(T) != tuple : 
        return [T]
    elif len(T) == 0: 
        return []
    else: 
        return flatten_list(T[0]) + flatten_list(T[1:])
    


def flatten_it_final1(T):
    test(T)
    if type(T) is list:
        return flatten_list(T)
    elif type(T) is tuple:
        return flatten_tuple(T)
    elif type(T) is set:
        return set(flatten_tuple(T))
    
    
def test(L, ghp = []):
    if type(L) == set:
        L = list(L)
    if (type(L) == list or type(L)== tuple  )and len(L) > 1 :
        if ghp.count(id(L)) == 0:
            ghp.append(id(L))
            test(L[0])
            for x in L[1:]:
                test(x)
        else:
            raise ValueError 
    elif type(L) == list or type(L)== tuple :
        if ghp.count(id(L)) == 0:
            ghp.append(id(L))
            test(L[0])
        else:
            raise ValueError 
    else return
        
if __name__ == "__main__":
    if  len(sys.argv) == 2:
        flatten_it_final1(sys.argv[1])
    else: 
        print('Не верное количество вргументов')



    



        
  
    

