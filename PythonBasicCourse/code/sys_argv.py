"""
example for app
v1.1
"""

def sys_argv(a,b):
    print(int(a) + int(b))


if __name__ == "__main__":
    import sys
    print(sys.argv[0])
    sys_argv(sys.argv[1], sys.argv[2])