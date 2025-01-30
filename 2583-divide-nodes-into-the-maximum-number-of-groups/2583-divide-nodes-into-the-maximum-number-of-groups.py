class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        # Represent graph as set of adjacency list
        def edges_to_adjacency_list(edges):
            adj_list = [[] for _ in range(n + 1)]
            for u, v in edges:
                adj_list[u].append(v)
                adj_list[v].append(u)
            return adj_list

        def is_bipartite(component, adj_list):
            # If a graph is bipartite, it's equivalently 2-colorable.
            # Moreover, once a node is colored 0, nodes in the other set will eventually
            # be colored 1. It's not bipartite otherwise. (*)
            color = { component[0]: True }
            q = deque([(component[0], True)])

            while q:
                u, color_u = q.popleft()

                for v in adj_list[u]:
                    # Color a node if it is uncolored, validate (*) otherwise.
                    if v in color:
                        if color[v] == color_u:
                            return False
                    else:
                        color[v] = not color_u
                        q.append((v, color[v]))
            
            return True

        # Find connected components
        def find_components(n, adj_list):
            groups = []
            visit = set()

            for node in range(1, n + 1):
                if node not in visit:
                    # bfs
                    q = deque([node])
                    group = [node]

                    while q:
                        u = q.popleft()
    
                        for v in adj_list[u]:
                            if v not in visit:
                                visit.add(v)
                                group.append(v)
                                q.append(v)

                    groups.append(group)

            return groups

        def num_groups_start_with_node(u, adj_list):
            group = { u:1 }     # node: group_idx
            q = deque([(u, 1)])

            while q:
                u, group_idx = q.popleft()

                for v in adj_list[u]:
                    if v not in group:
                        group[v] = group_idx + 1
                        q.append((v, group[v]))

            return max(group.values())

        adj_list = edges_to_adjacency_list(edges)
        components = find_components(n, adj_list)

        # For each component, find the maximum number of group of it
        res = 0

        for comp in components:
            # Check the viability of the component
            if not is_bipartite(comp, adj_list):
                return -1

            # Find the longest distance (maximum number of group)
            maximum_groups = 0

            for node in comp:
                num_groups = num_groups_start_with_node(node, adj_list)
                maximum_groups = max(maximum_groups, num_groups)
            
            res += maximum_groups

        return res         