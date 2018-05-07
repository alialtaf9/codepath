class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        #2A - 1 lists of size 2A-1
        response = [[0]*(2*A -1) for i in range(2*A -1)]
        startRowIndex = 0
        endRowIndex = 2*A-1
        startColumnIndex = 0
        endColumnIndex = 2*A-1
        currentNum = A
        for _ in range(A):
            for i in range(startColumnIndex, endColumnIndex):
                response[startRowIndex][i] = currentNum
            startRowIndex += 1

            for i in range(startRowIndex, endRowIndex):
                response[i][endColumnIndex-1] = currentNum
            endColumnIndex -=1

            for i in range(startColumnIndex, endColumnIndex):
                response[endRowIndex-1][i] = currentNum
            endRowIndex -= 1

            for i in range(startRowIndex, endRowIndex):
                response[i][startColumnIndex] = currentNum
            startColumnIndex += 1

            currentNum -= 1
        return response
