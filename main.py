budget = int(input())  
A = [26,20,34,10.5,18]  #list of weekly prices of newspapers
lst= ['TOI','Hindu','ET','BM','HT']  #list of newspapers
for i in range(len(A)):
    for j in range(i,len(A)):
        if (A[i]+A[j] < budget):
            if lst[i] == lst[j]:
                continue
            else:
                result = {lst[i],lst[j]}
            if len(result) == 1 :
                continue
            else:
                print(result)

