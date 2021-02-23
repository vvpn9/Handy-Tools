# 批量更新本地python三方库
# 基于macos

import subprocess

command = "pip list --outdated"
outdatelist = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               shell=True).stdout.readlines()
updatelist = [bytes.decode(x).split(" ")[0] for x in outdatelist]
for x in updatelist[2:]:
    tempcmd = "pip install -U " + x
    print(subprocess.Popen(tempcmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                           shell=True).stdout.readlines())

# 检查三方库中依赖关系
# pip3 check

# 生成版本文件
# cd /Users/账户名/Desktop
# pip3 freeze -> requirements.txt
# 桌面上即可获得txt格式的版本文件

# 下载需要的安装包依赖包到本地目录
# pip3 download -r requestments.txt -c requestments.txt -d pgk

# 拷贝至新机器安装
# pip3 install -r requestments.txt --no-index  --find-links pgk
