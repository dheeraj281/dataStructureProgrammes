arr = [2, 7, 11, 15]

class SumProblems:

    def twosum(self,arr, target):
        """
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Output: Because nums[0] + nums[1] == 9, we return [0, 1].
        """
        mapped = {}
        for i, num in enumerate(arr):
            diff = target - num
            if diff not in mapped:
                mapped[num] = i
            else:
                return [i, mapped[diff]]

    def threeSum(self,arr):

        """
        Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
        and nums[i] + nums[j] + nums[k] == 0. Notice that the solution set must not contain duplicate triplets.
        Input: nums = [-1,0,1,2,-1,-4]
        Output: [[-1,-1,2],[-1,0,1]]
        """
        res = []
        arr.sort()
        for i, num in enumerate(arr):

            if i > 0 and num == arr[i-1]:
                continue

            left, right = i+1, len(arr)-1
            while left < right:
                newsum = num+ arr[left] + arr[right]
                if newsum > 0:
                    right-=1
                elif newsum < 0:
                    left+=1
                else:
                    res.append([num,arr[left], arr[right]])
                    left+=1
                    while left< len(arr) and [left] == arr[left-1]:
                        left+=1
        return res


    def threeSumClosest(self,arr, target):
        """
            Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
            Return the sum of the three integers. You may assume that each input would have exactly one solution.
        """
        arr.sort()
        res = sum(arr[0:3])

        for i, num in enumerate(arr):

            left, right = i+1, len(arr)-1
            while left < right:
                newsum = num + arr[left] + arr[right]
                if abs(target-newsum) < abs(target-res):
                    res = newsum
                if newsum < target:
                    left+=1
                    while left < len(arr) and arr[left] == arr[left-1]:
                        left+=1
                else:
                    right-=1

        return res




sumsol = SumProblems()
print(sumsol.twosum(arr, 17))

print(sumsol.threeSum([-1,0,1,2,-1,-4]))
print(sumsol.threeSumClosest( [-1,2,1,-4],1))

