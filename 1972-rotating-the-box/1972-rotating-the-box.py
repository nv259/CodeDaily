class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        
        # Flush all the rocks to the right of the box, or until it is impeded by an obstacle
        for row_idx, row in enumerate(box):
            empty_ptr = n - 1
            while row[empty_ptr] != '.' and empty_ptr > 0: empty_ptr -= 1 

            # Flush all rocks to the right
            for col_idx in range(empty_ptr - 1, -1, -1):
                # Check whether the empty cell is appropriate or not
                if empty_ptr <= 0: break

                if row[col_idx] == '#': # If encouter a rock
                    # and simultaneously free the rock cell
                    box[row_idx][col_idx] = '.'
                    # Fill the right most empty cell with the rock
                    box[row_idx][empty_ptr] = '#'
                    # Update the pointer of viable empty cell
                    empty_ptr -= 1
                
                elif row[col_idx] == '*':   # If encounter an obstacle,
                    empty_ptr = col_idx - 1 # update the pointer of viable empty cell

                # If current cell is empty, do nothing
            
        # Transpose the box matrix
        box_transpose = [[box[i][j] for i in range(m - 1, -1, -1)]
                            for j in range(n)] 

        return box_transpose
