def print_num():
    i = 0
    while(i < 9):
        i += 1
        j = 1
        while (j <= i):
            print('%d * %d = %d' %(j, i, j*i), end = '\t')
            j += 1
        print()

print_num()
