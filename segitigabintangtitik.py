def print_star_pattern(n):
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        print(spaces, end='')  
        for j in range(1, i + 1):
            if j == 1:
                print('*', end='') 
            else:
                print('.*', end='')  
        print()  
n = 5
print_star_pattern(n)
