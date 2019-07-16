class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)+len(nums2)
        if n%2:
            return self.findkth(nums1,nums2,n//2+1)
        else:
            smaller = self.findkth(nums1,nums2,n//2)
            bigger = self.findkth(nums1,nums2,n//2+1)
            return (smaller+bigger)/2
        
        
    def findkth(self,A,B,k):
        if len(A)==0:
            return B[k-1]
        if len(B)==0:
            return A[k-1]
        
        if k==1:
            return min(A[0],B[0])
        if len(A)>=k//2:
            a=A[k//2-1]
        else:
            a= None
        
        if len(B)>=k//2:
            b=B[k//2-1]
        else:
            b=None
            
        if a is None or(b is not None and b<a):
            return self.findkth(A,B[k//2:],k-k//2)
        return self.findkth(A[k//2:],B,k-k//2)
    
        