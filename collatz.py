def collatz(n):
   
      if(n%2==0):
	n = n/2
        print(n)
      else:
	n =(3*n+1)/2
	print(n)

n = 10000
collatz(n)

for i in range(1,n+1):
   if not collatz(i):
     print(i + ' doesnot follow collatz conjecture ')
