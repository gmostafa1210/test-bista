d={}
n = int(input("Enter number of elements : "))
d = [ map(str,input().split()) for x in range(n)]

for key, val in d:
    if len(key) > 8:
        if key[0:8] == 'default_':
            key = key[8::]
    print(key,val)