# reading an integer n
n = int(input('Type an integer value: '))

# THIS IS THE PART THAT WILL BE INSIDE THE SUBMITION FUNCTION

# going from 1 to n (inclusive)
for i in range(1, n + 1):
    if (i % 3 == 0) and (i % 5 == 0):
        print('FizzBuzz')
    if (i % 3 == 0) and (i % 5 != 0):
        print('Fizz')
    if (i % 3 != 0) and (i % 5 == 0):
        print('Buzz')
    if (i % 3 != 0) and (i % 5 != 0):
        print(i)
