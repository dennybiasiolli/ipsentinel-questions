def fizz_buzz():
    for i in range(1, 101):
        s = ''
        if i % 3 == 0 or '3' in str(i):
            s = 'Fizz'
        if i % 5 == 0 or '5' in str(i):
            s = ' '.join((s, 'Buzz')).lstrip()
        print(s or str(i))


def main():
    fizz_buzz()


if __name__ == "__main__":
    main()
