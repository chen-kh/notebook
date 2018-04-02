---
title: 经典动态规划的题目
categories: 数据结构与算法
tags: [数据结构与算法, 动态规划]
---
# 经典动态规划的题目
<!-- TOC -->

- [1. 矩阵联乘问题](#1-矩阵联乘问题)
- [2. 最长公共子序列](#2-最长公共子序列)
- [3. 最长不重复子串](#3-最长不重复子串)
- [4. 最大连续子序列之和](#4-最大连续子序列之和)
- [5. 到达终点的路线条数](#5-到达终点的路线条数)
- [6. 数塔问题](#6-数塔问题)
- [7. 背包问题及其延伸](#7-背包问题及其延伸)
- [8. 最长递增子序列(LIS)](#8-最长递增子序列lis)
- [9. 代码及示例](#9-代码及示例)

<!-- /TOC -->
## 1. 矩阵联乘问题

## 2. 最长公共子序列
- 描述  
一个序列 S ，如果分别是两个或多个已知序列的子序列，且是所有符合此条件序列中最长的，则 S 称为已知序列的最长公共子序列。

- 转移方程：  
问题简化为在已知`str1[:i-1]`与`str2[:j-1]`的情况下，个字新添加一个字符之后最长公共子序列的长度的问题。  
`dp[i,j] = 0                                 i=0 || j=0`  
`dp[i,j] = dp[i-1][j-1]+1                    i>0,j>0, a[i] = b[j]`  
`dp[i,j] = max(dp[i-1][j],dp[i][j-1])        i>0,j>0, a[i] != b[j]`

## 3. 最长不重复子串
- 描述  
针对某个字符串，输出最长的不含有重复字符的子串的长度。注意子串（substring）和子序列（subsequence）是有区别的。

- 转移方程：  
使用`HashMap`存储`key-value`对，其中`key=字符`，`value=字符所在index`。问题转换为新填入一个字符之后，最长不重复子串如何变化的问题。  
`dp[i]`表示以第i个字符为结尾的不重复子串的长度。  
`condition = str[i] not in hashmap || str[i] in hashmap but hashmap[str[i]] <= (i - dp[i])`
`dp[i]=dp[i-1]+1  if condition==true`
`dp[i]=1          if condition==false`

## 4. 最大连续子序列之和
- 描述  
给定K个整数的序列{ N1, N2, ..., NK }，其任意连续子序列可表示为{ Ni, Ni+1, ..., Nj }，其中 1 <= i <= j <= K。最大连续子序列是所有连续子序中元素和最大的一个， 例如给定序列{ -2, 11, -4, 13, -5, -2 }，其最大连续子序列为{ 11, -4, 13 }，最大和为20。

- 状态转移方程：  
`sum[i]=max(sum[i-1]+a[i],a[i])`

- 提示：  
可以使用状态矩阵，也可以使用两个变量代替状态矩阵，从而将空间复杂度降低到O(1)
## 5. 到达终点的路线条数
## 6. 数塔问题

## 7. 背包问题及其延伸
- 描述  
有N件物品和一个容量为V的背包。第i件物品的费用是c[i]，价值是w[i]。求解将哪些物品装入背包可使价值总和最大。

- 转移方程：  
将问题转化为放不放进最后一个背包进去。  
`dp[i][j]` 表示前i个物品放到承重为j的背包里的最大价值。  
`dp[i][j] = max(dp[i-1][j],dp[i-1][j-weight[i]] + value[i]`

## 8. 最长递增子序列(LIS)
- 描述  
给定一个序列 `An = a1 ,a2 ,  ... , an` ，找出最长的子序列使得对所有 `i<j, ai < aj`。
- 转移方程：  
`b[k]`表示以第k个元素为结尾的最长递增子序列的长度，问题转化为放不放入最后一个数字的问题。  
`b[k]=max(max(b[j]|a[j]<a[k],j<k)+1,1);`

## 9. 代码及示例
```java
package chenkh.basic.dp;

public class ClassicDP {
	public static void main(String[] args) {
		int max = 0;
		max = MaxSumofContinousSubSequence(new int[] { -2, 11, -4, 13, -5, -2 }, true);
		max = MaxSumofContinousSubSequence(new int[] { -2, 11, -4, 13, -5, -2 }, false);
		max = MaxSumofContinousSubSequence(new int[] { 1, 2, 3, 4, 5 }, true);
		max = MaxSumofContinousSubSequence(new int[] { 1, 2, 3, 4, 5 }, false);
		max = MaxSumofContinousSubSequence(new int[] {}, true);
		max = MaxSumofContinousSubSequence(new int[] {}, false);
		max = MaxSumofContinousSubSequence(new int[] { -1, -2 }, true);
		max = MaxSumofContinousSubSequence(new int[] { -1, -2 }, false);
		System.out.println(max);
	}

	// 最大连续子序列之和
	// 状态转移方程： sum[i]=max(sum[i-1]+a[i],a[i])
	// 可以使用状态矩阵，也可以使用两个变量代替状态矩阵，从而将空间复杂度降低到O(1)
	public static int MaxSumofContinousSubSequence(int[] seq, boolean extraSpaceAllowable) {
		if (seq == null || seq.length <= 0)
			return 0;
		int max = Integer.MIN_VALUE;
		if (extraSpaceAllowable) {
			int[] sum = new int[seq.length];
			sum[0] = seq[0];
			max = sum[0] > max ? sum[0] : max;
			for (int i = 1; i < seq.length; i++) {
				int nextSum = sum[i - 1] + seq[i];
				sum[i] = nextSum > seq[i] ? nextSum : seq[i];
				max = sum[i] > max ? sum[i] : max;
			}
		} else {
			int sum = seq[0];
			max = max > sum ? max : sum;
			for (int i = 1; i < seq.length; i++) {
				int newSum = sum + seq[i];
				sum = newSum > seq[i] ? newSum : seq[i];
				max = sum > max ? sum : max;
			}
		}
		System.out.println(max);
		return max;
	}
}

```