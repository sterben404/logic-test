## SOLVED ##
global n
def logic(n):
    hasil = 0
    for x in range(0,n):
        x += 1
        count = [i for i in range(0,n,15)]
        s = [i - 1 for i in range(0,n,15)]
        hasil = hasil + x
        
        if x in count:
            print('BMG',end=",")
            continue
        if x in s:
            print(x, end=",")
            continue
        if x == n:
            print(x, end="")
            continue
        print(x,end="+")
    print(' =',hasil)
logic(20)
