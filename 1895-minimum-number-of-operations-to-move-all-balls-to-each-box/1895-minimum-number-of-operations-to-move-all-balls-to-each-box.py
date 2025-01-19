class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)

        def move_counts(arr):
            # prefix_sum[i]: number of steps to move all the ball 
            # from the left-most to i-th box
            prefix_sum = [0 for _ in range(n)]

            # calculate number of balls in each box
            for i in range(1, n):
                new_ball = 1 if arr[i - 1] == '1' else 0
                prefix_sum[i] = prefix_sum[i - 1] + new_ball

            # print(prefix_sum)
            for i in range(1, n):
                prefix_sum[i] = prefix_sum[i] + prefix_sum[i - 1]
            # print(prefix_sum)
            return prefix_sum

        # fill boxes from left and right seperately
        prefix_move_counts = move_counts(boxes)
        suffix_move_counts = move_counts(boxes[::-1])[::-1]

        # calculate the total number of moves
        res = [prefix_move_counts[i] + suffix_move_counts[i] for i in range(n)]

        return res