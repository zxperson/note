import sys
import os

def readfile(filename):
    with open(filename) as f:
        while True:
            line = f.readline()
            if len(line) == 0:
                print('\033[0;31m%s读取完毕!!!\033[0m' % filename)
                break
            print(line)

def main():
    if len(sys.argv) < 2:
        print("输入的命令不完整")
        sys.exit()
    elif sys.argv[1].startswith('--'):
        option = sys.argv[1][2:]
        if option == 'version':
            print('Version 1.1.1')
        elif option == 'help':
            print('''\
    This program prints files to the standard output.
    Any number of files can be specified.
    Options include:
    --version : Prints the version number
    --help    : Display this help''')
        else:
            print('未知的选项!!!')
            sys.exit()
        
    else:
        for filename in sys.argv[1:]:
            if os.path.exists(filename):
                readfile(filename)    
            else:
                print('\033[0;32m%s这个文件不存在!!!\033[0m' % filename)

if __name__ == "__main__":
    main()
