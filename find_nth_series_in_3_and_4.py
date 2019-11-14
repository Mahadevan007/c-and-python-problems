def find_nth_series(n):
    arr = [""]*(n+1)
    size = 1
    m = 1
    
    while(size<=n):
        i = 0
        while(i<m and (size+i)<=n):
            arr[size+i] = "3"+arr[size-m+i]
            i = i + 1
        i = 0
        while(i<m and (size+m+i)<=n):
            arr[size+m+i] = "4"+arr[size-m+i]
            i = i + 1
        m = m * 2
        size = size + m
    print(arr[n])
    
n = int(input("Enter a number"))
find_nth_series(n)