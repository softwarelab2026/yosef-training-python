def sum_of_number(number):
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total
    
def print_number_details():
    number = input("please eneter 5 digit number: ")
    if len(number) != 5:
        return "number must be 5 digit"
    print(int(number))
    print(",".join(number))
    print(sum_of_number(int(number)))

