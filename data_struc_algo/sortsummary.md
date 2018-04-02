---
title: 各种排序方法的简单总结
categories: 数据结构与算法
tags: [数据结构与算法, 排序]
---
# 各种排序方法的简单总结
排序算法算是计算机的经典算法，解决很多问题的时候排序算法的思想都值得参考。
<!-- TOC -->

- [1. 快速排序的思想](#1-快速排序的思想)
- [2. 归并排序的思想](#2-归并排序的思想)
- [3. 堆排序的思路](#3-堆排序的思路)

<!-- /TOC -->
## 1. 快速排序的思想
学习容易记住的快排算法过程（Partition函数式最重要的，有两种写法，一种高效，另一种普通，参考[这里](http://selfboot.cn/2016/09/01/lost_partition/)）
```c
// main sort function
void qsort(int* arr, int len, int start, int end){
	if(start == end)
		return;
	int index = partition(arr, len, start, end);
	print_arr(arr, len);
	if(index > start)
		qsort(arr, len, start, index - 1);
	if(index < end)
		qsort(arr, len, index + 1, end);
}
// partition function 1
int partition(int* arr, int len, int start, int end){
	if(arr == NULL || start < 0 || end < 0 || end >= len || end < start){
		printf("partition input invalid\n");
		exit(1);
	}
	int pivot = arr[end];

	int small = start - 1;
	int i;
	for(i = start; i < end; i++){
		if(arr[i] < pivot){
			small++;
			if(i != small)
				swap(&arr[small], &arr[i]);
		}
	}

	small++;
	swap(&arr[small], &arr[end]);
	
	return small;
}
// partition function which is more efficient
int partition(int* arr, int len, int start, int end){
	if(arr == NULL || start < 0 || end < 0 || end >= len || end < start){
		printf("partition input invalid\n");
		exit(1);
	}
	int pivot = arr[end];
	start--;
	while(start < end){
		while(start < end && arr[++start] <= pivot);
		arr[end] = arr[start];
		while(start < end && arr[--end] >= pivot);
		arr[start] = arr[end];
	}
	arr[start] = pivot;
	return start;
}
```
## 2. 归并排序的思想
归并排序就是将数组分成两个部分，然后分别对两个部分进行排序，然后再融合起来。可以递归实现，算法时间复杂度时O(nlogn)，空间复杂度O(n)，也就是需要辅助空间。


## 3. 堆排序的思路
参考：[常见排序算法 - 堆排序 (Heap Sort)](http://bubkoo.com/2014/01/14/sort-algorithm/heap-sort/)

堆排序就是把最大堆堆顶的最大数取出，将剩余的堆继续调整为最大堆，再次将堆顶的最大数取出，这个过程持续到剩余数只有一个时结束。在堆中定义以下几种操作：

- 最大堆调整（Max-Heapify）：将堆的末端子节点作调整，使得子节点永远小于父节点
- 创建最大堆（Build-Max-Heap）：将堆所有数据重新排序，使其成为最大堆
- 堆排序（Heap-Sort）：移除位在第一个数据的根节点，并做最大堆调整的递归运算

最大堆调整（MAX‐HEAPIFY）的作用是保持最大堆的性质，是创建最大堆的核心子程序。下面是Java版本的代码：

```java
import java.util.Arrays;
/* 堆排序的思路：
 * 1. 首先明确堆是一种数据结构，利用堆这种数据结构的特性可以很高效地做排序算法。
 * 2. 第一步：堆化。将原本不是堆结构的数组转换成堆，方法时从第一个不是叶节点的节点开始，到根节点，进行堆化操作。堆化操作就是数字的上浮和下沉，要注意的是下沉要彻底，也就是需要递归或者迭代处理下沉的点。
 * 3. 第二步：排序。以最大堆为例，堆顶（也就是树结构的根节点，也就是数组第一个元素）存的是最大值，堆顶元素与最末尾叶节点交换，交换后堆就不是最大堆了，需要重新调整，但是调整的时候就不管最后一个元素了，所以堆的长度减少1。循环此过程直到堆内只剩下一个元素。排序完成。
 * 
 */
public class HeapSortWiki {

	private int[] arr;

	public HeapSortWiki(int[] arr) {
		this.arr = arr;
	}

	/**
	 * 堆排序的主要入口方法，共两步。
	 */
	public void sort() {
		/*
		 * 第一步：将数组堆化 beginIndex = 第一个非叶子节点。 从第一个非叶子节点开始即可。无需从最后一个叶子节点开始。
		 * 叶子节点可以看作已符合堆要求的节点，根节点就是它自己且自己以下值为最大。
		 */
		int len = arr.length - 1;
		int beginIndex = (len - 1) >> 1;
		for (int i = beginIndex; i >= 0; i--) {
			maxHeapify(i, len);
		}

		/*
		 * 第二步：对堆化数据排序 每次都是移出最顶层的根节点A[0]，与最尾部节点位置调换，同时遍历长度 - 1。
		 * 然后从新整理被换到根节点的末尾元素，使其符合堆的特性。 直至未排序的堆长度为 0。
		 */
		for (int i = len; i > 0; i--) {
			swap(0, i);
			maxHeapify(0, i - 1);
		}
	}

	private void swap(int i, int j) {
		int temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}

	/**
	 * 调整索引为 index 处的数据，使其符合堆的特性。
	 * 
	 * @param index
	 *            需要堆化处理的数据的索引
	 * @param len
	 *            未排序的堆（数组）的长度
	 */
	private void maxHeapify(int index, int len) {
		int li = (index << 1) + 1; // 左子节点索引
		int ri = li + 1; // 右子节点索引
		int cMax = li; // 子节点值最大索引，默认左子节点。

		if (li > len)
			return; // 左子节点索引超出计算范围，直接返回。
		if (ri <= len && arr[ri] > arr[li]) // 先判断左右子节点，哪个较大。
			cMax = ri;
		if (arr[cMax] > arr[index]) {
			swap(cMax, index); // 如果父节点被子节点调换，
			maxHeapify(cMax, len); // 则需要继续判断换下后的父节点是否符合堆的特性。
		}
	}

	/**
	 * 测试用例
	 * 
	 * 输出： [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7,
	 * 7, 8, 8, 8, 9, 9, 9]
	 */
	public static void main(String[] args) {
		int[] arr = new int[] { 3, 5, 3, 0, 8, 6, 1, 5, 8, 6, 2, 4, 9, 4, 7, 0, 1, 8, 9, 7, 3, 1, 2, 5, 9, 7, 4, 0, 2,
				6 };
		new HeapSortWiki(arr).sort();
		System.out.println(Arrays.toString(arr));
	}
}
```