class Solution:
    def maxArea(self, height: List[int]) -> int:
        mx=0
        front = 0
        tail = len(height)-1

        while front<tail:
            area = (tail-front)*min(height[front], height[tail])
            if height[front] < height[tail]:
                front+=1
            else:
                tail-=1
            mx = max(mx, area)
        return mx
