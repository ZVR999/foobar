# python foobar.py
import math
for num in range(100,100001):
    if math.sqrt(num)**2 == num:
        print 'foo'
    if num != 2 and num % 2 == 0:
        if num > 2 and num % num == 0: 
            print 'bar'
    else:
        print 'foobar'
        