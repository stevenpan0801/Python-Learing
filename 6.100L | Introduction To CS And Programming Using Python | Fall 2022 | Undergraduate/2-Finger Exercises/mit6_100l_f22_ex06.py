N = int(input('Enter an integer 0<=N<=1000:'))
high = 1000
low = 0
guess = (high + low)/2
count = 1
while guess != N:
    if guess < N:
        low = guess
    else:
        high = guess
    guess = (high + low)//2
    count += 1
print("count:",count)
print("answer:",int(guess))
