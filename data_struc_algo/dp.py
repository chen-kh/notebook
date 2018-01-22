
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


def exchange2min_sumdiff(arr1, arr2):
    n, m = len(arr1), len(arr2)
    last_absdiff = abs(sum(arr2) - sum(arr1))
    if last_absdiff == 0:
        return
    best = 0
    while(not best):
        best_absdiff = last_absdiff
        for i, a in enumerate(arr1):
            best_index = 0
            for j, b in enumerate(arr2):
                newabsdiff = abs(sum(A) - sum(B) - 2 * (a - b))
                if newabsdiff < best_absdiff:
                    best_absdiff = newabsdiff
                    best_index = j
                    if best_absdiff == 0:
                        arr1[i], arr2[best_index] = arr2[best_index], arr1[i]
                        return
            if best_absdiff < last_absdiff:
                print('exchange A[{0}]='.format(i) + str(arr1[i]) + ' and B[{0}]='.format(best_index) + str(arr2[best_index]) + ", " + str(best_absdiff))
                arr1[i], arr2[best_index] = arr2[best_index], arr1[i]

        if best_absdiff == last_absdiff:
            best = 1
            break
        if best_absdiff < last_absdiff:
            last_absdiff = best_absdiff
        

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
    # test()
    A = [1,2,3,4,5]
    B = [5,6,7,8,9]
    exchange2min_sumdiff(A,B)
    print(A)
    print(B)
    print(abs(sum(A) - sum(B)))