class Graph:
    def __init__(self, n):
        self.n = n
        self.adj_list = { idx: [] for idx in range(self.n)}
    
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = Graph(len(amount))
        for u, v in edges:
            graph.add_edge(u, v)

        bob_visit_time = [float("inf") for _ in range(len(amount))]

        def bob_dfs(u, prev_node, time_step):
            if u == 0:
                bob_visit_time[u] = time_step
                return True

            for v in graph.adj_list[u]:
                if v != prev_node:  # eliminate cycles
                    is_path_to_root = bob_dfs(v, u, time_step + 1)

                    if is_path_to_root:
                        bob_visit_time[u] = time_step
                        return True
            
            return False
        
        def alice_dfs(u, prev_node, time_step, net_income):
            if time_step < bob_visit_time[u]:
                net_income += amount[u]
            elif time_step == bob_visit_time[u]:
                net_income += amount[u] // 2

            if u != 0 and len(graph.adj_list[u]) == 1:
                return net_income
            
            max_net_income = -float("inf")
            for v in graph.adj_list[u]:
                if v != prev_node: 
                    max_net_income = max(max_net_income, alice_dfs(v, u, time_step + 1, net_income)) 

            return max_net_income

        bob_dfs(bob, bob, 0)
        return alice_dfs(0, 0, 0, 0)
            