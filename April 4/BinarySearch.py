
def binarySearch(arr, l, r, x):

    if r >= l:

        mid = int(l + (r - l) / 2)


        if arr[mid] == x:
            return mid


        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)


        else:
            return binarySearch(arr, mid + 1, r, x)

    else:

        return -1



size = int(input("Enter Array size"))


print("Enter elements")
arr = []
for i in range(0,size):
    arr.append(int(input()))

x = int(input("Enter element to be searched for"))
# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index " , result)
else:
    print("Element is not present in array")
