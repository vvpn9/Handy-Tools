import os
import pathlib

# For python 2/3
print(os.path.dirname(os.path.abspath(__file__)))

print(os.path.abspath(os.getcwd()))

# For python 3
print(pathlib.Path(__file__).parent.absolute())

print(pathlib.Path().absolute())

# os.path.abspath() vs. os.path.realpath()
# 两者都可以取得绝对路径
# 但realpath可以取得软连接所定向的文件的真正位置
# e.g. A -> B
# realpath(A) -> B
