class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        m = len(meetings)
        has_secret = [False] * n
        has_secret[0] = True
        has_secret[firstPerson] = True
        
        def dfs(u, adj_list, is_visited):
            is_visited[u] = True 

            for v in adj_list[u]:
                if not is_visited[v]: 
                    has_secret[v] = True
                    dfs(v, adj_list, is_visited)  

            return
            
        def build_adj_graph_from_edge_list(edges):
            unique_nodes = set()
            for u, v in edges:
                unique_nodes.add(u)
                unique_nodes.add(v)

            adj_list = {}
            for u, v in edges:
                if u not in adj_list:
                    adj_list[u] = []
                adj_list[u].append(v)
                
                if v not in adj_list:
                    adj_list[v] = []
                adj_list[v].append(u)
            
            return adj_list, unique_nodes
            
        for i in range(len(meetings)):
            meetings[i] = [meetings[i][2], meetings[i][0], meetings[i][1]]
        meetings.sort()
        
        i = 0
        is_visited = [False] * n
        while i < m:
            curr_meeting_time = meetings[i][0]
            edges = []
            while i < m and meetings[i][0] == curr_meeting_time:
                u, v = meetings[i][1], meetings[i][2]
                edges.append((u, v))
                is_visited[u] = False
                is_visited[v] = False
                i += 1
            adj_list, unique_nodes = build_adj_graph_from_edge_list(edges)
            # del edges
            
            for u in unique_nodes:
                if not is_visited[u] and has_secret[u]:
                    dfs(u, adj_list, is_visited)

        ans = []
        for i in range(n):
            if has_secret[i]:
                ans.append(i)
        return ans