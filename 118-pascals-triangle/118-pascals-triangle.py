class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for x in range(numRows+1)[2:]:
            temp = []
            for y in range(x):
                if(y != 0 and y != x-1):
                    temp.append(ans[x-2][y-1]+ans[x-2][y])
                else:
                    temp.append(1)
            ans.append(temp)
        return ans