
def knapsack(wlist, i, j, k):
    if i<0 or j<0 or k<=0:
        return 0
    if i+1 == k:
        return sum(wlist[:i+1])
    if j<=0 and k != 0:
        return None 
    if wlist[i] > j:
        return knapsack(wlist, i-1, j, k)
    else:
        a = knapsack(wlist, i-1, j, k)
        bt = knapsack(wlist, i-1, j-wlist[i], k-1)
        if bt is None:
            b = 0
        else:
            b = bt + wlist[i]
        if a is None:
            a = 0
        if a >= b and a <= j:
            return a
        if a < b and b <= j:
            return b
        if a > j or b > j:
            return min(a,b)
        # return max(knapsack(wlist, i-1, j, k), knapsack(wlist, i-1, j-wlist[i], k) + wlist[i])

def test():
    wlist = [1,3,4,9,6,7,10,2]
    i = len(wlist)-1
    j = sum(wlist)/2
    # k = len(wlist)/2
    for k in range(1,7):
        a = knapsack(wlist,i,j,k)
        print(wlist,i+1,j,k)
        print(a)

if __name__ == '__main__':
    test()