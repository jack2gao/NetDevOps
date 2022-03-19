"""
@description: shelve

@author:Jack2Gao
@time:2022/3/19:15:55
"""

import shelve
from datetime import datetime


def main():

    db1 = {"key1":1}
    db1["now"] = datetime.now()
    db2 = {"key2":2}
    db2["old"] = datetime.now()
    db = shelve.open("people-shelve")
    db['cq_bomb'] = db1
    db['db2'] = db2
    db["datetime"] = datetime.now()
    db.close()

    db = shelve.open('people-shelve')
    db.get("db2")
    print(db.get("db2"))
    for key in db.get("db2").keys():
        print(key + ":" + str(db.get("db2")[key]))



if __name__ == '__main__':
    main()
