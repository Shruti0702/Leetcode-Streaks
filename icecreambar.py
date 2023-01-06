costs=[int(x) for x in input().split(',')]
coins=int(input())
sum=maximum=flag=0
costs.sort()
lr=[]
for i in range(len(costs)):
    if costs[i]<=coins:
        sum+=costs[i]
        flag=1
    if sum<=coins and flag==1:
        maximum+=1
    else:
        sum=sum-costs[i]
        break;
print(maximum)
