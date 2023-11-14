from django.test import TestCase
# Create your tests here.



n = int(input())
n = bin(n)
n = str(n)
n = sorted(n)
n = n[::-1]
n.remove('b')
n.remove('0')
x = ''.join(n)
x = int(x,2)
print(x)