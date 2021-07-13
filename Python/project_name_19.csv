import os

pwd = os.popen('pwd').readlines()[0].split('\n', 1)[0]

print(pwd)

num = 0
project_name = 'project_name'  # test, train, pred, etc.
for f in os.listdir(pwd):
    os.rename(os.path.join(pwd, f), os.path.join(pwd, project_name + '_' + str(num) + '.csv'))
    num += 1
