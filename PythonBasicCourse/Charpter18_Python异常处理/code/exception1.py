"""
@description:

@author:Jack2Gao
@time:2022/3/20:11:33
"""
import re


def findindex(obj,index):
    print(obj[index])


def main():
    #findindex("jack", 10)
    #IndexError: string index out of range
    # findindex("jack", "jack")
    #TypeError: string indices must be integers
    #findindex(10,"jack")
    #TypeError: 'int' object is not subscriptable

    try:
        findindex(10, "jack")
    except IndexError:
        print("索引错误")
    except TypeError as e:
        print("类型错误")
        print(e)
        err_massage = str(e)
        if "indices must be integers" in err_massage:
            print("索引必须是整数")
        elif re.match("\'(\w+)\'\s+object is not subscriptable",err_massage):
            print((re.match("\'(\w+)\'\s+object is not subscriptable",err_massage).groups()[0] + "不能被索引"))
    else:
        print("没有任何错误")
    finally:
        print("不管是否出错，都打印")

if __name__ == '__main__':
    main()
