for _ in range(int(input())):
    M = []
    ij = []
    pq = []
    N = int(input())
    for i in range(N):
        M.append(list(map(int,input().split())))
    inversion_count = 0
    for i in range(N):
        for j in range(N):
            ij.append((i,j))
            pq.append((i,j))
    for i,j in ij:
        for p,q in pq:
            if(i<= p and j <= q):
                if(M[i][j] > M[p][q]):
                    inversion_count += 1
    print(inversion_count)
