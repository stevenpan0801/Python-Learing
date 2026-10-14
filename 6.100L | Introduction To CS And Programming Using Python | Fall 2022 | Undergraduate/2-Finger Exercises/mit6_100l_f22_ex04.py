N = int(input('Give a positive integer:'))

Flag = False
for i in range(N+1):
   if i**3 == N:
       print(i)
       Flag = True
       break
   elif i**3 > N:
       print('error')
       break
   else:
       continue
if not Flag:
   print('error')

i = 0
while i**3 < N:
    i += 1
if i**3 == N:
    print('The number ', i, ' is a perfect square')
else:
    print('error')