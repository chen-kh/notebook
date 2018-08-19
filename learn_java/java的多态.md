---
title: Java的多态
categories: [Java知识]
tags: [Java知识, 多态]
---
# Java的多态

## 静态绑定与动态绑定
- 静态绑定/前期绑定：简单的可以理解为程序编译期的绑定。java当中的方法只有final，static，private和构造方法是前期绑定
    - private方法不能被继承，只能通过这个类自身的对象来调用，因此private方法和类绑定在了一起。
    - final方法可以被继承，但不能被重写（覆盖）， 将方法声明为final类型，一是为了防止方法被覆盖，二是为了有效地关闭java中的动态绑定。
    - static方法可以被子类继承，但是不能被子类重写（覆盖），可以被子类隐藏。

- 动态绑定/后期绑定：在运行时根据具体对象的类型进行绑定。动态绑定的过程：虚拟机提取对象的实际类型的方法表 -> 虚拟机搜索方法签名 -> 调用方法。
- >与方法不同，在处理java类中的成员变量（实例变量和类变量）时，并不是采用运行时绑定，而是一般意义上的静态绑定。所以在向上转型的情况下，对象的方法可以找到子类，而对象的属性（成员变量）还是父类的属性（子类对父类成员变量的隐藏）。
```java
import java.util.ArrayList;
import java.util.List;

public class Polymorphism {
	public static void main(String[] args) {
		List<Animal> list = new ArrayList<>();
		// parent class' constructor is inherited by default, actually it invokes super() by default
		Animal dog = new Dog();
		System.out.println("dog instance of Animal dog: " + dog.getClass());
		Animal cat = new Cat();
		System.out.println("cat instance of Animal cat: " + cat.getClass());
		// list.add(cat);
		list.add(dog);
		for (Animal animal : list) {
			if (animal.name == "animal")
				System.out.println("animal.name = animal, so instance fields are statically bound");
			if (animal.toString().contains("color") || animal.toString().contains("eyes"))
				System.out.println("invoke subclass method, so instance methods are dynamically bound");
			System.out.println(animal.toString());
		}
		Animal.staticMethod();
		// static methods can be inherited
		Cat.staticMethod();
		// static method can be hidden but not override
		Dog.staticMethod();
		// it's deprecated, but it works and invoke the partent class static method 
		Animal dog2 = new Dog();
		dog2.staticMethod();
	}
}

class Animal {
	static String staticVar = "Animal StaticVar";
	String name = "animal";

	public Animal() {
		System.out.println("Animal is created");
	}

	@Override
	public String toString() {
		return name;
	}

	// @Override cause compile error
	public static void staticMethod() {
		System.out.println("I am Animal static method");
	}
}

class Dog extends Animal {
	static String staticVar = "Dog StaticVar";
	String name = "dog";
	String color = "color";

	@Override
	public String toString() {
		return super.toString() + ":" + color;
	}

	public static void staticMethod() {
		System.out.println("I am Dog static method");
	}
}

class Cat extends Animal {
	static String staticVar = "Cat StaticVar";
	String name = "cat";
	String eyes = "eyes";

	@Override
	public String toString() {
		return super.toString() + ":" + eyes;
	}
}
```
参考资料：
- [IBM: 多态在 Java 和 C++ 编程语言中的实现比较](https://www.ibm.com/developerworks/cn/java/j-lo-polymorph/)
- [JAVA动态绑定与静态绑定](https://www.jianshu.com/p/7a322d39d963)