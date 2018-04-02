---
title: 初识二分图
categories: 数据结构与算法 #文章分类
tags: [数据结构与算法, 图, 二分图]      #文章标签，可以一次添加多个标签
---
# 初识二分图
<!-- TOC -->

- [什么是二分图？](#什么是二分图)
- [二分图研究问题](#二分图研究问题)
    - [最大匹配问题与完美匹配问题](#最大匹配问题与完美匹配问题)
        - [匈牙利算法](#匈牙利算法)
- [参考资料](#参考资料)

<!-- /TOC -->
## 什么是二分图？
**Wiki定义**

二分图指顶点可以分成两个不相交的集 **U** 和 **V**（**U** 和 **V** 皆为独立集：independent sets），使得在同一个集内的顶点不相邻（没有共同边）的图，又称双分图、二部图、偶图。

**符号化描述**

设 ***G=(V, E)*** 是一个无向图，如果顶点 **V** 可分割为两个互不相交的子集 **U** , **V**，并且图中的每条边 **(i,j)** 所关联的两个顶点 **i** 和 **j** 分别属于这两个不同的顶点集 ( **i** in **U**, **j** in **V**)，则称图 ***G*** 为一个二分图。

**图形化描述**

![二分图范例](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Simple-bipartite-graph.svg/250px-Simple-bipartite-graph.svg.png)

**应用场景示例**

学生与课程的关系，商家与顾客的关系，司机与乘客的关系等等。

## 二分图研究问题
先引入几个概念，文章[二分图的最大匹配、完美匹配和匈牙利算法](https://www.renfei.org/blog/bipartite-matching.html)中讲的非常好，这里直接引用。
> **匹配**：在图论中，一个「匹配」（matching）是一个边的集合，其中任意两条边都没有公共顶点。例如，图 3、图 4 中红色的边就是图 2 的匹配。
> <!-- 图片 -->
> ![Bipartite Graph(1)](https://img.renfei.org/2013/08/1.png)
![Bipartite Graph(2)](https://img.renfei.org/2013/08/2.png)
![Matching](https://img.renfei.org/2013/08/3.png)
![Maximum Matching](https://img.renfei.org/2013/08/4.png)  
> 
> 我们定义匹配点、匹配边、未匹配点、非匹配边，它们的含义非常显然。例如图 3 中 1、4、5、7 为匹配点，其他顶点为未匹配点；1-5、4-7为匹配边，其他边为非匹配边。  
> **最大匹配**：一个图所有匹配中，所含匹配边数最多的匹配，称为这个图的最大匹配。图 4 是一个最大匹配，它包含 4 条匹配边。  
> **完美匹配**：如果一个图的某个匹配中，所有的顶点都是匹配点，那么它就是一个完美匹配。图 4 是一个完美匹配。显然，完美匹配一定是最大匹配（完美匹配的任何一个点都已经匹配，添加一条新的匹配边一定会与已有的匹配边冲突）。但并非每个图都存在完美匹配。
> 
### 最大匹配问题与完美匹配问题
> 举例来说：如下图所示，如果在某一对男孩和女孩之间存在相连的边，就意味着他们彼此喜欢。是否可能让所有男孩和女孩两两配对，使得每对儿都互相喜欢呢？图论中，这就是完美匹配问题。如果换一个说法：最多有多少互相喜欢的男孩/女孩可以配对儿？这就是最大匹配问题。  
> 
> ![boys and girls](https://img.renfei.org/2013/08/0.png)

#### 匈牙利算法

详见[二分图的最大匹配、完美匹配和匈牙利算法](https://www.renfei.org/blog/bipartite-matching.html) 这文章写的太好。

匈牙利算法是解决最大匹配和完美匹配的一种算法，应用度很高。下面写一下匈牙利算法的大致过程，由于需要图形展示才能更好的理解，所以这里的大部分内容都是[二分图的最大匹配、完美匹配和匈牙利算法](https://www.renfei.org/blog/bipartite-matching.html)中的内容。但我加入了个人的理解，比原版要更容易理解。

首先明确两个概念：交替路和增广路
> ![figure 5](https://img.renfei.org/2013/08/5.png)
> 
> **交替路**：从一个未匹配点出发，依次经过非匹配边、匹配边、非匹配边…形成的路径叫交替路。
>
> **增广路**：从一个未匹配点出发，走交替路，如果途径另一个未匹配点（出发的点不算），则这条交替路称为增广路（agumenting path）。例如，图 5 中的一条增广路如图 6 所示（图中的匹配点均用红色标出）：
> 
> ![figure 6](https://img.renfei.org/2013/08/6.png)

增广路的首尾是非匹配点。因此，增广路径的第一条和最后一条边，必然是非匹配边；同时它的第二条边（如果有）和倒数第二条边（如果有），必然是匹配边；以及第三条边（如果有）和倒数第三条边（如果有），一定是非匹配边。

亦即，增广路径从非匹配边开始，匹配边和非匹配边依次交替，最后由非匹配边结束。这样一来，增广路径中非匹配边的数目会比匹配边大 1。

如果我们置换增广路径中的匹配边和非匹配边，由于增广路径的首尾是非匹配点，其余则是匹配点，这样的置换不会影响原匹配中其他的匹配边和匹配点，因而不会破坏匹配；亦即增广路径的置换，可以得到比原有匹配更大的匹配（具体来说，匹配的边数增加了 1）。

由于二分图的最大匹配必然存在（比如，上限是包含所有顶点的完全匹配），所以，再任意匹配的基础上，如果我们有办法不断地搜寻出增广路径，直到最终我们找不到新的增广路径为止，我们就有可能得到二分图的一个最大匹配。这就是**匈牙利算法的核心思想**。

**贪心思路的证明**

唯一的问题在于，在这种贪心的思路下，我们如何保证不存在例外的情况，即：当前匹配不是二分图的最大匹配，但已找不到一条新的增广路径。

我们从反证法考虑，即假设存在这样的情况。因为当前匹配不是二分图的最大匹配，那么在两个集合中，分别至少存在一个非匹配点。那么情况分为两种：

- 这两个点之间存在一条边——那么我们找到了一条新的增广路径，产生矛盾；
- 这两个点之间不存在直接的边，即这两个点分别都只与匹配点相连——那么：
    - 如果这两个点可以用已有的匹配点相连，那么我们找到了一条新的增广路径，产生矛盾；
    - 如果这两个点无法用已有的匹配点相连，那么这两个点也就无法增加匹配中边的数量，也就是我们已经找到了二分图的最大匹配，产生矛盾。
在所有可能的情况，上述假设都会产生矛盾。因此假设不成立，亦即贪心算法必然能求得最大匹配的解。

**贪心算法过程简述**

对二分图中的某一部分遍历，对每个节点查找增广路，如果查找到，交换匹配边与非匹配边；如果没有找到，计算下个节点。遍历完成后便得到了一个最大匹配。
代码见[二分图的最大匹配、完美匹配和匈牙利算法](https://www.renfei.org/blog/bipartite-matching.html)，此处引用。


```C++
// 顶点、边的编号均从 0 开始
// 邻接表储存
 

struct Edge
{
    int from;
    int to;
    int weight;

    Edge(int f, int t, int w):from(f), to(t), weight(w) {}
};

vector<int> G[__maxNodes]; /* G[i] 存储顶点 i 出发的边的编号 */
vector<Edge> edges;
typedef vector<int>::iterator iterator_t;
int num_nodes;
int num_left;
int num_right;
int num_edges;
int matching[__maxNodes]; /* 存储求解结果 */
int check[__maxNodes];

bool dfs(int u)
{
    for (iterator_t i = G[u].begin(); i != G[u].end(); ++i) { // 对 u 的每个邻接点
        int v = edges[*i].to;
        if (!check[v]) {     // 要求不在交替路中
            check[v] = true; // 放入交替路
            if (matching[v] == -1 || dfs(matching[v])) {
                // 如果是未盖点，说明交替路为增广路，则交换路径，并返回成功
                matching[v] = u;
                matching[u] = v;
                return true;
            }
        }
    }
    return false; // 不存在增广路，返回失败
}

int hungarian()
{
    int ans = 0;
    memset(matching, -1, sizeof(matching));
    for (int u=0; u < num_left; ++u) {
        if (matching[u] == -1) {
            memset(check, 0, sizeof(check));
            if (dfs(u))
                ++ans;
        }
    }
    return ans;
}
queue<int> Q;
int prev[__maxNodes];
int Hungarian()
{
    int ans = 0;
    memset(matching, -1, sizeof(matching));
    memset(check, -1, sizeof(check));
    for (int i=0; i<num_left; ++i) {
        if (matching[i] == -1) {
            while (!Q.empty()) Q.pop();
            Q.push(i);
            prev[i] = -1; // 设 i 为路径起点
            bool flag = false; // 尚未找到增广路
            while (!Q.empty() && !flag) {
                int u = Q.front();
                for (iterator_t ix = G[u].begin(); ix != G[u].end() && !flag; ++ix) {
                    int v = edges[*ix].to;
                    if (check[v] != i) {
                        check[v] = i;
                        Q.push(matching[v]);
                        if (matching[v] >= 0) { // 此点为匹配点
                            prev[matching[v]] = u;
                        } else { // 找到未匹配点，交替路变为增广路
                            flag = true;
                            int d=u, e=v;
                            while (d != -1) {
                                int t = matching[d];
                                matching[d] = e;
                                matching[e] = d;
                                d = prev[d];
                                e = t;
                            }
                        }
                    }
                }
                Q.pop();
            }
            if (matching[i] != -1) ++ans;
        }
    }
    return ans;
}
```

> **匈牙利算法的要点如下**  
从左边第 1 个顶点开始，挑选未匹配点进行搜索，寻找增广路。  
如果经过一个未匹配点，说明寻找成功。更新路径信息，匹配边数 +1，停止搜索。  
如果一直没有找到增广路，则不再从这个点开始搜索。事实上，此时搜索后会形成一棵匈牙利树。我们可以永久性地把它从图中删去，而不影响结果。  
由于找到增广路之后需要沿着路径更新匹配，所以我们需要一个结构来记录路径上的点。DFS 版本通过函数调用隐式地使用一个栈，而 BFS 版本使用 prev 数组。  
> 
> **性能比较**  
两个版本的时间复杂度均为O(V⋅E)O(V⋅E)。DFS 的优点是思路清晰、代码量少，但是性能不如 BFS。我测试了两种算法的性能。对于稀疏图，BFS 版本明显快于 DFS 版本；而对于稠密图两者则不相上下。在完全随机数据 9000 个顶点 4,0000 条边时前者领先后者大约 97.6%，9000 个顶点 100,0000 条边时前者领先后者 8.6%, 而达到 500,0000 条边时 BFS 仅领先 0.85%。

## 参考资料
[1] [二分图的最大匹配、完美匹配和匈牙利算法](https://www.renfei.org/blog/bipartite-matching.html)