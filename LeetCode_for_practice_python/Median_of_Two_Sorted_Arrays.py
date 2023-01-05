def findMedianSortedArrays(nums1, nums2):
    Ans = 0.0
    Ansvector = []
    checkindex = 0
    medianindex = 0

    Ansvector = nums1 + nums2
    Ansvector = sorted(Ansvector)
    checkindex = len(Ansvector)
    if (checkindex %2 == 1):
        print("odd")
        medianindex = int(checkindex/2)
        Ans = float(Ansvector[medianindex])
    elif (checkindex %2 == 0):
        print("even")
        medianindex = int(checkindex/2)
        Ans = float((Ansvector[medianindex]+Ansvector[medianindex-1])/2)
    print(Ans)
    return Ans

findMedianSortedArrays([1,3],[2])
findMedianSortedArrays([1,2],[3,4])