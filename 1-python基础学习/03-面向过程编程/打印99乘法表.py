# 定义起始行
row = 1

while row <= 9:

    #定义起始列
    col = row

    if row >= 2:
        print("           " * (row-1), end="")

    while col <= 9:

        ret = "%d * %d = %2d" % (row, col, row*col)

        print(ret, end=" ")

        col += 1

    print("")
    
    row += 1