import numpy as np

aa = np.eye(3)
print(aa)

bb = np.c_[aa, aa[2]]
print('bb : \n', bb)

cc = np.r_[aa, [aa[2]]]
print('cc : \n', cc)

print('appent, insert, delete 함수 사용')
a = np.array([1,2,3])
print(a)
b = np.append(a, [4, 5], axis=0)
print(b)
c = np.insert(a, 0, [6, 7])
print(c)
d = np.delete(a, 1)
print(d)

print()
aa = np.arange(1, 10).reshape(3, 3)
print(aa)
print(np.insert(aa, 1, 99))
print(np.insert(aa, 1, 99, axis=0))
print(np.insert(aa, 1, 99, axis=1))

print()
x = np.array([1,2,3])
y = np.array([4,5,6])
conditionData = np.array([True, False, True])
result = np.where(conditionData, x, y)
print(result)

print()
print(x)
aa = np.where(x >= 2)
print(aa)
print(a[aa])

print()
kbs = np.concatenate([x, y])
print(kbs)

mbc, sbs = np.split(kbs, 2)
print('mbc : ', mbc)
print('sbs : ', sbs)

print()
a = np.arange(1, 17).reshape(4, 4)
print(a)
x1, x2 = np.hsplit(a, 2)
print(x1)
print(x2)

print()
print(np.vsplit(a, 2))
print('-------------------')

li = np.array([1,2,3,4,5,6,7])
sample1 = np.random.choice(li, size=3, replace = False)
print(sample1)
sample2 = np.random.choice(li, size=3, replace = True)
print(sample2)

print()
for _ in range(5):
    print(li[np.random.randint(0, len(li) - 1)], end = ' ')

print()
import random
print(random.sample(li.tolist(), 5))