class Solution:
    def maximumSum(self, arr):
        max_,x,y=arr[0],arr[0],0
        for num in arr[1:]:
            x,y=max(x+num,num),max(y+num,x)
            max_=max(y,max_)
        return max(max_,x)


if __name__ == "__main__":
    a = Solution()
    print(a.maximumSum([4, -3, -3, 5, -6, 7]))