class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeTwoSortedArray(arr1,arr2):
            result = []
            i= 0
            j =0
            while i<len(arr1) and j<len(arr2):
                if arr1[i] <= arr2[j]:
                    result.append(arr1[i])
                    i+=1
                else:
                    result.append(arr2[j])
                    j+=1
            if i<len(arr1):
                result.extend(arr1[i:])
            if j < len(arr2):
                result.extend(arr2[j:])    
            return result    
        def mergesort(arr):
            if(len(arr)<=1):
                return arr
            mid = len(arr) //2
            left = mergesort(arr[:mid])
            right = mergesort(arr[mid:])
            return mergeTwoSortedArray(left , right)
        return mergesort(nums)        

        