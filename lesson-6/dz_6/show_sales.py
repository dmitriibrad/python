import sys


def show_all():
    for line in g_bakery:
        print(line.rstrip('\n'))


def show_start(start):
    for i, line in enumerate(g_bakery):
        if i >= start - 1:
            print(line.rstrip('\n'))


def show_start_end(start, end):
    for i, line in enumerate(g_bakery):
        if start - 1 <= i < end:
            print(line.rstrip('\n'))
        if i == end:
            break


if __name__ == '__main__':
    f_bakery = open("bakery.csv", 'r', encoding='utf-8')
    g_bakery = (line for line in f_bakery)
    if len(sys.argv) == 1:
        show_all()
    if len(sys.argv) == 2:
        show_start(int(sys.argv[1]))
    if len(sys.argv) > 2:
        show_start_end(int(sys.argv[1]), int(sys.argv[2]))
