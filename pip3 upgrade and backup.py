# 批量更新本地python三方库
# 基于macos

import os
import subprocess

# 检查三方库依赖关系
os.system('pip3 check')

# 若存在版本错误则需单独处理

# 批量更新三方库
command = "pip3 list --outdated"  # 使用pip3而非pip
outdatelist = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               shell=True).stdout.readlines()
updatelist = [bytes.decode(x).split(" ")[0] for x in outdatelist]
for x in updatelist[2:]:
    tempcmd = "pip3 install -U " + x
    print(subprocess.Popen(tempcmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                           shell=True).stdout.readlines())

# 在当前目录下生成备份文件
os.system('pip3 freeze > requirements.txt')

# 当前目录
os.system('pwd')

# 下载需要的安装包依赖包到本地目录
# pip3 download -r requestments.txt -c requestments.txt -d pgk

# 拷贝至新机器安装
# pip3 install -r requestments.txt --no-index  --find-links pgk
