class RecentCounter:

    def __init__(self):
        self.calls = deque()

    def ping(self, t: int) -> int:
        while self.calls:
            oldest_call = self.calls[0]
            
            if t - oldest_call > 3000: 
                self.calls.popleft()
            else: 
                break
        
        self.calls.append(t) 
        return len(self.calls)  


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)