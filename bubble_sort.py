def sort(n):
    for i in range(len(n)-1,0,-1):
        for j in range(i):
            if n[j]>n[j+1]:
                temp = n[j]
                n[j] = n[j+1]
                n[j+1] = temp
    


n = [2,5,6,3,1,7]
sort(n)
print(n)