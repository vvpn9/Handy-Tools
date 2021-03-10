str8 = "3万"
# a=str8.find("Python")
# print a
# b = str8.find("和")
# print(b)
word = str8.split("万")  # Python3 和Spark 这里可以直接正确分割中文
print(word)
