n = int(input("enter a n value:"))
d = {}

for i in range(n):
    keys = input() 
    values = int(input()) 
    d[keys] = values

print(d)

d_n = sorted(d.items(),reverse=True)
d=dict(d_n) 

print(d)
