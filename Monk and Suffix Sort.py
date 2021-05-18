# Write your code here
s1,pos=input().split()
pos = int(pos)
all_suffix = []
for i in range(len(s1)-1,-1,-1):
    all_suffix.append(s1[i:])
all_suffix.sort()
print(all_suffix[pos-1])
