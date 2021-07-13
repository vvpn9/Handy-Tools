# python调用系统命令
# 基于macOS Big Sur Version 11.2.1

# os module
# 如下方法缺点在于不能将输出结果作为变量

import os
import shlex
import subprocess

os.system('ls -al')

# 如下方法可以将结果作为变量

stream = os.popen('echo Returend output')
output = stream.read()  # 所有输出结果视作str，亦可使用.readlines()逐行读取

"""
output.strip()
output.lstrip()
output.rstrip()
"""

print(output)

# subprocess module

# 主要使用
# subprocess.run() 但不捕获结果

# 只能一次性执行一条命令as a list
process = subprocess.Popen(['echo', 'More output'],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
print(stdout)
print(stderr)

with open('test.txt', 'w') as f:
    process = subprocess.Popen(['ls', '-al'], stdout=f, universal_newlines=True)
    # uni方法解决bytes输出形式

# .communicate()会等到进程结束才执行，如下可避免
process = subprocess.Popen(['ping', '-c 4', 'baidu.com'],  # 请求十次
                           stdout=subprocess.PIPE,
                           universal_newlines=True)

while True:
    output = process.stdout.readline()  # single line
    print(output.strip())
    # Do something else
    return_code = process.poll()  # check the return code of the process
    # .poll()返回None当进程持续运行
    if return_code is not None:
        print('RETURN CODE', return_code)
        # Process has finished, read rest of the output
        for output in process.stdout.readlines():
            print(output.strip())
        break  # 跳出整个循环

# 针对不确定如何反向分解shell中命令
# shlex module

print(shlex.split("/bin/prog -i data.txt -o \"more data.txt\""))

# subprocess.call() 等待命令执行结束并返回结果
return_code = subprocess.call(['echo', 'even more output'])

# subprocess.run() 返回 subprocess.CompletedProcess object
process = subprocess.run(['echo', 'even more output'],
                         stdout=subprocess.PIPE,
                         universal_newlines=True)

print(process)

print(process.stdout)

# # 输入命令
# ssh = subprocess.Popen(["ssh", "-i .ssh/id_rsa", "user@host"],
#                        stdin=subprocess.PIPE,
#                        stdout=subprocess.PIPE,
#                        stderr=subprocess.PIPE,
#                        universal_newlines=True,
#                        bufsize=0)
#
# # Send ssh commands to stdin
# ssh.stdin.write("uname -a\n")
# ssh.stdin.write("uptime\n")
# ssh.stdin.close()
#
# # Fetch output
# for line in ssh.stdout:
#     print(line.strip())


# os.listdir()用于返回一个由文件名和目录名组成的列表
#
# os.path.isdir()用于判断对象是否为一个目录
#
# os.path.isfile()用于判断对象是否为一个文件

# os.path.join()函数：连接两个或更多的路径名组件
#
# 1.如果各组件名首字母不包含’/’，则函数会自动加上
# 2.如果有一个组件是一个绝对路径，则在它之前的所有组件均会被舍弃
# 3.如果最后一个组件为空，则生成的路径以一个’/’分隔符结尾
#
# Demo1
# import os
#
# Path1 = 'home'
# Path2 = 'develop'
# Path3 = 'code'
#
# Path10 = Path1 + Path2 + Path3
# Path20 = os.path.join(Path1,Path2,Path3)
# print ('Path10 = ',Path10)
# print ('Path20 = ',Path20)
