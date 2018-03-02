# coding: UTF-8
print 'こんにちは'

a = 'hello world!'
b = a.replace('hello', 'morning')
print b

c = '10'
d = 10
print c == d

e = d == 10
print not e

f = [1, 'test', 10, 'test2', 20, 'test3', 30]
print f[2:4]

list1 = [123, 234, 345]
tuple1 = (123, 234, 345)

list1[1] = 111
list1.append(345)

# error
# tuple1[1] = 111
# tuple1.append(345)
print list1
print tuple1

dict1 = {'taro': 111, 'hanako': 222}
dict1['jiro'] = 1234
print dict1

it = 0
while it < 10:
    print it
    it += 1
