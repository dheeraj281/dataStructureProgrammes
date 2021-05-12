arr = [23, 38, 6, 12, 17, 66, 45, 77, 84, 90]
fruits = ["orange", "banana", "apple", "grapes", "mango"]

class Search:

    def binsearch_sortedArray(self, arr, item):
        arr.sort()
        low, high = 0, len(arr)
        while low <= high:
            mid = (low + high) // 2
            if item == arr[mid]:
                return arr.index(item)
            else:
                if item < arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1


    def binsearch_rotatedArray(self, arr, target):
        start, end = 0, len(arr)-1

        while start<= end:
            mid = (start+end)//2

            if arr[mid] == target:
                return arr.index(arr[mid])
            else:
                if arr[mid] > arr[start]:
                    if target >= arr[start] and target <= arr[mid]:
                        end = mid-1
                    else:
                        start = mid+1
                else:
                    if target >= arr[mid] and target <= arr[end]:
                        start = mid+1
                    else:
                        end = mid-1
        return -1

    def first_and_last_position(self, arr, target):
        """
        Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
        Input: nums = [5,7,7,8,8,10], target = 8
        Output: [3,4]

        """
        start = 0
        end = len(arr) - 1
        res = []
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == target:
                return [self.findLeft(arr, 0, mid, target), self.findRight(arr, mid, len(arr) - 1, target)]
            else:
                if target < arr[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
        return [-1, -1]

    def findLeft(self, arr, start, end, target):
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == target:
                if (mid > 0 and target > arr[mid - 1]) or mid == 0:
                    return mid
                else:
                    end = mid - 1
            else:
                if target < arr[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
        return -1

    def findRight(self, arr, start, end, target):
        while start <= end:
            mid = (start + end) // 2

            if arr[mid] == target:
                if (mid < len(arr) - 1 and target < arr[mid + 1]) or mid == len(arr) - 1:
                    return mid
                else:
                    start = mid + 1
            else:
                if target < arr[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
        return -1

    def search_Insert_Position(self, arr, target):
        """
        Given a sorted array of distinct integers and a target value, return the index if the target is found.
        If not, return the index where it would be if it were inserted in order.
        """
        arr.sort()
        low, high = 0, len(arr)
        while low <= high:
            mid = (low + high) // 2
            if target == arr[mid]:
                return arr.index(target)
            else:
                if target < arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        return low


s = Search()
print(s.binsearch_sortedArray(arr, 66))
print(s.binsearch_rotatedArray([4,5,6,7,0,1,2],0))
print(s.first_and_last_position([5,7,7,8,8,8,8,8,10],8))
print(s.search_Insert_Position([1,3,5,6],5))
print(s.search_Insert_Position([1,3,5,6],2))