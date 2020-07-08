#pgm to find if the given number is armstrong number
n = int(input('Enter a number'))
print('The given number is',n)

#n = 123
#1**3 + 2**3 + 3**3 = 123
#36! = 123(not equal to), not an amstrong number

n1 = n
u = n%10 #u = 3
n = n//10 #n = 12
t = n%10 #t = 2
n = n//10 #n = 1
h = n%10 #h = 1

s = (u**3) + (t**3) + (h**3)

if (s==n1) :
    print('Armstrong number')
else :
    print('Not an armstrong number')