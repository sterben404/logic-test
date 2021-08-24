def logic(n): 
	hasil = 0
	for x in range(0,n):
	    x += 1
	    count = [i for i in range(0,n,15)]
	    hasil = hasil + x
	    if x in count:
	        print(',BMG',end=",")
	        
	    print(x,end="+")
	print(' =',hasil)
logic(50)
