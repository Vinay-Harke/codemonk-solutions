testCase  = int(input())
for _ in range(testCase):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    index = k % n
    print(*(l[n-index:]+l[:n-index]))
