import collections
for _ in range(int(input())):
    N = int(input())
    l1 = list(map(int,input().split()))
    height_list = collections.Counter(l1)
    height_list = list(height_list.values())
    height_list.sort()
    if(height_list[-1]-height_list[0] > 0):
        print(height_list[-1]-height_list[0])
    else:
        print(-1)
