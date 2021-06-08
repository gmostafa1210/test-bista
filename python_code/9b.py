lst = []

n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input())
    lst.append(ele)

set_l = set(lst)
my_list = list(set_l)

print(my_list)

