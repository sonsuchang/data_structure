def recursive_func(n):
    if n == 1:
        return 0    
    else:
        return 5 * recursive_func(n-1) + 3
print(recursive_func(3))