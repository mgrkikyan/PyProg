def vi (i): 
    if i == 1:
        print(0)
        return 0
    elif i == 2:
        print(0)
        return 0
    elif i == 3:
        print(1.5)
        return 1.5
    else:
        A = (i+1)/((i*i)+1) * vi(i-1) - vi(i-2) * vi(i-3)
        print(A)
        return A
    
vi()
