---
title: leetcode 题目与总结
categories: [offer, leetcode]
tags: [offer, leetcode]
---
# leetcode 题目与总结
## 二叉树
### 前序遍历（递归、非递归）
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
### 中序遍历（递归、非递归）
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
### 后序遍历（递归、非递归）
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
### 层次遍历与层次输出
层次遍历很简单，使用队列辅助就行了。但是如何进行层次输出呢？这就是102号题目：[Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)。思路如下。

思路1：递归。设置level记录层数。每进行一次子节点访问，层数加1。不同层用不同list存储。具体见代码。
```java
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> levelList = new ArrayList<>();
        helper(root, levelList, 0);
        return levelList;
    }
    
    private void helper(TreeNode node, List<List<Integer>> levelList, int level) {
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