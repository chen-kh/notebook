# 两个整型数组之间的数据互相调整，使得和之差的绝对值最小
问题描述：整形数组A和B，长度分别为n和m，设计一个算法：两个数组之间可以交换数值，最终使得 | sum(A) - sum(B) | 最小

输入：数组A，B

输出：无

## 分析

问题的终极版：[有一个数字集合，将集合分成多个（固定数量）子集合，使得子集的和的最大值最小]，已经被证明是NP问题了。当然还有集合和的方差最小等等更难的变形。近似算法一般都是基于贪心的。问题太难了，简化一下。数字集合分成两组，数量不必相等，和的差最小，就是与本题类似的一个题目。可以转换为背包问题，背包重量为sum/2。其实再之后的一些问题，就是加一些限制了，比如本题，限制了两个子集的大小。

下面分别给出没有限制和有限制的解题思路。

### 整型数组A，分解为两个数组，使得两个数组的和之差最小。
- 解题思路：动态规划中的0-1背包问题，背包重量bagweight=sum/2。  
- 算法证明：使用动态规划求解的结果只有两种情况： 1. 背包被装满（物品重量正好等于背包重量） 2. 背包没有被装满。第一种情况当然就是最优解。至于第二种情况，假设存在另外一个解使得原解的物品总重量与背包重量之差abs(w1-bagweight)小于最优解的物品总重量与背包重量之差abs(wi-bagweight)。由于w1 < bagweight，则wi > bagweight，则sum-wi < bagweight。sum-wi，wi与sum/2的距离相等。因此w1 < sum-wi < bagweight，因此sum-wi是0-1背包的最优解，而w1也是，所以矛盾。问题得证！
- 解题代码
```python
'''使用背包问题求解，设原数组S的长度为n, 和为sum。
选择背包重量为sum/2，S中每个数值表示一件物品的重量和价值（相等）。
'''
def min_sumdiff_subsets(intset):    
    bagweight = sum(intset)/2
    indexarray = get_01knapsack_solution(bagweight, intset)
    A = [intset[i] for i in indexarray]
    B = [intset[i] for i not in indexarray]
    return (A, B)
```

### 在上面的基础上，限定一个集合的大小为 m，其中 m<n 
- 解题思路：仍然认为是0-1背包问题，与上面一种情况不同的是，这里限定了选择东西的数量。只需要在计算动态规划问题的时候考虑选择东西数量的问题就好了。其实这里思考起来并不难，但是很多边界条件需要考虑进去，也就说如何保证选择确定的m个数值，既不多也不少。
- 状态方程：
![状态方程](dp_sum_diff_min.png)  
其中w[i]和p[i]分别表示重量数组和价值数组，本题中相等。f(i,j,k)表示从第1到第i个元素中取k个，放在重量为j的包里的最大价值（重量）问题。边界条件主要有3点需要注意：1.当i <= k时，需要将前i-i个元素都取出来；2.当j <= 0而k != 0时，直接舍弃这种情况; 3. 如果重量不得已必须超过j时，开始选小的那一个。一个简单版的递归代码如下，仅仅表示思想，代码很乱，很没有技术含量。。。
```python
def knapsack(wlist, i, j, k):
    if i<0 or j<0 or k<=0:
        return 0
    if i+1 == k:
        return sum(wlist[:i+1]) # the sum maybe larger than j
    if j<=0 and k != 0: # it tells us that there is no solution
        return None 
    if wlist[i] > j:
        return knapsack(wlist, i-1, j, k)
    else:
        a = knapsack(wlist, i-1, j, k)
        bt = knapsack(wlist, i-1, j-wlist[i], k-1)
        if bt is None: # 
            b = 0
        else:
            b = bt + wlist[i]
        if a is None:
            a = 0
        if a >= b and a <= j: 
            return a
        if a < b and b <= j:
            return b
        if a > j or b > j: # in case of one of sum larger than j, the best result smaller than j does not exist, then we trying to find the result which is closest to j (althought it's larger than j)
            return min(a,b)

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
```

### 回到最初的问题，交换两个数组的元素，使得数组和的差值最小
从最初的角度思考问题，交换两个数组的元素。这种方法也达到目标。
- 算法过程：从数组A的第一个元素开始，在数组B中寻找最优的下标i，即`argmin(sum(A) - A[1] + B[i] - sum(B) + B[i] - A[1]) = argmin(sum(A) - sum(B) - 2 * (A[1] - B[i]))`。然后交换A[1]与B[i]。之后对A[2]进行同样的操作。知道将数组A遍历完毕，会得到一个比原来和的差值小很多新的A和B。以上过程为一次迭代，直到和的差值为0或者上一次迭代与本次迭代没有变化，循环完毕。
- 算法证明：明显可以看出，只要数组A和B中存在调优的空间（交换数值可以使和的差值更小），每次迭代总会有数值交换，因此总能到达最优的情况。
- 问题思考：值得考虑的是，这种算法的时间复杂度有多少，因为迭代多少次似乎是未知的，最坏的情况时每次迭代优化一个单位，这样至少需要迭代abs(sum(A) - sum(B))次，时间复杂度最坏的情况是abs(sum(A) - sum(B)) * m * n
- 算法代码示例
```python
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


if __name__ == '__main__':
    A = [1,2,3,4,5]
    B = [5,6,7,8,9]
    exchange2min_sumdiff(A,B)
    print(A)
    print(B)
    print(abs(sum(A) - sum(B)))
```
