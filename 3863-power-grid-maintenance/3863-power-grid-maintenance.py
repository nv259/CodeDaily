class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1 


class AVLTree:
    def __init__(self):
        self.root = None
        
    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def insert(self, root, value):
        if not root: 
            return Node(value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        root.height = 1 + max(self.height(root.left),
                              self.height(root.right))
        balance = self.balance(root)

        # LL imbalance
        if balance > 1 and value < root.left.value:
            return self._right_rotate(root)

        # RR imbalance
        if balance < -1 and value > root.right.value:
            return self._left_rotate(root)

        # LR imbalance
        if balance > 1 and value > root.left.value :
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)

        # RL imbalance
        if balance < -1 and value < root.right.value:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)
        
        return root
    
    def delete(self, root, value):
        if not root:
            return root
        elif value < root.value:
            root.left = self.delete(root.left, value)
        elif value > root.value:
            root.right = self.delete(root.right, value)
        elif value == root.value:
            if not root.left:
                tmp = root.right
                root = None
                return tmp
            elif not root.right:
                tmp = root.left
                root = None
                return tmp

            tmp = self.min_value_node(root.right)
            root.value = tmp.value
            root.right = self.delete(root.right, tmp.value)

        if not root:
            return root

        root.height = 1 + max(self.height(root.left),
                              self.height(root.right))
        balance = self.balance(root)

        # LL imbalance
        if balance > 1 and self.balance(root.left) >= 0:
            return self._right_rotate(root)

        # RR imbalance
        if balance < -1 and self.balance(root.right) <= 0:
            return self._left_rotate(root)

        # LR imbalance
        if balance > 1 and self.balance(root.left) < 0:
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)

        # RL imbalance
        if balance < -1 and self.balance(root.right) > 0:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)

        return root
    
    def _left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def _right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3
        
        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def min_value_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    def search(self, root, value):
        if not root or root.value == value:
            return root

        if root.value < value:
            return self.search(root.right, value)
        return self.search(root.left, value)

    def insert_value(self, value):
        self.root = self.insert(self.root, value)

    def delete_value(self, value):
        self.root = self.delete(self.root, value)

    def search_value(self, value):
        self.root = self.search(self.root, value)
    
        
class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        is_online = [True] * (c + 1)
        adj_list = [[node_id] for node_id in range(c + 1)]
        # Convert to the adjacent list
        for u, v in connections:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        is_visited = [False] * (c + 1)
        group_ids = [0] * (c + 1)
        def dfs(u, tree, group_idx):
            is_visited[u] = True
            group_ids[u] = group_idx
            tree.insert_value(u)

            for v in adj_list[u]:
                if is_visited[v]: continue
                dfs(v, tree, group_idx) 

            return
    
        # Form groups
        group_cnt = 0
        avl_trees = []
        for u in range(1, c + 1):
            if not is_visited[u]:
                tree = AVLTree()
                dfs(u, tree, group_cnt)
                avl_trees.append(tree)
                group_cnt += 1
        
        ans = []
        for type, station in queries:
            power_grid = avl_trees[group_ids[station]]
            if type == 2:
                is_online[station] = False
                power_grid.delete_value(station)
            else:
                if is_online[station]:
                    ans.append(station)
                else:
                    if power_grid.root is None: 
                        ans.append(-1)
                    else:
                        ans.append(power_grid.min_value_node(power_grid.root).value)

        return ans
        

# Solution().processQueries(5, [[1,2],[2,3],[3,4],[4,5]], [[1,3],[2,1],[1,1],[2,2],[1,2]])