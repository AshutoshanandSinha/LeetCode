#Idea:

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1, l2 = len(nums1), len(nums2)

        # Step:1 find out the array with less number of items than other
        if l1 > l2:
            return self.findMedianSortedArrays(nums2, nums1)

        isodd = True if (len(nums1) + len(nums2)) % 2 != 0 else False

        # Step:2 define length of minimum length array (l1) as high
        low = 0
        high = l1

        # Step:3 while low reached to length of the array, do following
        #   partition x = (low+high)/2
        #   partition y  = (l1 + l2 + 1) // 2 - partx
        # define :
        # l1max,r2min, l2max, r1min
        # until found the scenario where l1max <= r2min and l2max <= r1min

        while low <= high:

            partx = (low + high) // 2
            party = (l1 + l2 + 1) // 2 - partx

            # print partx, party, low

            l1max = float("-inf") if partx == 0 else nums1[partx - 1]
            l2max = float("-inf") if party == 0 else nums2[party - 1]
            r1min = float("inf") if partx == l1 else nums1[partx]
            r2min = float("inf") if party == l2 else nums2[party]

            # print l1max,r2min, l2max, r1min

            if l1max <= r2min and l2max <= r1min:
                if not isodd:
                    return (max(l1max, l2max) + min(r1min, r2min)) / 2.0
                else:
                    return max(l1max, l2max)

            elif l1max > r2min:
                high = partx - 1
            else:
                low = partx + 1


if __name__ == '__main__':
    sol1 = Solution()
    nums1 = [1, 2]
    nums2 = [3, 4]

    res1 = sol1.findMedianSortedArrays(nums1, nums2)

    assert res1 == 2.5

    nums1 = [1, 3]
    nums2 = [5, 8]

    res2 = sol1.findMedianSortedArrays(nums1, nums2)

    assert res2 == 4.0
