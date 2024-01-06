def firstNonRepeating(arr, n):
    for i in range(n):
        j = 0
        while (j < n):
            if (i != j and arr[i] == arr[j]):
                break
            j += 1
        if (j == n):
            return arr[i]
    return -1
arr = [8, 4, 8, 6,6, 7, 4]
n = len(arr)
print("The first non repeating element is:",firstNonRepeating(arr, n))



