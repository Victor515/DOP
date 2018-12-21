def ints(start, end = None):
    i = start
    while i <= end or end is None:
        yield i
        i = i + 1

def all_ints():
    "Generate integers in the order 0, +1, -1, +2, -2, +3, -3, ..."
    i = 0
    yield i

    while True:
        i = i + 1
        yield i
        yield -i


if __name__ == "__main__":
    for i in all_ints():
        print(i)