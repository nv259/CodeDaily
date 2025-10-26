class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance        

    def _zero_index(self, index):
        return index - 1
    
    def _is_valid_account(self, account):
        return 1 <= account <= len(self.balance)
    
    def _is_enough_money(self, account, money):
        return self.balance[account] >= money

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not (self._is_valid_account(account1)
            and self._is_valid_account(account2)): return False

        account1 = self._zero_index(account1)
        account2 = self._zero_index(account2)

        if self._is_enough_money(account1, money):
            self.balance[account1] -= money
            self.balance[account2] += money
            return True
        
        return False
        

    def deposit(self, account: int, money: int) -> bool:
        if not self._is_valid_account(account): return False

        account = self._zero_index(account)
        self.balance[account] += money
         
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self._is_valid_account(account): return False
        account = self._zero_index(account)

        if self._is_enough_money(account, money):
            self.balance[account] -= money
            return True

        return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)