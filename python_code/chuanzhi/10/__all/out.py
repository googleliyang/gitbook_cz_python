import sys

# sys.path.append('../')

# 不是不需要 __init__.py 吗

#..A imports are only allowed within a package.
from ..cat import *

# import cat.cat

cat.eat()
