from sortedcontainers import SortedList 
        
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
            # tree.insert_value(u)
            tree.add(u)

            for v in adj_list[u]:
                if is_visited[v]: continue
                dfs(v, tree, group_idx) 

            return
    
        # Form groups
        group_cnt = 0
        avl_trees = []
        for u in range(1, c + 1):
            if not is_visited[u]:
                tree = SortedList()
                dfs(u, tree, group_cnt)
                avl_trees.append(tree)
                group_cnt += 1
        
        ans = []
        for type, station in queries:
            power_grid = avl_trees[group_ids[station]]
            if type == 2:
                is_online[station] = False
                power_grid.discard(station)
            else:
                if is_online[station]:
                    ans.append(station)
                else:
                    if len(power_grid) == 0:
                        ans.append(-1)
                    else:
                        ans.append(power_grid[0])

        return ans
        

# Solution().processQueries(5, [[1,2],[2,3],[3,4],[4,5]], [[1,3],[2,1],[1,1],[2,2],[1,2]])