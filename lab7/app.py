 
list = [1,2,3,4,5]
n = 2

def split(list, n):
    list1 = [] 
    list2 = []
    for i in list:
        if (i % 2 != 0):
            list1.append(i)
        else:
            list2.append(i)
    print(list1) 
    print(list2)

split(list, n)
