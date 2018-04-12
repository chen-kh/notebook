---
title: leetcode 题目与总结
categories: [offer, leetcode]
tags: [offer, leetcode]
---
# leetcode 题目与总结<!-- TOC -->

- [1. 二叉树](#1-二叉树)
    - [1.1. 前序遍历（递归、非递归）](#11-前序遍历递归非递归)
    - [1.2. 中序遍历（递归、非递归）](#12-中序遍历递归非递归)
    - [1.3. 后序遍历（递归、非递归）](#13-后序遍历递归非递归)
    - [1.4. 层次遍历与层次输出](#14-层次遍历与层次输出)
    - [1.5. 树的深度（略）](#15-树的深度略)
    - [1.6. 对称树](#16-对称树)
    - [1.7. 路径和（略）](#17-路径和略)
    - [1.8. 中序遍历加后序遍历恢复原树结构](#18-中序遍历加后序遍历恢复原树结构)
    - [1.9. 使用链表连接每一层](#19-使用链表连接每一层)
    - [1.10. 给定一棵树和一个节点，输出从根节点到这个节点的路径](#110-给定一棵树和一个节点输出从根节点到这个节点的路径)
    - [1.11. 两个节点的最小公共祖先](#111-两个节点的最小公共祖先)
    - [1.12. 树的序列化和反序列化](#112-树的序列化和反序列化)

<!-- /TOC -->


## 1. 二叉树
### 1.1. 前序遍历（递归、非递归）
递归版本是最基本的了。非递归的版本需要使用stack来保存访问的路径。
```java
class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> list = new ArrayList<Integer>();
        // method 1
        // preorderTraversalIter(root,list);
        // method 2
        Stack<TreeNode> stack = new Stack<TreeNode>();
        while(root != null || !stack.isEmpty()){
            if(root != null){
                stack.push(root);
                list.add(root.val);
                root = root.left;
            }else{
                root = stack.pop().right;
            }
        }
        return list;
    }
    public void preorderTraversalIter(TreeNode root, List<Integer> list) {
        if(root != null)
            list.add(root.val);
        else
            return;
        if(root.left != null)
            preorderTraversalIter(root.left, list);
        if(root.right != null)
            preorderTraversalIter(root.right, list);
    }
}
```
### 1.2. 中序遍历（递归、非递归）
```java
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> list = new ArrayList<Integer>();
        // method 1
        // inorderTraversalIter(root,list);
        // method 2
        Stack<TreeNode> stack = new Stack<TreeNode>();
        while(root != null || !stack.isEmpty()){
            if(root != null){
                stack.push(root);
                root = root.left;
            }else{
                root = stack.pop();
                list.add(root.val);
                root = root.right;
            }
        }
        return list;
    }
    public void inorderTraversalIter(TreeNode root, List<Integer> list) {
        if(root != null){
            if(root.left != null)
                inorderTraversalIter(root.left, list);
            list.add(root.val);
            if(root.right != null)
                inorderTraversalIter(root.right, list);
        }
    }
}
```
### 1.3. 后序遍历（递归、非递归）
后序遍历其实是镜像+颠倒版的前序遍历。使用右先前序遍历（先访问右节点）思想，最后倒着输出。
```java
class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> list = new LinkedList<Integer>();
        // method 1
        // postorderTraversalIter(root,list);
        // method 2
        Stack<TreeNode> stack = new Stack<TreeNode>();
        while(root != null || !stack.isEmpty()){
            if(root != null){
                stack.push(root);
                list.add(0, root.val);
                root = root.right;
            }else{
                root = stack.pop();
                root = root.left;
            }
        }
        return list;
    }
    public void postorderTraversalIter(TreeNode root, List<Integer> list) {
        if(root != null){
            if(root.left != null)
                postorderTraversalIter(root.left, list);
            if(root.right != null)
                postorderTraversalIter(root.right, list);
            list.add(root.val);
        }
    }
}
```
### 1.4. 层次遍历与层次输出
层次遍历很简单，使用队列辅助就行了。但是如何进行层次输出呢？这就是102号题目：[Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)。思路如下。

思路1：递归。设置level记录层数。每进行一次子节点访问，层数加1。不同层用不同list存储。具体见代码。
```java
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> levelList = new ArrayList<>();
        helper(root, levelList, 0);
        return levelList;
    }
    
    private void helper(TreeNode node, List<List<Integer>> levelList, int level){
        if (node == null) return;
        if (levelList.size() <= level) {
            levelList.add(new ArrayList<Integer>());
        }
        levelList.get(level).add(node.val);
        helper(node.left, levelList, level+1);
        helper(node.right, levelList, level+1);
    }
}
```

思路2：迭代。记录上下两层的数量。使用队列进行存储，但是记录前一层和当前层分别有多少个节点被存储了。当前一层还剩下0个节点的时候，存储成新的list。详见代码。
```java
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> lists = new ArrayList<List<Integer>>();
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        int preCount=0;
        int curCount=0;
        List<Integer> list = new ArrayList<Integer>();
        if(root != null){
            queue.offer(root);
            preCount++;
            while(!queue.isEmpty()){
                TreeNode node = queue.poll();
                list.add(node.val);
                preCount--;
                if(node.left != null){
                    queue.offer(node.left);
                    curCount++;
                }
                if(node.right != null){
                    queue.offer(node.right);
                    curCount++;
                }
                if(preCount == 0){
                    lists.add(new ArrayList(list));
                    list = new ArrayList<Integer>();
                    preCount = curCount;
                    curCount = 0;
                }
            }
        }
        return lists;
    }
}
```

思路3：迭代。双队列，第一个队列存储已经访问过的上一层的节点值，第二个队列存储当前访问层的节点值。
```java
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res=new ArrayList<>();
        if(root==null){
            return res;
        }
        Queue<TreeNode> queue=new LinkedList<>();
        queue.add(root);
        while(!queue.isEmpty()){
            List<Integer> list=new ArrayList<>();
            Queue<TreeNode> temp=new LinkedList<>();
            while(!queue.isEmpty()){
                TreeNode node=queue.poll();
                list.add(node.val);
                if(node.left!=null){
                    temp.add(node.left);
                }
                if(node.right!=null){
                    temp.add(node.right);
                }
            }
            res.add(list);
            queue=temp;     
        }
        return res;
    }
}
```

### 1.5. 树的深度（略）
### 1.6. 对称树
判断两棵子树是否对称是关键点，其它就是使用这个方法进行递归了。
```java
class Solution {
    public boolean isSymmetric(TreeNode root) {
        if(root == null)
            return true;
        return isEqual(root.left, root.right);
    }
    public boolean isEqual(TreeNode left, TreeNode right) {
        if(left == null && right == null)
          return true;
        if(left == null || right == null)
          return false;
        if(left.val != right.val)
            return false;
        return isEqual(left.left, right.right) && isEqual(left.right, right.left);
    }
}
```

### 1.7. 路径和（略）
### 1.8. 中序遍历加后序遍历恢复原树结构
需要对中后序遍历的关系搞得非常清楚才能写出这样的代码。真的很神奇。
```java
public class Solution {
    int p_inorder, p_postorder;
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        p_inorder = inorder.length - 1;
        p_postorder = postorder.length - 1;
        return buildTree(inorder, postorder, null);
    }
    public TreeNode buildTree(int[] inorder, int[] postorder, TreeNode end){
        if(p_postorder < 0)
            return null;
        TreeNode root = new TreeNode(postorder[p_postorder]);
        p_postorder--;
        // 判断是否存在右节点
        if(inorder[p_inorder] != root.val)
            root.right = buildTree(inorder, postorder, root);
        p_inorder--;
        // 判断是否存在左点， 当end==null时都是一棵左子树开始创建的时候
        if(end == null || inorder[p_inorder] != end.val)
            root.left = buildTree(inorder, postorder, end);
        return root;
    }
}
```

### 1.9. 使用链表连接每一层
```java
public class Solution {
    // for complete binary tree
    public void connect(TreeLinkNode root) {
        if( root == null )
            return;
        if( root.left != null ){
            root.left.next = root.right;
        }
        
        if( root.right != null){
            if( root.next != null ){
                root.right.next = root.next.left;
            }
        }
        
        connect( root.left );
        connect( root.right );
    }
    // for normal binary tree
    public void connect(TreeLinkNode root) {
        if( root == null )
            return;
        if( root.left != null ){
            root.left.next = root.right;
        }
        
        if( root.right != null){
            if( root.next != null ){
                root.right.next = root.next.left;
            }
        }
        
        connect( root.left );
        connect( root.right );
    }
}
```
### 1.10. 给定一棵树和一个节点，输出从根节点到这个节点的路径
思路就是，首先判断边界条件，如果根节点或者目标节点为空的话，就不用找了。正常情况下，使用一个列表记录路径，这个列表也相当于一个栈，使用遍历（回溯）的方法。当前节点不为空，入栈，如果栈顶节点等于目标节点，则找到了。如果不等于则需要判断是否需要出栈，情况有2，第一种，如果当前节点已经是叶节点了，出栈；第二种，如果当前节点的左右子树都没有找到这个节点，出栈。
```java
public boolean findPath(TreeNode root, TreeNode target, List<TreeNode> list) {
    boolean found = false;
    if(root == null || target == null)
        return found;
    list.add(root);
    if (root == target) {
        found = true;
    } else {
        boolean leftFound = false, rightFound = false;
        if (root.left == null && root.right == null) {
            list.remove(list.size() - 1);
        } else {
            leftFound = findPath(root.left, target, list);
            rightFound = findPath(root.right, target, list);
            found = (leftFound || rightFound);
            if (!found)
                list.remove(list.size() - 1);
        }
    }
    return found;
}
```

### 1.11. 两个节点的最小公共祖先
> If the current (sub)tree contains both p and q, then the function result is their LCA. If only one of them is in that subtree, then the result is that one of them. If neither are in that subtree, the result is null/None/nil.

算法的整体思路是：以当前节点为父节点（或者叫祖先节点），看它的左右两棵子树是否都包含p和q，由于p和q使用的是对象等于判断方法，所以如果两棵子树都包含的话，必定分别包含p和q，则直接返回当前节点。如果都不包含，那就是没有。如果一个包含一个不包含，返回包含的那个节点。

但是注意：这种编程方法只适合于两个节点都存在于树中的情况。如果有一个不存在的话输出的结果是有问题的。
```java
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root == p || root == q) return root;
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        return left == null ? right : right == null ? left : root;
    }
}
```

### 1.12. 树的序列化和反序列化
思路是将叶节点的子节点（null)也记录在案，这样无论是哪种遍历顺序（前中后，层次）都方便恢复。这里选择前序遍历进行序列化，反序列化就是前序遍历结果的反推。
```java
// Encodes a tree to a single string.
public String serialize(TreeNode root) {
    if (root == null)
        return "N,";
    String res = root.val + ",";
    res += serialize(root.left);
    res += serialize(root.right);
    return res;
}

// Decodes your encoded data to tree.
public TreeNode deserialize(String data) {
    if (data.length() <= 2)
        return null;
    // method 1
    // String[] vals = data.split(",");
    // return deserializeCore(vals);
    // method 2
    return deserializeCore2(new StringBuilder(data));
}

public TreeNode deserializeCore(String[] data) {
    if (MyCounter.count >= data.length)
        return null;
    String valStr = data[MyCounter.count];
    MyCounter.count++;
    if (valStr.equals("N")) {
        return null;
    }
    TreeNode node = new TreeNode(Integer.parseInt(valStr));
    node.left = deserializeCore(data);
    node.right = deserializeCore(data);
    return node;
}

public TreeNode deserializeCore2(StringBuilder data) {
    if (data.length() <= 0)
        return null;
    int idx = data.indexOf(",");
    String valStr = data.substring(0, idx);
    data.delete(0, idx + 1);
    if (valStr.equals("N")) {
        return null;
    }
    TreeNode node = new TreeNode(Integer.parseInt(valStr));
    node.left = deserializeCore2(data);
    // data.delete(0, data.indexOf(",") + 1);
    node.right = deserializeCore2(data);
    return node;
}
class MyCounter {
	static int count = 0;
}
```