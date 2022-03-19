"""
@description:

@author:Jack2Gao
@time:2022/3/19:15:39
"""
import pickle
from datetime import  datetime

def main():
    db = {"key1":1}
    db["now"] = datetime.now()
    print(db)

    with open("D:\\PycharmProjects\\PythonCourse\\code\\people-pickle.pl","wb") as dbfile:
        pickle.dump(db,dbfile)

    with open("people-pickle.pl", 'rb') as dbfile:
        result = pickle.load(dbfile)
    print(result)

if __name__ == '__main__':
    main()
