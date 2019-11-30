"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total = len(nums1) + len(nums2)
        merged_list = (self.half_merge(nums1,nums2))
        median_index = int(total//2)
        print(merged_list)
        
        if total % 2 == 0:
          return (merged_list[median_index-1]+merged_list[median_index])/2.0
        else:
          return merged_list[median_index]

    def half_merge(self,list_a,list_b):
      new_list = []
      length = ((len(list_a)+len(list_b))/2)  + 1
      print(length)
      while (((len(list_a)>0) or (len(list_b)>0))) and len(new_list)<length:

        if len(list_a)<1:
          new_list.extend(list_b)
          list_b = []

        elif len(list_b)<1:
          new_list.extend(list_a)
          list_a = []
        else:
          if list_a[0] < list_b[0]:
            new_list.append(list_a[0])
            del list_a[0]
          else:
            new_list.append(list_b[0])
            del list_b[0]
      return new_list

 