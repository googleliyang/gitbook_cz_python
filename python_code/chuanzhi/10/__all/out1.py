# import child.dog
# from child import dog

# dog.say()

from child import *  # 需要 当 import * 一个 模块时，需要 __init__.py(必须要加 __all__), 以及当引入相对目录外层 模块时需要 __init__.py

dog.say()
