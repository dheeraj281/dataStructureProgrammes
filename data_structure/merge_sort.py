
class Sorting:

    def mergeSort(self,arr):
        if len(arr) <= 1:
            return
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        self.mergeSort(left)
        self.mergeSort(right)
        self.merge_two_array(left, right, arr)


    def merge_two_array(self, left, right, arr):
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


    def bubbleSort(self,arr):

        for i in range(len(arr)-1):
            for j in range(0, len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp

testarr = [12, 9, 45, 23, 34, 57, 65, 90, 67, 43, 23]

customsort = Sorting()
customsort.mergeSort(testarr)
print(testarr)
