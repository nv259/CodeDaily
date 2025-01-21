class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        board = "".join(str(val) for val in board[0] + board[1])
        # define movable positions from each position
        adj = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }

        def bfs(state, goal):
            # initialize q with the start state
            q = deque([[state, 0]])   # state, path's length
            visited_states = set(state)

            while q:
                state, length = q.popleft()

                # check for goal state
                if state == goal: return length

                # visit the next state
                zero_index = state.index('0')
                for next_pos in adj[zero_index]:
                    new_state = list(state)
                    
                    # swap two tiles
                    temp = new_state[zero_index]
                    new_state[zero_index] = new_state[next_pos]
                    new_state[next_pos] = temp

                    new_state = "".join(new_state) 
                    # push new state into q if it has not been visited
                    if not new_state in visited_states:
                        visited_states.add(new_state)
                        q.append((new_state, length + 1))

            return -1

        return bfs(board, "123450")