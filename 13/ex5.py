def func(n):
    return list(filter(lambda x:  x % 3 == 0, (range(n, 0, -1))))

def main():
    print(func(10))

if __name__ == "__main__":
    main()