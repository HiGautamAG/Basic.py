

def _Sum(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return(sum)

arr =[]    
arr = [12, 3, 4, 15]


n = len(arr)
ans = _Sum(arr)

print("Sum of the array is", ans)