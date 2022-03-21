"""
@description: 异常打印01

@author:Jack2Gao
@time:2022/3/20:22:28
"""

def find_index(obj, index):
    print(obj[index])

def main():
    # find_index(2,"jack")
    #TypeError: 'int' object is not subscriptable
    # find_index('jack', 'jack')
    #TypeError: string indices must be integers
    find_index("jack",10)
    #IndexError: string index out of range

if __name__ == '__main__':
    main()
