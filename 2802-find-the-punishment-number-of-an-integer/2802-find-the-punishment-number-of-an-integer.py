class Solution:
    def punishmentNumber(self, n: int) -> int:
        punishment_num = 0

        for i in range(1, n + 1):
            ii = i * i

            if self.can_partition(str(ii), i):
                punishment_num += ii

        return punishment_num

    def can_partition(self, string_num, target):
        if not string_num and target == 0:
            return True

        if target < 0:
            return False

        for i in range(len(string_num)):
            left = string_num[: i + 1]
            right = string_num[i + 1: ]
            left_num = int(left)

            if self.can_partition(right, target - left_num):
                return True

        return False
