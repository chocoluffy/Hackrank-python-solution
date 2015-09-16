# -*- coding: UTF-8 -*-
from itertools import permutations

n = 8
cols = range(n)
for vec in permutations(cols):
    if (n == len(set(vec[i]+i for i in cols)) == len(set(vec[i]-i for i in cols))):
        print vec

        # 一下是为了pretty print那个具体的点阵
        for col in vec:
			s = ['- '] * len(vec)
			s[col] = 'Q '
			print ''.join(s)
		# print


# 将每一个vec 看作是每个row里面queen所在的位置， 也就是保证他们不在同一个row; 
# 比如（1，3，4，0）就是（0，1）（1，3）（2，4）（3，0）
# 然后使用permutations, 由于每个数字都有， 就保证他们不在同一个column;

# 剩下的就是要保证他们不在同一个diagonal；

# 使用一个性质： 注意每一个位置只和自己的row编号有关； 

# 1、如果同时减掉自己的所在row编号后的都的数字相同， 那么原来的时候他们在一个斜向右边下的diagonal上；
# 2、如果同时加上自己的所在row编号后得到的数字相同， 那么原来他们在一个斜向左边下面的diagonal上；


# 下面这个方法是使用backtracking来避开permutation效率上的不足， 因为总是会使用n!的选择来排除

def nqueens(r,n,p):
  s  = len(p)
  cols = range(s)
  valid = s == len(set(p[i] + i for i in cols)) == len(set(p[i] - i for i in cols))

  count = 0

  if valid:
    if r == n:
      return 1

    for c in set(range(n)) - set(p):
        count += nqueens(r + 1, n, p + [c])

  return count


def backtracknqueens(n):
    print n, nqueens(0,n,[])


backtracknqueens(8)






