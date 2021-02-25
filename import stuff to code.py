import os, sys

# from a subdirectory

# > main.py
# > --->folder/
# > ----->file.py

# Do from folder.file import Klasa

# from a parent directory
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# sys.path 返回的是一个list
print(sys.path)

# 把路径添加到系统的环境变量
path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(path)
