def calculate_and_print_vi(n):
    if n == 1:
        print(0)
        return 0
    elif n == 2:
        print(0)
        return 0
    elif n == 3:
        print(1.5)
        return 1.5
    else:
        vi = (n+1)/((n*n)+1) * calculate_and_print_vi(n-1) - calculate_and_print_vi(n-2) * calculate_and_print_vi(n-3)
        print(vi)
        return vi