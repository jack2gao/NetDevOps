"""
@description: 异常处理

@author:Jack2Gao
@time:2022/3/20:22:41
"""


def find_index(obj, index):
    print(obj[index])


def main():
    try:
        find_index("jack", "youyou")
    # except:      #捕获所有异常，除了Even system exit calls and ctrl + c key combinations，并忽略这些异常
    #     pass
    except Exception as e:  # 捕获所有异常，除了Even system exit calls and ctrl + c key combinationY意外的异常
        print(e)

    else:
        print("no err")

    finally:
        print("the end")


if __name__ == '__main__':
    main()
