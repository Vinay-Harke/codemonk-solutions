in_list= []
for _ in range(int(input())):
    s1 = input()
    in_list.append(s1)
    in_list.sort()
    print(in_list.index(s1))
