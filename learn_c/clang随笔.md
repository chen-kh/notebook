---
title: C language 随笔
categories: C语言
tags: [随笔, C语言]
---
# C language 随笔

## 结构体指针需要先初始化（分配内存空间）再进行赋值

关于这个问题网上有很多人问，这里记录一下。我认为网上的一些认识是有误的。先说原理。

- 指针变量其实是一种数据类型，他有自己的地址，也有自己占的内存空间和值。只不过他的值等于另一个（常规）变量的地址。星号`*`其实是取值操作，也就是说`*pointer`就是将`pointer`的值（指针变量存储的值）对应的地址上的值拿到。

- 对于普通整型变量`int a`的指针`int* a`，不能直接通过`*a = 10`进行赋值，因为这时变量 a 还没有地址，需要首先`a = (int*)malloc(sizeof(int))`获取内存空间，再进行`*a = 10`的赋值操作。在`*a = 10`这一过程中并不是`=`这个赋值操作的问题，而是`*a`这个取值操作本身就有问题。显而易见：a变量不在内存中，所以找不到。其实在进行内存分配也就是`malloc`之前，如果你用`&a`查看a的地址，其实看到的是指针变量`int* a`的地址；或者你用`sizeof(a)`去查看a占用内存的大小，其实看到的也是指针变量占用的字节大小（我这里显示8）；当你使用`&(*a)`去查看指针指向的变量的地址时，其实等于查看`a`(也就是指针变量的value)；`malloc`操作之后，再查看`&(*a)`或者`a`，你会发现他跟之前不一样了，也就是说初始化了之后，指针真正指向了内存中的某个地址。也就相当于给指针变量进行了**赋值操作**。指针变量创建（`int* a`）的时候，并没有初始化的值（即便你看到了也是不被承认的）

- 对于结构体指针，同上，其实道理都是一样的。只要是指针，就不会给指针指向的变量进行初始化，而只会进行指针变量的初始化，但是指针变量的初始值是不被承认的，或者理解为在内存中无法按照这个值找到具体变量的。

下面是我的测试代码：

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct St
{
	int i;
	int j;
} S;


int main(){
	printf("%d\n", sizeof(int));// check if size of integer is 4, YES
	/*the following 3 line is the normal code for decloration -> malloc -> set value for pointer type variable
	*/
	int* b;
	b = (int*)malloc(sizeof(int));
	*b = 10;
	printf("%s\n", "============== test for int pointer ==============="); 
	int* a;
	printf("before malloc: ------------\n");
	printf("address of pointer a = %d\n", &a);
	printf("value of pointer a = %d\n", a);
	printf("address of pointer pointed = %d\n", a);
	printf("size of value pointer pointer = %d\n", sizeof(*a));
	// printf("value of pointer pointed = %d\n",*a); // execute this line will cause error cause *a has not value
	a = (int*)malloc(4);
	printf("before set value: ------------\n");
	printf("address of pointer a = %d\n", &a);
	printf("value of pointer a = %d\n", a);
	printf("address of pointer pointed = %d\n", a);
	printf("value of pointer pointed = %d\n",*a); // the result is 0
	printf("size of value pointer pointer = %d\n", sizeof(*a));
	printf("a = %d\n", *a);
	*a = 10;
	printf("after set value: ------------\n");
	printf("address of pointer a = %d\n", &a);
	printf("value of pointer a = %d\n", a);
	printf("address of pointer pointed = %d\n", a);
	printf("value of pointer pointed = %d\n",*a);
	printf("size of value pointer pointer = %d\n", sizeof(*a));
	printf("%s\n", "============= test for struct pointer ===============");
	S* sb;
	sb = (S*)malloc(sizeof(S));
	sb->i = 10;
	// *sb = {1, 2};// cause error cause we can not init sa like this
	S* sa;
	printf("sa = %d\n", *sa);
	printf("before malloc: ------------\n");
	printf("address of pointer a = %d\n", &sa);
	printf("value of pointer a = %d\n", sa);
	printf("address of pointer pointed = %d\n", sa);
	printf("size of value pointer pointer = %d\n", sizeof(*sa));
	sa = (int*)malloc(sizeof(S));
	printf("before set value: ------------\n");
	printf("address of pointer sa = %d\n", &sa);
	printf("value of pointer sa = %d\n", sa);
	printf("address of pointer pointed = %d\n", sa);
	printf("value of pointer pointed = %d\n",*sa); // the result is 0
	printf("size of value pointer pointer = %d\n", sizeof(*sa));
	printf("sa->i = %d\n", sa->i);
	sa->i = 10;
	sa->j = 20;
	printf("after set value: ------------\n");
	printf("address of pointer sa = %d\n", &sa);
	printf("value of pointer sa = %d\n", sa);
	printf("address of pointer pointed = %d\n", sa);
	printf("value of pointer pointed = %d\n",*sa);
	printf("size of value pointer pointer = %d\n", sizeof(*sa));
	printf("sa->i = %d\n", sa->i);
	
	return 0;
}
```
## C C++ 命名规范
请参考[C++命名规范](https://www.jianshu.com/p/028a1b22ecfa)与[Google C++命名约定](http://zh-google-styleguide.readthedocs.io/en/latest/google-cpp-styleguide/naming/)

## 指针加法
指针是有类型的，本质上标示的是一个整型（ssize_t)地址，可以进行加减法运算。但是跟普通整型加减法不同的是：指针的加减单位是相应指针类型在内存中的占用空间大小。例如：
```c
int *a = 0;
long *b = 0;
char *c = 0;
printf("%ld\n", a + 1);//output = 4
printf("%ld\n", b + 1);//output = 8
printf("%ld\n", c + 1);//output = 1
```

## `char str[]` 和 `char *str` 的区别（涉及到字符串常量的特点）
```c
// wrong function 
char* get_str(void){
    char str[] = {"abcd"};
    return str;
}

// right function 
char* get_str(void){
    char *str = {"abcd"};
    return str;
}

const char str[] ="abcd";       //abcd存储在堆栈中
const char *str ="abcd";        //abcd存储在静态存储区

// 数组和指针是不同的数据类型，有本质的区别：
char str[] ="abcd";        //sizeof(str) == 5 * sizeof(char)
char *str ="abcd";       //sizeof(str) == 4(x86) or 8(x64)
```
- `char str[] ={"abcd"};`定义了一个局部字符数组（放在堆栈中，函数调用完即销毁此段内存），尽管是数组，但它是一个局部变量，返回它的地址肯定是一个已经释放了的空间的地址。此函数返回的是内部一个局部字符数组str的地址，且函数调用完毕后此数组被销毁，所以你返回的指针也就指向一块被销毁的内存，这种写法是错误的。
- 此函数返回的是**字符串常量的地址**，而像这种字符串都是属于全局的，**在编译的时候就已经分配了内存了，只有程序退出的时候才会被销毁**，所以返回它的地址是没有问题的，但是你最好返回常量指针，因为你不能去改变字符串常量的值。