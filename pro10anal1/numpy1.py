import numpy as np
ss = ['tom', 'james', 'oscar', 1, True]
print(ss, ' ', type(ss))

ss2 = np.array(ss)
print(ss2, ' ', type(ss2))

li = list(range(1, 10))
print(li)
print(id(li[0]), id(li[1]), hex(id(li[0])),hex(id(li[1])))
print(li * 10)
print("-- " * 10)

for i in li:
    print(i * 10, end = ' ')

print()
num_arr = np.array(li)
print(num_arr[0], ' ', num_arr[1], ' ', id(num_arr[0]), ' ', id(num_arr[1]))
print(num_arr * 10)

print()
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b, b.shape)
print(b[0], ' ', b[[0]], ' ', b[0, 0])

print()
c = np.zeros((2, 2))
print(c)

d = np.ones((2, 3))
print(d)

e = np.eye(3)
print(e)

print()
print(np.random.rand(5))
print(np.random.randn(5))

np.set_printoptions(threshold=np.inf)
print(np.mean(np.random.rand(5000)))
print(np.mean(np.random.randn(5000)))

np.random.seed(0)
print(np.random.randn(2, 3))

print('\n배열의 인덱싱과 슬라이싱')
aa = np.array([1,2,3,4,5])
print(aa, ' ', aa[1])
print(aa[1:4])
print(aa[1:])
print(aa[0:5:1])
print(aa[0:5:2])
print(aa[-2:])
print(aa[-4:-1])

print()
bb = aa
print(aa)
print(bb)
print(id(aa), ' ', id(bb))
print(bb)
print(aa)
cc = np.array(aa)
print(aa)
print(cc)
print(id(aa), ' ', id(cc))

print('\n\2차원 배열의 인덱싱과 슬라이싱')
dd = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])
print(dd, '\n', dd.shape)
print("인덱싱 ---")
print(dd[0])
print(dd[0, 0])
print(dd[2, 3])

print("슬라이싱 ---")
print(dd[0:2])
print(dd[1:])
print(dd[:, 0])
print(dd[:, [1]])
print(dd[1:3, 1:3])
print(dd[::])
print(dd[::2, :])
print(dd[::2, ::2])

print(dd[-1, -1])
print(dd[-1])
print(dd[:, -1])
print(dd[::-1])
print(dd[:, ::-1])