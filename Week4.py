def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True

arr = [6, 2, 5, 4, 3]
print("Before sort:")
print(arr)

arr.sort()
print("After sort:")
print(arr)

if is_sorted(arr):
    print("The array is sorted.")
else:
    print("The array is not sorted.")
