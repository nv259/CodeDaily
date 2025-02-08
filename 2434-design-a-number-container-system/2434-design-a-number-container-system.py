class NumberContainers:

    def __init__(self):
        self.index_value = dict()   # index : value
        self.value_indices = dict() # value : List[index]

    def change(self, index: int, number: int) -> None:
        if number not in self.value_indices:
            self.value_indices[number] = []

        if index in self.index_value:
            old_value = self.index_value[index]
            self.index_value[index] = number

            # Pop the smallest index (indices) assigned with old value
            # if it (they) be outdated
            while (self.value_indices[old_value] and 
                    self.index_value[self.value_indices[old_value][0]] != old_value):
                heapq.heappop(self.value_indices[old_value])

        # Update number at the given index
        self.index_value[index] = number
        heapq.heappush(self.value_indices[number], index)
            
    def find(self, number: int) -> int:
        try:
            return self.value_indices[number][0]
        except:
            return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)