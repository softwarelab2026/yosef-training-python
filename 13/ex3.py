def main():
    f = lambda x : x + 2
    f2 = lambda x: -x if x < 0 else x 

    lst = [1, -2, 4, -6, 3, -9]
    lst.sort(key= lambda x: f2(x))

    print(f(4))
    print(lst)



if __name__ == "__main__":
    main()