budget = int(input())
A = [26,20,34,10.5,18]
lst= ['TOI','Hindu','ET','BM','HT']
for i in range(len(A)):
    for j in range(i,len(A)):
        if (A[i]+A[j] < budget):
            if list[i] == lst[j]:
                continue
            else:
                result = {lst[i],lst[j]}
            if len(result) == 1 :
                continue
            else:
                print(result)

