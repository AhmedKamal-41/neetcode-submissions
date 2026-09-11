class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = {'W': 0, 'B': 0}

        # 1. Build the first window: [0:k]
        for i in range(k):
            count[blocks[i]] += 1

        # Number of whites = recolors needed
        minimum = count['W']

        # 2. Slide the window
        l = 0

        for r in range(k, len(blocks)):
            # remove left character
            count[blocks[l]] -= 1

            # add right character
            count[blocks[r]] += 1

            # move left pointer
            l += 1

            # update minimum whites
            minimum = min(minimum, count['W'])

        return minimum