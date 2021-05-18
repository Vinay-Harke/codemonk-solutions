for _ in range(int(input())):
    N = int(input())
    A = list(map(int,input().split()))
    min_val=float('inf')
    A.sort()
    for i in range(N-1):
                val = A[i] ^ A[i+1]
                min_val = min(val,min_val)
    print(min_val)
