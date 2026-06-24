class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        return  list(matrix.pop(0)) + self.spiralOrder(list(map(list,zip(*matrix)))[::-1])