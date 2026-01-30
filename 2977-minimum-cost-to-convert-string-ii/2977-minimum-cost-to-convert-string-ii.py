from typing import List, Dict
import heapq

class TrieNode:
    __slots__ = ("ch", "word_id")
    def __init__(self):
        self.ch: Dict[str, "TrieNode"] = {}
        self.word_id: int = -1

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s: str, wid: int):
        node = self.root
        for c in s:
            nxt = node.ch.get(c)
            if nxt is None:
                nxt = TrieNode()
                node.ch[c] = nxt
            node = nxt
        node.word_id = wid

class Solution:
    def minimumCost(self, source: str, target: str,
                    original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(source)
        if len(target) != n:
            return -1

        # 1) Compress nodes (unique strings)
        words = {}
        wid_list = []
        def get_id(s: str) -> int:
            if s in words:
                return words[s]
            words[s] = len(wid_list)
            wid_list.append(s)
            return words[s]

        for a, b in zip(original, changed):
            get_id(a); get_id(b)

        V = len(wid_list)

        # 2) Build adjacency with min edge cost per (u,v)
        edge_min = [dict() for _ in range(V)]
        for a, b, c in zip(original, changed, cost):
            u = words[a]
            v = words[b]
            prev = edge_min[u].get(v)
            if prev is None or c < prev:
                edge_min[u][v] = c

        adj = [[] for _ in range(V)]
        for u in range(V):
            for v, w in edge_min[u].items():
                adj[u].append((v, w))

        # 3) Build trie of all words (same trie works for both source and target)
        trie = Trie()
        maxLen = 0
        for s, wid in words.items():
            trie.insert(s, wid)
            if len(s) > maxLen:
                maxLen = len(s)

        # 4) Lazy Dijkstra cache: dist_cache[u] = list of distances from u
        dist_cache: Dict[int, List[int]] = {}

        INF = 10**30

        def dijkstra(start: int) -> List[int]:
            dist = [INF] * V
            dist[start] = 0
            pq = [(0, start)]
            while pq:
                du, u = heapq.heappop(pq)
                if du != dist[u]:
                    continue
                for v, w in adj[u]:
                    nd = du + w
                    if nd < dist[v]:
                        dist[v] = nd
                        heapq.heappush(pq, (nd, v))
            return dist

        # 5) DP with trie-walk on source and target simultaneously
        dp = [INF] * (n + 1)
        dp[0] = 0

        for i in range(n):
            if dp[i] >= INF:
                continue

            # single-char "do nothing"
            if source[i] == target[i]:
                if dp[i] < dp[i + 1]:
                    dp[i + 1] = dp[i]

            # try all word-length substrings starting at i that exist in the trie
            nodeS = trie.root
            nodeT = trie.root

            # walk up to maxLen, but break as soon as either path dies
            upper = min(n, i + maxLen)
            for k in range(i, upper):
                cs = source[k]
                ct = target[k]
                nodeS = nodeS.ch.get(cs)
                if nodeS is None:
                    break
                nodeT = nodeT.ch.get(ct)
                if nodeT is None:
                    break

                sid = nodeS.word_id
                tid = nodeT.word_id
                if sid != -1 and tid != -1:
                    if sid not in dist_cache:
                        dist_cache[sid] = dijkstra(sid)
                    d = dist_cache[sid][tid]
                    if d < INF:
                        j = k + 1
                        ndp = dp[i] + d
                        if ndp < dp[j]:
                            dp[j] = ndp

        return -1 if dp[n] >= INF else dp[n]
