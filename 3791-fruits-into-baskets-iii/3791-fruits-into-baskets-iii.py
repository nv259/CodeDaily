class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.arr = [0] * (4*n)

    def _merge(self, left_val, right_val):
        return max(left_val, right_val)

    def update(self, idx, val):
        self._update_recursive(1, 0, self.n - 1, idx, val)
    
    def _update_recursive(self, node_id, left, right, idx, val):
        if idx < left or right < idx: return 

        if left == right == idx:
            self.arr[node_id] = val
        else:
            mid = (left + right) // 2
            self._update_recursive(node_id * 2, left, mid, idx, val)
            self._update_recursive(node_id * 2 + 1, mid + 1, right, idx, val)
            self.arr[node_id] = self._merge(
                self.arr[node_id * 2],
                self.arr[node_id * 2 + 1]
            )
        return
    
    def query(self, val):
        return self._query_recursive(1, 0, self.n - 1, val)
    
    def _query_recursive(self, node_id, left, right, val):
        if self.arr[node_id] < val: return -1
        if left == right: 
            self.arr[node_id] = -1
            return left

        mid = (left + right) // 2 
        if self.arr[node_id * 2] >= val:
            basket_id = self._query_recursive(node_id * 2, left, mid, val)
        elif self.arr[node_id * 2 + 1] >= val:
            basket_id = self._query_recursive(node_id * 2 + 1, mid + 1, right, val)
        if basket_id != -1:
            self.arr[node_id] = self._merge(
                self.arr[node_id * 2],
                self.arr[node_id * 2 + 1]
            )
        return basket_id
        

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        # build segment tree
        basket_st = SegmentTree(len(baskets))
        for basket_idx, basket_size in enumerate(baskets):
            basket_st.update(basket_idx, basket_size)

        res = len(fruits) 
        for fruit_cnt in fruits:
            basket_idx = basket_st.query(fruit_cnt)
            if basket_idx != -1:
                # basket_st.update(basket_idx, -1)
                res -= 1

        return res
            
 