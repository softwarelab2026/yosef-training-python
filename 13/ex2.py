def anti_bi(string: str) -> str:
    return "".join(ch for ch in string if ch != 'b')

def main():
    print(anti_bi("whbatbs bubp"))

if __name__ == "__main__":
    main()