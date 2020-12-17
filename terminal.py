import sys
import os
import platform
import getpass


#pwd = os.system('pwd')

l = os.getcwd()

username = getpass.getuser()


try:
   m = l.replace('/private/var/mobile/Containers/Data/Application/C55CFD3B-16DA-434C-8B46-F0AD54FB79AC', '')

except:
      m = l


platform = platform.node()


while True:
    
    select = input(f"""\033[0;31;40m
┌──[\033[1;32;40m{username}\033[1;33;40m@\033[94m{platform}\033[0;31;40m]-[\033[1;32;40m{m}\033[0;31;40m]
└──╼ \033[1;33;40m$\033[01;32m""")
    print("\033[01;32m")
    print(' \n')
    os.system(select)
