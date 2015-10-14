

class Solution(object):

    # time: O(n), space: O(1)
    def maxSubArray(self, nums):
        def f(l, r):
            if l == r:
                return [nums[l]] * 4
            else:
                m = (l + r) / 2
                mx1, lmx1, rmx1, sum1 = f(l, m)
                mx2, lmx2, rmx2, sum2 = f(m + 1, r)
                mx = max(max(mx1, mx2), rmx1 + lmx2)
                lmx = max(lmx1, sum1 + lmx2)
                rmx = max(rmx2, sum2 + rmx1)
                sum_ = sum1 + sum2
                return mx, lmx, rmx, sum_
        # mx (largest sum of this subarray), 
        # lmx(largest sum starting from the left most element), 
        # rmx(largest sum ending with the right most element), 
        # sum_(the sum of the total subarray). 
        mx, lmx, rmx, sum_ = f(0, len(nums) - 1)
        return mx

    # time: O(n) space: O(1)
    def maxSubArray2(self, nums):
        M = nums[0]
        pre = 0
        for n in nums:
            pre = n if pre < 0 else n + pre
            if pre > M:
                M = pre
        return M

    # time: O(n) space: O(n)
    def maxSubArray1(self, nums):
        submax = [nums[0]]
        for i in xrange(1, len(nums)):
            a = nums[i]
            b = submax[i - 1] + a
            c = b if b > a else a
            submax.append(c)
        return max(submax)

    # time: O(n**2) space: O(1)
    def maxSubArray0(self, nums):
        M = nums[0]
        for i in xrange(len(nums)):
            m = nums[i]
            t = 0
            for n in nums[i:]:
                t += n
                if t > m:
                    m = t
            if m > M:
                M = m
        return M


def main():
    test = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([-2, 3, -1, 4], 6)
    ]
    s = Solution()
    for nums, ans in test:
        a = s.maxSubArray2(nums)
        print(nums, ans, a, a == ans)

if __name__ == "__main__":
    main()
