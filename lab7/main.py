<<<<<<< Updated upstream
def vi (i): 
=======
def func(i):
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
        A = (i+1)/((i*i)+1) * vi(i-1) - vi(i-2) * vi(i-3)
        print(A)
        return A
    
vi()
=======
        A = (i+1)/((i*i)+1) * func(i-1) - func(i-2) * func(i-3)
        print(A)
        return A

func(4)
>>>>>>> Stashed changes
