def test(lenght):
    arr = [0, 1]
    while len(arr) < lenght:
        res = len(arr)
        arr.append(arr[res - 1 ] + 1)
    print(arr)
test(50)