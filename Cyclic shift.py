for _ in range(int(input())):
    N,K = map(int,input().split())
    A = input()
    Atemp = A
    max_value = 0
    A = A[1:]+A[0]
    while(A != Atemp):
        value = int(A,2)
        max_value = max(max_value,value)
        A = A[1:]+A[0]
    B = str(bin(max_value))
    B = B[2:]
    A = Atemp
    count =0
    for _ in range (K):
        A = A[1:]+A[0]
        count += 1
        while(int(A,2) != int(B,2)):
            A = A[1:]+A[0]
            count += 1
    print(count)
