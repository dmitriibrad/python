def odd_num(to):
    for i in range(1, to + 1, 2):
        yield i


def odd_num_no_yield(to):
    return (x for x in range(1, to + 1, 2))


if __name__ == "__main__":
    a_gen = odd_num(15)
    b_gen = odd_num_no_yield(15)

    print("a_gen type", type(a_gen))
    print("b_gen type", type(b_gen))

    for elem in a_gen:
        print(elem)
