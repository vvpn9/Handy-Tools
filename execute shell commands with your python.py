# python调用系统命令
# 基于macos

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
