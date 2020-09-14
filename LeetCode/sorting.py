def selection_sort(arr):
    for index in range(len(arr)):
        get_min_inx = arr.index(min(arr[index:]))
        arr[get_min_inx], arr[index] = arr[index], arr[get_min_inx]
    return arr


def insert_sort(arr):
    for index in range(1,len(arr)):
        key = arr[index]
        j = index - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def merge_sort(arr,low, high):
    if len(arr) > 1:
        mid = (low +(high-low))//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L, 0, len(L))
        merge_sort(R, 0, len(R))

        i, j, k = 0, 0, 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i +=1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def merge(arr,i,m,k):
        index = 0
        j = m
        print (i,j,m,k)
        while i < m and j < k:
            if arr[i] > arr[j]:
                arr[index] = arr[j]
                j += 1
            else:
                arr[index] = arr[i]
                i += 1
            index += 1

def partition(arr, low, high):
        pivot = arr[high]
        index = low-1
        for i in range(low,high):
            if arr[i] <= pivot:
                index += 1
                arr[index], arr[i] = arr[i], arr[index]
        arr[index+1], arr[high] = arr[high], arr[index+1]
        return index+1


def quick_sort(arr,low,high):
    if low<high:
        p = partition(arr,low,high)
        quick_sort(arr,low,p-1)
        quick_sort(arr,p+1,high)


if __name__ == '__main__':

    nums = [3, 7, 2, 9, 5, 8]

    merge_sort(nums,0,len(nums))

    print (nums)

    nums = [3, 7, 2, 9, 5, 8]

    quick_sort(nums,0,len(nums)-1)

    print(nums)





