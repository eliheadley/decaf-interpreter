
def count():
    for i in range(0,15):
        yield i


def main():
    for n in count():
        print(n)

if __name__ == "__main__":
    main()