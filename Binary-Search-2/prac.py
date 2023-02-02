arr =  [10, 20, 10] #[2, 1, 4, 2, 4, 1] # [7, 3, 20, 5, 15, 1, 11, 8, 10]
l = 0 
n = len(arr)
r = len(arr) - 1
res = 0
ls = arr[0]
rs = arr[-1]
while l < r:
    if ls == rs:
        res = l + n - r + 1
        print(res, l,n,r)
        l += 1
        r -= 1
        ls = arr[l]
        rs = arr[r] 
    elif ls < rs :
        l += 1
        ls += arr[l]
    else:
        r -= 1
        rs += arr[r] 
print(res, l, r)
