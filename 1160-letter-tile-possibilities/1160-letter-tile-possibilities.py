class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        sequences = set()
        is_choosed = [False for _ in range(len(tiles))]

        def backtrack(string):
            if string not in sequences:
                sequences.add(string)

            for i in range(len(tiles)):
                if not is_choosed[i]:
                    # Choose tiles[i] to append to string
                    is_choosed[i] = True
                    string = string + tiles[i]
                    backtrack(string)

                    # Reverse back
                    is_choosed[i] = False
                    string = string[:-1]

        backtrack('')

        return len(sequences) - 1

