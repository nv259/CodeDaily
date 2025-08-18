import itertools

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        sorted_cards = sorted(cards)
        all_perms = sorted(list([list(perm) for perm in itertools.permutations(sorted_cards)]))

        def op(x, y):
            op_results = [x + y, x - y, x * y]
            if y != 0: op_results.append(x / y)
            return op_results

        def backtrack(cards):
            if len(cards) == 1:
                return abs(cards[0] - 24) < 1e-5

            for i in range(len(cards) - 1):
                for new_card in op(cards[i], cards[i + 1]):
                    left_cards = cards[:i]
                    right_cards = cards[i + 2:] if i + 2 < len(cards) else []
                    # print(i, cards[i], i + 1, cards[i + 1], new_card)
                    left_cards.append(new_card)
                    new_cards = left_cards + right_cards
                    # print(cards, '=>', new_cards)
                    if backtrack(new_cards): return True
        
        for perm in all_perms:
            if backtrack(perm): return True

        return False

