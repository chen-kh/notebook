---
title: Java的List总结
categories: [Java知识]
tags: [Java知识, ArrayList, LinkedList, List]
---
# Java的List总结

## ArrayList和LinkedList在使用上的不同
其实很简单了，就是两种数据结构的不同。`ArrayList`按照`index`进行查询十分高效，但是删除和添加元素的过程涉及数据的`copy`操作，效率较低，但是删除末尾元素的话效率可是不低的，因为不涉及`copy`操作。`LinkedList`正好相反，按照`index`查询十分低效，但是删除和添加元素很高效，因为使用的链表的结构，数据在内存中是分散的。

总体来说比较容易区分两种类型的数据的使用场景，关键还是在于对jdk源码的理解，搞清楚数据和链表常用操作都是怎么实现的。下面是一些源码与注释。
```java
public class ArrayList<E> extends AbstractList<E>
        implements List<E>, RandomAccess, Cloneable, java.io.Serializable
{
    // 在末尾添加元素只有在数组元素不够的时候才会触发grow操作，也就是Arrays.copyof操作
    public boolean add(E e) {
        ensureCapacityInternal(size + 1);  // Increments modCount!!
        elementData[size++] = e;
        return true;
    }
    // 在指定位置插入的话，不光涉及上面的情况，还需要进行System.arraycopy操作移动数组
    public void add(int index, E element) {
        rangeCheckForAdd(index);

        ensureCapacityInternal(size + 1);  // Increments modCount!!
        System.arraycopy(elementData, index, elementData, index + 1,
                         size - index);
        elementData[index] = element;
        size++;
    }
    // 使用index进行删除，如果index不是最后一个才会触发System.arraycopy
    // 所以数组进行末尾删除的时候效率还是很高的
    public E remove(int index) {
        rangeCheck(index);

        modCount++;
        E oldValue = elementData(index);

        int numMoved = size - index - 1;
        if (numMoved > 0)
            System.arraycopy(elementData, index+1, elementData, index,
                                numMoved);
        elementData[--size] = null; // clear to let GC do its work

        return oldValue;
    }
    // 直接删除一个对象的话就是涉及到循环查找对象了。fastRemove跟remove基本一样，只是没有返回值
    public boolean remove(Object o) {
        if (o == null) {
            for (int index = 0; index < size; index++)
                if (elementData[index] == null) {
                    fastRemove(index);
                    return true;
                }
        } else {
            for (int index = 0; index < size; index++)
                if (o.equals(elementData[index])) {
                    fastRemove(index);
                    return true;
                }
        }
        return false;
    }
}

public class LinkedList<E>
    extends AbstractSequentialList<E>
    implements List<E>, Deque<E>, Cloneable, java.io.Serializable
{
    // 核心就是linkLast操作，很简单
    public boolean add(E e) {
        linkLast(e);
        return true;
    }
    
    // 核心是unlink操作，由于LinkedList是双向链表，操作起来不要太容易，效率不要太高。
    public boolean remove(Object o) {
        if (o == null) {
            for (Node<E> x = first; x != null; x = x.next) {
                if (x.item == null) {
                    unlink(x);
                    return true;
                }
            }
        } else {
            for (Node<E> x = first; x != null; x = x.next) {
                if (o.equals(x.item)) {
                    unlink(x);
                    return true;
                }
            }
        }
        return false;
    }

    // 删除指定小标的元素，首先会遍历数组找到这个元素。方法就是node(index)方法
    public E remove(int index) {
        checkElementIndex(index);
        return unlink(node(index));
    }
    
    // 同样是遍历的问题
    public E set(int index, E element) {
        checkElementIndex(index);
        Node<E> x = node(index);
        E oldVal = x.item;
        x.item = element;
        return oldVal;
    }
}
```