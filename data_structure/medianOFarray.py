nums1= [2,4,5,6,7,12]
nums2= [15,17,18,19,25]

def median_of_sorted_array(nums1, nums2):
    X = min(nums1,nums2, key=len)
    Y = max(nums1,nums2, key=len)

    start = 0
    end = len(X)

    while True:
        partitionX = (start+end)//2
        partitionY = (len(X)+len(Y)+1)//2 - partitionX

        leftX, rightX = X[:partitionX] or [float('-inf')], X[partitionX:] or [float('inf')]
        leftY, rightY = Y[:partitionY] or [float('-inf')], Y[partitionY:] or [float('inf')]

        if max(leftX) <= min(rightY) and max(leftY) <= min(rightX):
            if (len(X) + len(Y)) % 2 != 0:
                return max(max(leftX), max(leftY))
            else:
                num1 = max(max(leftX), max(leftY))
                num2 = min(min(rightX), min(rightY))
                return (num1 + num2) / 2

        if max(leftX) > min(rightY):
            end = partitionX-1
        if max(leftY) > min(rightX):
            start = partitionX+1

print( median_of_sorted_array(nums1, nums2) )