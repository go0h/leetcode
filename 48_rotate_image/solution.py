class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        side = len(matrix) - 1

        for circle in range((side + 1) // 2):
            for i in range(0, side - (circle * 2)):
                
                top = matrix[circle][circle + i]

                right = matrix[circle + i][side - circle]

                bottom = matrix[side - circle][side - circle - i]

                left = matrix[side - circle - i][circle]

                matrix[circle][circle + i]= left
                matrix[circle + i][side - circle] = top
                matrix[side - circle][side - circle - i] = right
                matrix[side - circle - i][circle] = bottom
    
if __name__ == '__main__':

    matrix = [[1,2], [3,4]]
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    print('\n'.join([' '.join([str(cell) for cell in row]) for row in matrix]))
    Solution().rotate(matrix)
    print('-' * 40)
    print('\n'.join([' '.join([str(cell) for cell in row]) for row in matrix]))