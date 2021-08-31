pos = -1

def search(list,n):    
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2
        if list[mid]==n:
            globals()['pos']=mid
            return 1
        else:
            if list[mid]>n:
                u=mid-1
            else:
                l=mid+1
    return 0
        


list = [1,3,4,6,7,9,2]
list.sort()
print(list)
n=9

if search(list,n):
    print("FOUND at:",pos+1)
else:
    print('NOT FOUND..')
