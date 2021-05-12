arr = [23, 38, 6, 12, 17, 66, 45, 77, 84,84, -90]


def findsecondLargest(arr):
    largest = arr [0]
    seclargest = arr[1]

    for i in arr[2:]:
        if i > largest:
            seclargest =largest
            largest = i
        elif i > seclargest and i != largest:
            seclargest = i

    return seclargest

print(findsecondLargest(arr))