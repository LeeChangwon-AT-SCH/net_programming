# print function
print(10 + 20)
print("IoT")
print("abc " * 3)
x = 25; y = 32; z = x + y
print(x, y)
print(x, '+', y, '=', z)
# Seperator option
print('2022', '03', '02', sep='_')
print('20171522', 'sch.ac.kr', sep='@')
# format
print('{} and {}'.format('You', 'me'))
print('{0} and {1} and {0}'.format('a', 'b'))
print('{a} are {b}'.format(a='You', b='me'))
# %s: char %d: int %f: float
print("%s's favorite number is %d" %('Changwon Lee', 14))
# %5d: 5자리 정수, %4.2f: 정수 4자리, 소수점 이하 2자리
print("Test1: %5d, Price: %4.2f" %(776, 6534.123))
print("Test1: {0:5d}, Price: {1:4.2f}".format(776, 6534.123))
print("Test1: {a:5d}, Price: {b:4.2f}".format(a=776, b=6534.123))