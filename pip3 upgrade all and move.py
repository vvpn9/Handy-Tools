# 批量更新本地python三方库
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
# pip3 freeze -> requirements.txt
# macos默认生成在/Users/账户名地址下

# 下载需要的安装包依赖包到本地目录
# pip3 download -r requestments.txt -c requestments.txt -d pgk

# 拷贝至新机器安装
# pip3 install -r requestments.txt --no-index  --find-links pgk
