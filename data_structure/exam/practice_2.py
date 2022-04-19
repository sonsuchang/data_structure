def move(n, src, tmp, dest):
    if n > 0:
        move(n-1, src, dest, tmp)
        print("move %d from %c to %c" % (n, src, dest))
        move(n-1, dest, tmp, src)
move(3, 'a', 'b', 'c')