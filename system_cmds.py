import os

print(os.name)             # posix
print(os.environ)          # environ({'SHELL': '/bin/bash', 'SESSION_MAN...
print(os.getcwd())         # /home/edwardjones/examples
os.chdir('/')              #
print(os.getcwd())         # /
os.system('ls | xargs')    # bin boot cdrom dev etc home lib lib32 lib64...
print(os.getenv)           # <function getenv at 0x7f9223623760>
print(os.get_exec_path())  # ['/usr/local/sbin', '/usr/local/bin', '/usr...
print(os.getuid())         # 1000
print(os.getpid())         # 39327
print(os.uname())          # posix.uname_result(sysname='Linux', nodenam...

###  example

import os

dir_list = os.listdir('/boot')

dirs = []
files = []

for item in dir_list:
   if os.path.isdir('/boot/' + item):
      dirs.append(item)
   else:
      files.append(item)

print("Dirs:")
print(dirs)
print("\nFiles:")
print(files)

###  example
