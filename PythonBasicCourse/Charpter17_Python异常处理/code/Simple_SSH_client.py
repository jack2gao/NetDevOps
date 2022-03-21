"""
@description: ssh登录并处理异常

@author:Jack2Gao
@time:2022/3/20:22:52
"""
import socket

import paramiko


def ssh_login(ip, username, password, port=22, cmd="ls"):
    try:
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port=port, username=username, password=password, timeout=5, compress=True)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        result = stdout.read().decode()

        return result
    except paramiko.ssh_exception.AuthenticationException as e:
        print("认证错误", e)
    except socket.timeout as e:
        print("连接超时")
        print("%s'Error: %s" % (ip, e))
    except Exception as e:
        print("%s'Error: %s" % (ip, e))


def main():
    from argparse import ArgumentParser

    usage = "python Simple_SSH_client -i ipaddr -u username -p password -c command"

    parser = ArgumentParser(usage=usage)

    parser.add_argument('-i', "--ipaddr", dest="ipaddr", help="SSH server", default="192.168.1.1", type=str)
    parser.add_argument('-u', "--username", dest="username", help="SSH Username", default="root", type=str)
    parser.add_argument('-p', "--password", dest="password", help="SSH Password", default="jack", type=str)
    parser.add_argument('-c', "--command", dest="command", help="SSH Command", default="ls", type=str)

    args = parser.parse_args()
    print(ssh_login(args.ipaddr, args.username, args.password, cmd=args.command))


if __name__ == '__main__':
    main()
