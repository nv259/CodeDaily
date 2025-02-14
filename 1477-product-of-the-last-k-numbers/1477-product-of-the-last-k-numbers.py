class ProductOfNumbers:

    def __init__(self):
        self.arr = [1]
        self.arr_prod = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.arr = [1]
            self.arr_prod = [1]
        else: 
            self.arr.append(num)
            self.arr_prod.append(self.arr_prod[-1] * num)

    def getProduct(self, k: int) -> int:
        if k > len(self.arr) - 1:
            return 0

        return self.arr_prod[-1] // self.arr_prod[-k - 1]    


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)