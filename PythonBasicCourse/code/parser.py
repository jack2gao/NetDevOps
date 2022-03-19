def t_argparse(host,filename,iface):
    print(host)
    print(filename)
    print(iface)

if __name__ == '__main__':
    from argparse import  ArgumentParser

    usage = "python arg_parse.py - t host -f fileneme -i interface"

    parser = ArgumentParser(usage=usage)

    parser.add_argument("-f", "--file", dest="filename", help="Write content to FILE", default="1.txt", type=str)
    parser.add_argument("-i", "--interface", dest="iface", help="spicify an interface", default=1, type=int)
    parser.add_argument("-t", "--host", dest="host", help="specify some hosts", default="10.1.1.1", type=str)
    parser.add_argument(nargs="*", dest="hosts", help="specify some hosts", default="10.1.1.1", type=str)
    args = parser.parse_args()

    t_argparse(args.host, args.filename, args.iface)