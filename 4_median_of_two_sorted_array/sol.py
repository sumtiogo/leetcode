

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        N1, N2 = len(nums1), len(nums2)
        N = N1 + N2


    def findMedianSortedArrays1(self, nums1, nums2):
        "O(m+n)"
        nums = []
        idx1 = idx2 = 0
        while 1:
            if nums1[idx1] < nums2[idx2]:
                nums.append(nums1[idx1])
                idx1 += 1

            else:
                nums.append(nums2[idx2])
                idx2 +=1

            if idx1 == len(nums1):
                nums += nums2[idx2:]
                break

            if idx2 == len(nums2):
                nums += nums1[idx1:]
                break

        m = len(nums)
        if m % 2 == 1:
            return nums[m // 2]
        else:
            return (nums[m // 2] + nums[m // 2 - 1]) / 2


def main():
    tests = [
        ([1, 3], [2], 2),
        ([1, 2], [3, 4], 2.5),
    ]
    s = Solution()
    for nums1, nums2, ans in tests:
        res = s.findMedianSortedArrays(nums1, nums2)
        print(res == ans, res, ans)


if __name__ == "__main__":
    main()
