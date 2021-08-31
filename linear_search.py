pos = -1

def search(list,n):    
    for i in range(len(list)):   
        if list[i]==n:
            globals() ['pos']=i
            return True
    return False


list = [1,3,4,6,7,9,2]
n=2

if search(list,n):
    print("FOUND at:",pos)
else:
    print('NOT FOUND..')
